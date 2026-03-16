import os
import sys
import logging
from pathlib import Path
from typing import Dict, Set
import asyncio

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import Forbidden

# Import our modules
import config
import advice_data
from shapefile_utils import get_zone_from_shapefile

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(config.LOGS_DIR / 'bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# User state storage
user_state: Dict[int, str] = {}
blocked_users: Set[int] = set()

# Level links - ALL pointing to the SAME channel
level_links = {
    "1": config.CHANNEL_LINK,
    "2": config.CHANNEL_LINK,
    "3": config.CHANNEL_LINK,
    "4": config.CHANNEL_LINK,
    "5": config.CHANNEL_LINK,
    "6": config.CHANNEL_LINK,
    "7": config.CHANNEL_LINK,
    "8": config.CHANNEL_LINK,
    "9": config.CHANNEL_LINK,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    chat_id = update.effective_chat.id
    
    if chat_id in blocked_users:
        return
    
    user_state[chat_id] = "start"
    
    keyboard = [
        [KeyboardButton("🔵 HA"), KeyboardButton("🔴 YO'Q")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "👉 Yashash joyingiz necha ballik zonada ekanligini bilasizmi?",
        reply_markup=reply_markup
    )

async def handle_yes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle 'HA' response - user knows their zone"""
    chat_id = update.effective_chat.id
    user_state[chat_id] = "choose_level"
    
    keyboard = [
        [KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3")],
        [KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6")],
        [KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "📊 Qaysi ballik zonadasiz?\n\n"
        "Tanlagan zonangizga mos zilzila xavfsizligi bo'yicha tavsiyalarni olasiz:",
        reply_markup=reply_markup
    )

async def handle_level_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle level selection and give advice"""
    chat_id = update.effective_chat.id
    level = update.message.text
    
    if level in level_links:
        # Get advice for this zone
        advice = advice_data.EARTHQUAKE_ADVICE.get(level, {})
        
        if advice:
            # Send the advice
            await update.message.reply_text(
                advice["advice"],
                parse_mode='Markdown',
                reply_markup=ReplyKeyboardRemove()
            )
            
            # Send precautions as a nice list
            precautions_text = "📋 **Tayyorlanish ro'yxati:**\n\n"
            for i, item in enumerate(advice.get("precautions", []), 1):
                precautions_text += f"{i}. {item}\n"
            
            await update.message.reply_text(
                precautions_text,
                parse_mode='Markdown'
            )
            
            # Send the Telegram channel link - ALL ZONES point to same channel
            await update.message.reply_text(
                f"📢 **Batafsil ma'lumot va yangiliklar uchun kanalimiz:**\n"
                f"🔗 [{config.CHANNEL_NAME}]({config.CHANNEL_LINK})\n\n"
                f"⚠️ *Eslatma:* Ushbu kanalda zilzila xavfsizligi bo'yicha muhim ma'lumotlar joylanadi.",
                parse_mode='Markdown',
                disable_web_page_preview=False
            )
        else:
            await update.message.reply_text(
                f"✅ Siz {level} ballik zonani tanladingiz.\n\n"
                f"👉 {level_links[level]}",
                reply_markup=ReplyKeyboardRemove()
            )
        
        if chat_id in user_state:
            del user_state[chat_id]

async def handle_no(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle 'YO'Q' response - user doesn't know their zone"""
    chat_id = update.effective_chat.id
    user_state[chat_id] = "waiting_location"
    
    location_button = KeyboardButton("📍 Lokatsiyani yuborish", request_location=True)
    reply_markup = ReplyKeyboardMarkup(
        [[location_button]], 
        resize_keyboard=True, 
        one_time_keyboard=True
    )
    
    await update.message.reply_text(
        "🏠 Iltimos, yashash joyingizni yuboring 👇\n\n"
        "Bot sizning joylashuvingizni tahlil qilib, qaysi seysmik zonada ekanligingizni aniqlaydi "
        "va xavfsizlik bo'yicha tavsiyalar beradi.",
        reply_markup=reply_markup
    )

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle location message and give zone-specific advice"""
    chat_id = update.effective_chat.id
    
    if chat_id in user_state and user_state[chat_id] == "waiting_location":
        lat = update.message.location.latitude
        lon = update.message.location.longitude
        
        # Send processing message
        processing_msg = await update.message.reply_text(
            "🔄 Joylashuvingiz tahlil qilinmoqda..."
        )
        
        # Log coordinates for debugging
        logger.info(f"Received location from user {chat_id}: lat={lat}, lon={lon}")
        
        # Get zone from shapefile
        zone = get_zone_from_shapefile(lat, lon, config.SHAPEFILE_PATH)
        
        if zone and zone in advice_data.EARTHQUAKE_ADVICE:
            # Delete processing message
            await processing_msg.delete()
            
            # Get advice for this zone
            advice = advice_data.EARTHQUAKE_ADVICE[zone]
            
            # Send location confirmation
            await update.message.reply_text(
                f"📍 Sizning joylashuvingiz: {lat:.4f}, {lon:.4f}\n"
                f"🏠 Aniqlangan zona: **{zone} ball**",
                parse_mode='Markdown'
            )
            
            # Send the advice
            await update.message.reply_text(
                advice["advice"],
                parse_mode='Markdown'
            )
            
            # Send precautions as a nice list
            precautions_text = "📋 **Tayyorlanish ro'yxati:**\n\n"
            for i, item in enumerate(advice.get("precautions", []), 1):
                precautions_text += f"{i}. {item}\n"
            
            await update.message.reply_text(
                precautions_text,
                parse_mode='Markdown'
            )
            
            # Send the Telegram channel link
            await update.message.reply_text(
                f"📢 **Batafsil ma'lumot va yangiliklar uchun kanalimiz:**\n"
                f"🔗 [{config.CHANNEL_NAME}]({config.CHANNEL_LINK})\n\n"
                f"⚠️ *Eslatma:* Ushbu kanalda zilzila xavfsizligi bo'yicha muhim ma'lumotlar joylanadi.",
                parse_mode='Markdown',
                disable_web_page_preview=False
            )
        else:
            # More helpful error message
            error_msg = "❌ Kechirasiz, sizning joylashuvingizni aniqlab bo'lmadi.\n\n"
            
            if not zone:
                error_msg += "🔍 **Sabablari:**\n"
                error_msg += "• Sizning joylashuvingiz O'zbekiston hududidan tashqarida bo'lishi mumkin\n"
                error_msg += "• Yuborilgan lokatsiya aniq emas\n"
                error_msg += "• Xaritada sizning zonangiz aniqlanmagan\n\n"
            else:
                error_msg += f"Aniqlangan zona: {zone}, lekin ma'lumot topilmadi.\n\n"
            
            error_msg += "📝 **Tavsiyalar:**\n"
            error_msg += "• Qaytadan lokatsiya yuboring\n"
            error_msg += "• Yoki qaysi zonada ekanligingizni bilsangiz, HA tugmasini bosing\n"
            error_msg += "• Yordam: /start"
            
            await processing_msg.edit_text(error_msg)
            
            # Log the issue
            logger.warning(f"Zone detection failed for user {chat_id}, lat={lat}, lon={lon}, zone={zone}")
        
        # Clear user state
        if chat_id in user_state:
            del user_state[chat_id]
    """Handle location message and give zone-specific advice"""
    chat_id = update.effective_chat.id
    
    if chat_id in user_state and user_state[chat_id] == "waiting_location":
        lat = update.message.location.latitude
        lon = update.message.location.longitude
        
        # Send processing message
        processing_msg = await update.message.reply_text(
            "🔄 Joylashuvingiz tahlil qilinmoqda..."
        )
        
        # Get zone from shapefile
        zone = get_zone_from_shapefile(lat, lon, config.SHAPEFILE_PATH)
        
        if zone and zone in advice_data.EARTHQUAKE_ADVICE:
            # Delete processing message
            await processing_msg.delete()
            
            # Get advice for this zone
            advice = advice_data.EARTHQUAKE_ADVICE[zone]
            
            # Send location confirmation
            await update.message.reply_text(
                f"📍 Sizning joylashuvingiz: {lat:.4f}, {lon:.4f}\n"
                f"🏠 Aniqlangan zona: **{zone} ball**",
                parse_mode='Markdown'
            )
            
            # Send the advice
            await update.message.reply_text(
                advice["advice"],
                parse_mode='Markdown'
            )
            
            # Send precautions as a nice list
            precautions_text = "📋 **Tayyorlanish ro'yxati:**\n\n"
            for i, item in enumerate(advice.get("precautions", []), 1):
                precautions_text += f"{i}. {item}\n"
            
            await update.message.reply_text(
                precautions_text,
                parse_mode='Markdown'
            )
            
            # Send the Telegram channel link - ALL ZONES point to same channel
            await update.message.reply_text(
                f"📢 **Batafsil ma'lumot va yangiliklar uchun kanalimiz:**\n"
                f"🔗 [{config.CHANNEL_NAME}]({config.CHANNEL_LINK})\n\n"
                f"⚠️ *Eslatma:* Ushbu kanalda zilzila xavfsizligi bo'yicha muhim ma'lumotlar joylanadi.",
                parse_mode='Markdown',
                disable_web_page_preview=False
            )
        else:
            await processing_msg.edit_text(
                "❌ Kechirasiz, sizning joylashuvingizni aniqlab bo'lmadi.\n"
                "Iltimos, qaytadan urinib ko'ring yoki boshqa joyni yuboring.\n\n"
                "Yordam: /start"
            )
        
        # Clear user state
        if chat_id in user_state:
            del user_state[chat_id]

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages"""
    chat_id = update.effective_chat.id
    
    if chat_id in blocked_users:
        return
    
    text = update.message.text
    
    if text == "🔵 HA":
        await handle_yes(update, context)
    elif text == "🔴 YO'Q":
        await handle_no(update, context)
    elif (chat_id in user_state and 
          user_state[chat_id] == "choose_level" and 
          text in level_links):
        await handle_level_choice(update, context)
    else:
        # Unknown command
        await update.message.reply_text(
            "❌ Noto'g'ri buyruq. Iltimos, /start ni bosing."
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    try:
        raise context.error
    except Forbidden as e:
        # User blocked the bot
        if update and update.effective_chat:
            blocked_users.add(update.effective_chat.id)
            logger.info(f"User {update.effective_chat.id} blocked the bot")
    except Exception as e:
        logger.error(f"Update {update} caused error {e}")

def main():
    """Main function to run the bot"""
    # Check if shapefile exists
    if not config.SHAPEFILE_PATH.exists():
        logger.warning(f"Shapefile not found at: {config.SHAPEFILE_PATH}")
        logger.warning("Location detection will not work until shapefile is added!")
        logger.warning("Please add your shapefile to: Data/U/ExportOutput9.shp")
    
    # Create application
    application = Application.builder().token(config.BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.LOCATION, handle_location))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Bot ishga tushdi! Waiting for messages...")
    logger.info(f"Telegram channel: {config.CHANNEL_NAME} - {config.CHANNEL_LINK}")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
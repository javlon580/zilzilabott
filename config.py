import os
from pathlib import Path

# Bot token
BOT_TOKEN = "6698742855:AAG0XMhviwtXTRP4pjOhBVrDCP6eyCCqu4c"

# Base directory
BASE_DIR = Path(__file__).parent.absolute()

# Shapefile path - using the correct path with uppercase DATA
SHAPEFILE_PATH = BASE_DIR / "DATA" / "U" / "Export_Output_9.shp"

# Logs directory
LOGS_DIR = BASE_DIR / "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Telegram channel - SINGLE CHANNEL FOR ALL ZONES
CHANNEL_LINK = "https://t.me/seysmik_xavfsizlik_1"
CHANNEL_NAME = "Seysmik Xavfsizlik kanali"
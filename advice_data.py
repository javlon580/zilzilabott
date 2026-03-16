"""
Earthquake safety advice for different seismic zones (1-9)
Higher zone numbers mean stronger potential earthquakes
"""

EARTHQUAKE_ADVICE = {
    "1": {
        "title": "🏠 1 ballik zona (Xavfsiz zona)",
        "advice": """
✅ Siz eng xavfsiz zonada yashayapsiz!

📌 **Tavsiyalar:**
• Kuchli zilzilalar bo'lish ehtimoli juda past
• Oddiy qurilish qoidalariga rioya qiling
• Har ehtimolga qarshi 3 kunlik oziq-ovqat va suv zaxirasi saqlang

🔧 **Uyingizda:**
• Shiftga osilgan narsalarni mahkamlang
• Og'ir mebellarni devorga mahkamlash tavsiya etiladi

📞 **Muhim telefonlar:**
• Favqulodda vaziyatlar: 112
• Seysmologik xizmat: +99871 123-45-67
""",
        "precautions": [
            "3 kunlik oziq-ovqat va suv zaxirasi",
            "Birinchi yordam aptechkasi",
            "Fonar va zaxira batareyalar"
        ]
    },
    
    "2": {
        "title": "🏠 2 ballik zona (Past xavf)",
        "advice": """
✅ Siz past xavfli zonada yashayapsiz!

📌 **Tavsiyalar:**
• Yengil zilzilalar sezilishi mumkin
• Uyingizda xavfsizlik choralarini ko'ring
• Yiliga 1 marta xavfsizlik mashg'uloti o'tkazing

🔧 **Uyingizda:**
• Barcha osma narsalarni mahkamlang
• Kitob javonlari va shkaflarni devorga mahkamlang
• Gaz ballonlarini mustahkam joylashtiring

🚨 **Zilzila paytida:**
• "Yerga yoting, Himoyalaning, Tuting" qoidasini eslang
• Deraza va oynalardan uzoq turing
• Stol yoki karavot tagiga yoting

📞 **Muhim telefonlar:**
• Favqulodda vaziyatlar: 112
• Seysmologik xizmat: +99871 123-45-67
""",
        "precautions": [
            "7 kunlik oziq-ovqat va suv zaxirasi",
            "Yoritish vositalari (fonar, sham)",
            "Birinchi yordam aptechkasi va dorilar",
            "Hujjatlar nusxasi (zip-paketda)"
        ]
    },
    
    "3": {
        "title": "🏠 3 ballik zona (O'rtacha xavf)",
        "advice": """
⚠️ Siz o'rtacha xavfli zonada yashayapsiz!

📌 **Tavsiyalar:**
• 3-4 balli zilzilalar bo'lishi mumkin
• Uyingizni zilzilaga tayyorlang
• Oilangiz bilan evakuatsiya rejasini tuzing

🔧 **Uyingizda:**
• Barcha mebellarni devorga mahkamlang
• Gaz va suv quvurlarini tekshiring
• Elektr simlarini yangilang

🚨 **Zilzila paytida:**
• Binodan chiqishga shoshilmang
• Ichki devor yonida yoki stol tagida himoyalaning
• Liftdan foydalanmang

💊 **Favqulodda to'plam:**
• 10 kunlik oziq-ovqat va suv
• Birinchi yordam vositalari
• Issiq kiyim va adyol
""",
        "precautions": [
            "10 kunlik oziq-ovqat va suv zaxirasi",
            "To'liq birinchi yordam to'plami",
            "Portativ radio va batareyalar",
            "Issiq kiyim va adyol",
            "Ko'p funksiyali asbob (multitool)"
        ]
    },
    
    "4": {
        "title": "🏠 4 ballik zona (O'rtacha xavf)",
        "advice": """
⚠️ Siz o'rtacha xavfli zonada yashayapsiz!
4 balli zilzilalar sezilarli bo'lishi mumkin.

📌 **Asosiy tavsiyalar:**
• Uyingizni zilzilaga mustahkamlang
• Oilaviy evakuatsiya rejasini tuzing
• Muntazam mashg'ulotlar o'tkazing

🔧 **Qurilish talablari:**
• Bino seysmik talablarga javob berishi kerak
• Poydevor mustahkamligini tekshiring
• Yoriqlarni kuzatib boring

🚨 **Zilzila paytida:**
• Vahimaga berilmang
• Xavfsiz joyni toping (stol tagi, ichki devor yoni)
• Boshingizni himoyalang

📦 **Favqulodda to'plam:**
• 2 haftalik oziq-ovqat va suv
• Dori-darmonlar
• Hujjatlar nusxalari
""",
        "precautions": [
            "14 kunlik oziq-ovqat va suv zaxirasi",
            "To'liq birinchi yordam to'plami",
            "Portativ radio, fonar, batareyalar",
            "Issiq kiyim va adyol",
            "Shaxsiy gigiena vositalari",
            "Ko'p funksiyali asbob"
        ]
    },
    
    "5": {
        "title": "🏠 5 ballik zona (Xavfli zona)",
        "advice": """
🚨 Siz xavfli zonada yashayapsiz!
5 balli zilzilalar binolarga zarar yetkazishi mumkin.

📌 **MUHIM TAVSIYALAR:**
• Uyingiz seysmik talablarga javob berishini tekshiring
• Har 3 oyda evakuatsiya mashg'uloti o'tkazing
• Favqulodda to'plamingizni doim tayyor saqlang

🏗 **Bino xavfsizligi:**
• Professional tekshiruvdan o'tkazing
• Zarur mustahkamlash ishlarini bajaring
• Yoriqlarni kuzatib boring

🚨 **Zilzila paytida:**
• Xotirjamlikni saqlang
• Stol tagida yoki ichki devor yonida himoyalaning
• Deraza va osma narsalardan uzoq turing

📦 **MAJBURIY TO'PLAM:**
• 3 haftalik oziq-ovqat va suv
• Birinchi yordam va dori-darmonlar
• Issiq kiyim, hujjatlar, pul
""",
        "precautions": [
            "21 kunlik oziq-ovqat va suv zaxirasi",
            "Kengaytirilgan birinchi yordam to'plami",
            "2 ta fonar va zaxira batareyalar",
            "Portativ radio, power bank",
            "Issiq kiyim, adyol, palatka",
            "Hujjatlar, pullar (naqd)",
            "Gaz va suvni o'chirish kaliti"
        ]
    },
    
    "6": {
        "title": "🏠 6 ballik zona (Yuqori xavf)",
        "advice": """
🚨🚨 Siz YUQORI XAVFLI zonada yashayapsiz!
6 balli zilzilalar jiddiy zarar yetkazishi mumkin.

📌 **HAYOTIY MUHIM TAVSIYALAR:**

🏗 **BINO XAVFSIZLIGI:**
• ✓ Seysmik mustahkamlash MAJBURIY
• ✓ Har yili professional tekshiruv
• ✓ Barcha yoriqlarni kuzatib boring

🏠 **UY TAYYORGARLIGI:**
• Barcha mebellarni devorga MAHKAM lang
• Osma narsalarni xavfsiz joylashtiring
• Gaz va suv o'chirish vanalarini belgilang

👨‍👩‍👧 **OILA REJASI:**
• Uchrashish joyini belgilang
• Har oyda mashg'ulot o'tkazing
• Bolalarga o'rgating

🚨 **ZILZILA VAQTIDA:**
1. YERGA YOTING
2. HIMOYALANING (stol tagi)
3. TUTING (tebranish to'xtaguncha)

📦 **FAVQULODDA TO'PLAM (DOIM TAYYOR):**
• 1 oylik oziq-ovqat va suv
• To'liq tibbiy to'plam
• Issiqlik saqlovchi kiyim-kechak
• Chodir, uyqu to'plami
""",
        "precautions": [
            "30 kunlik oziq-ovqat va suv zaxirasi",
            "To'liq tibbiy to'plam va maxsus dorilar",
            "Chodir, uyqu to'plami, issiq kiyim",
            "2 ta fonar, radio, power bank",
            "Gaz plitasi, qozon, idishlar",
            "Hujjatlar, pullar, bank kartalari",
            "Ko'p funksiyali asboblar",
            "Shaxsiy gigiena vositalari (1 oylik)",
            "Bolalar va uy hayvonlari uchun"
        ]
    },
    
    "7": {
        "title": "🏠 7 ballik zona (Juda yuqori xavf)",
        "advice": """
🆘🆘🆘 Siz JUDA YUQORI XAVFLI zonada yashayapsiz!
7 balli zilzilalar binolarni vayron qilishi mumkin!

📌 **HAYOT MAMOT MASALASI:**

🏗 **BINO XAVFSIZLIGI 1-RAQAMLI VAZIFA:**
• ❗ MAJBURIY seysmik mustahkamlash
• ❗ Professional tekshiruv (yiliga 2 marta)
• ❗ Zilzilaga chidamli qurilish

🏠 **UY TAYYORGARLIGI:**
• Barcha narsalar mahkamlangan bo'lishi shart
• Xavfsiz joylarni belgilang (stol taglari, burchaklar)
• Chiqish yo'llarini to'siqsiz saqlang

👨‍👩‍👧 **OILAVIY REJA:**
• Har oyda MAJBURIY mashg'ulot
• 2 ta uchrashish joyi belgilang
• Qo'shnilar bilan hamkorlik qiling

🚨 **ZILZILA PROTOKOLI:**
1. TUSHUNING - bu zilzila!
2. HIMOYALANING - "Uchburchak hayot" qoidasi
3. KUTING - tebranish to'xtaguncha
4. EVAKUATSIYA - xavfsiz joyga

📦 **FAVQULODDA TO'PLAM (2 TA):**
• Birinchi to'plam - uyda
• Ikkinchi to'plam - mashinada/ishda
• 45 kunlik minimal zaxira
""",
        "precautions": [
            "45 kunlik oziq-ovqat va suv zaxirasi",
            "2 ta to'liq tibbiy to'plam",
            "2 ta chodir, uyqu to'plami, issiq kiyim",
            "Portativ gaz plitasi, 2 ta qozon",
            "3 ta fonar, radio, 2 ta power bank",
            "Hujjatlar, pullar, zargarlik buyumlari",
            "Maxsus dorilar (2 oylik)",
            "Bolalar formulasi, tagliklar",
            "Uy hayvonlari uchun oziq",
            "Ko'p funksiyali asboblar to'plami",
            "Issiqlik saqlovchi adyollar"
        ]
    },
    
    "8": {
        "title": "🏠 8 ballik zona (Eng xavfli zona)",
        "advice": """
💀💀💀 Siz ENG XAVFLI zonada yashayapsiz!
8 balli zilzilalar KATTA vayronagarchilik keltirishi mumkin!

📌 **BU JIDDIY - HAYOT UCHUN KURASH:**

🏗 **BINO - HAYOTINGIZ UNGA BOG'LIQ:**
• ❗❗ MAJBURIY mustahkamlash (hozir!)
• ❗❗ Seysmik audit (yiliga 2-3 marta)
• ❗❗ Zilzilaga to'liq mos qurilish

⚠️ **AGAR BINO ESKI BO'LSA:**
• Tezda seysmik tekshiruv
• Zarur mustahkamlash ishlari
• Vaqtinchalik xavfsizroq joyga ko'chish

🏠 **XAVFSIZ MAKON YARATING:**
• Mustahkam stol/jadval (boshpana)
• Burchaklar (uchburchak hayot zonasi)
• Derazalardan uzoq joylar

👨‍👩‍👧 **OILAVIY HIMOYA:**
• Har 2 haftada mashg'ulot
• Signal tizimi o'rnating
• Qo'shnilar bilan birlashing

🚨 **ZILZILA VAQTIDA:**
❌ Derazalardan uzoq
❌ Oshxonadan uzoq
❌ Osma narsalardan uzoq
✅ "Uchburchak hayot" zonasiga
✅ Bosh va bo'yinni himoyalang

📦 **FAVQULODDA TO'PLAM (KO'CHISHGA TAYYOR):**
• 60 kunlik minimal zaxira
• "Go-bag" - tez evakuatsiya sumkasi
• "Stay-bag" - uyda qolish uchun
""",
        "precautions": [
            "60 kunlik oziq-ovqat va suv zaxirasi",
            "3 ta tibbiy to'plam (uy, mashina, ish)",
            "2 ta chodir, 2 ta uyqu to'plami",
            "Maxsus qishki kiyim to'plami",
            "Portativ gaz plitasi va 2 ta ballon",
            "3 ta fonar, radio, 2 ta power bank",
            "Hujjatlar nusxalari (vodorod)",
            "2 oylik maxsus dorilar",
            "Bolalar uchun MAXSUS to'plam",
            "Kommunikatsiya vositalari",
            "GPS, xarita, kompas",
            "Ko'p funksiyali asboblar",
            "Issiqlik saqlovchi vositalar",
            "Gigiena to'plami (2 oylik)"
        ]
    },
    
    "9": {
        "title": "🏠 9 ballik zona (KATASTROFIK XAVF)",
        "advice": """
☢️☢️☢️ Siz KATASTROFIK XAVFLI zonada yashayapsiz!
9 balli zilzilalar BUTUNLAY vayron qiluvchi kuchga ega!

📌 **BU FAVQULODDA HOLAT - MAXSUS TAYYORGARLIK TALAB ETILADI:**

⚠️⚠️⚠️ **HAYOTIY MUHIM KO'RSATMALAR:**

🏗 **QURILISH TALABLARI:**
• ❗❗❗ Maxsus seysmik loyiha
• ❗❗❗ Davlat ekspertizasi
• ❗❗❗ Eng zamonaviy texnologiyalar
• ESKI BINOLARDA YASHASH XAVFLI!

🏠 **MAXSUS BOSHPANA:**
• Uyingizda seysmik xavfsiz xona
• Mustahkam temir-beton konstruksiya
• 2 ta chiqish yo'li
• Aloqa vositalari

👨‍👩‍👧 **OILA PROTOKOLI:**
• Har hafta mashg'ulot
• Maxsus signal so'zlari
• 3 ta uchrashish joyi
• Qo'shnilar bilan maxsus guruh

📋 **DOIMIY TAYYORGARLIK:**
• Seysmik monitoring kuzatuvi
• Erta ogohlantirish tizimiga ulanish
• Mahalliy shtab bilan aloqa

🚨 **ZILZILA PROTOKOLI (AVTOMAT):**
1. SIGNAL - 5 soniya ichida harakat
2. HIMOYA - maxsus boshpanaga
3. KUTISH - 24 soatgacha
4. EVAKUATSIYA - belgilangan marshrut

📦 **FAVQULODDA TO'PLAM (MAXSUS TARKIB):**
• 90 kunlik hayotiy zaxira
• Maxsus himoya vositalari
• Avtonom hayot tizimi
""",
        "precautions": [
            "90 kunlik oziq-ovqat va suv zaxirasi",
            "Maxsus himoya vositalari (kaska, himoya oyoq kiyimi)",
            "3 ta tibbiy to'plam + jarrohlik asboblari",
            "2 ta professional chodir, maxsus uyqu to'plami",
            "Portativ generator va yoqilg'i",
            "Sun'iy yo'ldosh telefoni",
            "Professional radio stansiya",
            "GPS, xarita, kompas, sekstant",
            "Maxsus qutqaruv asboblari",
            "Suv tozalash tizimi",
            "Harbiy ratsion",
            "Maxsus dorilar (3 oylik)",
            "Nafas olish apparati",
            "Kimyoviy himoya vositalari",
            "Bolalar va chaqaloqlar uchun MAXSUS to'plam",
            "Evakuatsiya qo'llanmasi"
        ]
    }
}
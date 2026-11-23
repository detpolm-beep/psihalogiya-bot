"""Bot konfiguratsiyasi: tokenni muhit o'zgaruvchisidan o'qiydi."""

import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN topilmadi!\n"
        "Quyidagi qadamlarni bajaring:\n"
        "  1. Telegram'da @BotFather ga /newbot yuboring va yangi bot yarating\n"
        "  2. Sizga token beriladi — uni nusxalang\n"
        "  3. Loyiha papkasida .env faylini yarating (.env.example namunadan)\n"
        "     va BOT_TOKEN=... qatorini yozing\n"
    )

ADMIN_IDS = [
    int(x)
    for x in os.getenv("ADMIN_IDS", "").split(",")
    if x.strip().isdigit()
]

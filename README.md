# 🤖 Psixologiya Testlari — Telegram Bot

Telegram bot foydalanuvchilarga **psixologik testlar** topshirishga imkon beradi:
savollar inline tugmalar orqali, yakunda avtomatik ball va izoh beriladi.

## ✨ Imkoniyatlar

- 4 ta test:
  - 😰 **Stress darajasi** (8 savol)
  - 😟 **Xavotir (anshedlik) darajasi** (GAD-7, 7 savol)
  - 😔 **Depressiv belgilar** (PHQ-9, 9 savol)
  - 💪 **O'z-o'zini baholash** (self-esteem, 10 savol)
- Inline tugmalar bilan qulay javob berish
- Avtomatik ball hisoblash va izoh
- Depressiya testida xavfsizlik eslatmasi (o'ziga zarar haqida savol)
- `/start`, `/help`, `/cancel` buyruqlari

> ⚠️ Testlar faqat ma'lumot berish maqsadida. Tibbiy yoki klinik diagnoz emas.
> Jiddiy holatlarda mutaxassisga (shifokor yoki psixolog) murojaat qiling.

## 🧰 Talablar

- Python 3.10+ (loyiha Python 3.11 da sinovdan o'tgan)
- Telegram Bot Token ([@BotFather](https://t.me/BotFather) dan olinadi)

> ℹ️ `requirements.txt` da aiogram `3.13..3.15` versiyasi belgilangan.
> Buning sababi: aiogram `3.16+` `rich_text_union` orqali Python 3.12+ talab
> qiladi, tizimingizda esa Python 3.11. Agar Python 3.12+ o'rnatgan bo'lsangiz,
> `requirements.txt` dan yuqori cheklovni olib tashlab, eng so'nggi aiogram'ni
> ishlatishingiz mumkin.

## 🚀 O'rnatish va ishga tushirish

1. **Kutubxonalarni o'rnatish**
   ```powershell
   py -m pip install -r requirements.txt
   ```

2. **Bot tokenini olish**
   - Telegram'da [@BotFather](https://t.me/BotFather) ga `/newbot` yuboring
   - Botga nom bering — sizga `BOT_TOKEN` beriladi

3. **`.env` faylini yarating** (`.env.example` namunadan nusxa oling)
   ```powershell
   Copy-Item .env.example .env
   ```
   So'ng `.env` ichidagi qatorni o'zgartiring:
   ```
   BOT_TOKEN=123456789:SizningHaqiqiyTokeningiz
   ```

4. **Botni ishga tushiring**
   ```powershell
   py bot.py
   ```
   Konsolda `Bot ishga tushdi: @your_bot` ko'rinishida xabar chiqadi.

5. **Telegram'da botni toping** va `/start` yuboring. 🎉

## 📁 Loyiha tuzilmasi

```
.
├── bot.py              # ishga tushiruvchi skript
├── config.py           # tokenni yuklash
├── states.py           # FSM holatlari
├── keyboards.py        # inline tugmalar
├── data/
│   └── tests.py        # testlar bazasi (savollar, ball, natijalar)
├── handlers/
│   ├── common.py      # /start, /help, /cancel, menyu
│   └── testing.py     # tanlash, javob, natija
├── requirements.txt
├── .env.example
└── .gitignore
```

## 🛠️ Yangi test qo'shish

`data/tests.py` dagi `TESTS` lug'atiga yangi kalit qo'shing:

```python
"my_test": {
    "title": "🎯 Mening testim",
    "description": "Test haqida qisqa izoh.",
    "questions": [
        {
            "text": "Savol matni?",
            "options": [
                {"text": "Variant A", "score": 0},
                {"text": "Variant B", "score": 1},
            ],
        },
    ],
    "results": [
        {"min": 0, "max": 1, "text": "Natija matni."},
        {"min": 2, "max": 2, "text": "Yuqori natija matni."},
    ],
},
```

Faqat shu — menyu va handler'lar avtomatik yangi testni ko'rsatadi.

## 📝 Eslatma

- Natijalar faqat ma'lumot berish uchun; ular shifokor yoki psixolog
  diagnozi o'rnini bosmaydi.
- Ma'lumotlar faqat joriy seansda (xotira) saqlanadi — bot qayta
  ishga tushganda tozalanadi.


## 🔧 Admin panel

Botda admin panel mavjud: statistika, foydalanuvchilar ro'yxati,
ommaviy xabar (broadcast) va bot haqida ma'lumot.

### Admin'ni sozlash

1. O'z Telegram ID'ingizni bilib oling:
   - Botga `/admin` yuboring (ADMIN_IDS bo'sh bo'lsa, bot sizning ID'ingizni chiqaradi)
   - yoki [@userinfobot](https://t.me/userinfobot) ga istalgan xabar yuboring
2. `.env` faylga qo'shing:
   ```
   ADMIN_IDS=123456789
   ```
   (Bir nechta admin uchun vergul bilan: `ADMIN_IDS=111,222`)
3. Botni qayta ishga tushiring: `py bot.py`

### Imkoniyatlar

- `/admin` — admin panel menyusi
- **📊 Statistika** — jami foydalanuvchilar, jami testlar, har test bo'yicha
  hisob, bugungi va oxirgi 7 kunlik statistika
- **👥 Foydalanuvchilar** — jami soni va oxirgi 10 ta foydalanuvchi ro'yxati
- **📢 Xabar yuborish** — barcha foydalanuvchilarga xabar/matn/rasm yuborish
  (broadcast). Yuborilgan xabar `copy_message` orqali uzatiladi, shu sabab
  matn, rasm, video, ovozli xabar va h.k. qo'llab-quvvatlanadi.
- **ℹ️ Bot haqida** — username, ID, admin'lar ro'yxati, ish vaqti (uptime)

### Ma'lumotlar bazasi

- SQLite — `bot.db` faylida saqlanadi (loyiha papkasida).
- Jadvallar: `users` (foydalanuvchilar), `test_results` (o'tkazilgan testlar).
- Foydalanuvchi `/start` da ro'yxatga olinadi; har yakunlangan test natijasi
  yozib qo'yiladi.
- `bot.db` git'ga tushmaydi (.gitignore'da).

"""Psixologik testlar bazasi.

Eslatma: bu testlar ommaviy ma'lumot berish maqsadida moslashtirilgan.
Ular rasmiy klinik diagnoz o'rnida o'tmaydi. Jiddiy holatlarda
mutaxassisga (shifokor yoki psixolog) murojaat qiling.
"""

DISCLAIMER = (
    "⚠️ Eslatma: bu testlar faqat ma'lumot berish maqsadida. "
    "Tibbiy yoki klinik diagnoz emas. Jiddiy holatlarda "
    "mutaxassisga (shifokor yoki psixolog) murojaat qiling."
)


TESTS = {
    # -------------------------------------------------- kasbiy stress
    "job_stress": {
        "title": "💼 Kasbiy stress darajasi",
        "description": (
            "Vaysman anketasi — kasbiy stressga chidamlilik darajasi.\n"
            "Har bir savolga qanchalik tez-tez duch kelishingizni belgilang."
        ),
        "questions": [
            {
                "text": "O'z majburiyatlaringizni bajarishda salohiyatingiz "
                "yetarli darajada emasligini his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Vazifangizni bajarishda noqulayliklarni "
                "his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Martabangiz ko'tarilishi uchun imkoniyatlardan "
                "qanday foydalanishni bilmay qolgan vaqtlaringiz bo'lganmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Kun davomida haddan tashqari charchaganingizda, "
                "ishlaringizga ulgurmaganingizni his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Atrofingizdagi insonlarning bir-biriga zid "
                "talablarini qondira olmasligingizni his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Ishingizni bajarish uchun yetarli darajada "
                "malakaga ega emasligingizni his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Rahbaringiz siz haqingizda qanday fikrda va "
                "ishingizga qay darajada baho berishini bilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Ishingiz uchun kerakli ma'lumotlarni "
                "ololmaydigan vaziyatlar tez-tez bo'lib turadimi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Qabul qilgan qarorlaringiz boshqalarning "
                "hayotiga ta'sir qilishi sizni xavotirga soladimi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Hamkasblaringiz sizni xushlamasliklarini va "
                "jamoaga qabul qilmasliklarini his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Rahbaringizning sizga nisbatan qabul qilgan "
                "qarorlariga ta'sir qila olasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Hamkasblaringiz sizdan nimalar "
                "kutayotganliklarini bilmay qolgan vaqtlaringiz bo'ladimi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Bajarishingiz kerak bo'lgan ishlarning miqdori "
                "sifatiga qanchalik ta'sir qiladi deb o'ylaysiz?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "O'z fikrlaringizga zid ish qilishingiz "
                "kerakligini his qilasizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
            {
                "text": "Ishingiz oilaviy hayotingizga salbiy ta'sir "
                "qiladi deb o'ylaysizmi?",
                "options": [
                    {"text": "Hech qachon", "score": 1},
                    {"text": "Kamdan-kam hollarda", "score": 2},
                    {"text": "Ba'zan", "score": 3},
                    {"text": "Tez-tez", "score": 4},
                    {"text": "Deyarli har doim", "score": 5},
                ],
            },
        ],
        "results": [
            {
                "min": 15, "max": 29,
                "text": "Kasbiy stress darajasi <b>past</b>. "
                "Ish muhitida o'zingizni qulay his qilyapsiz. 🟢",
            },
            {
                "min": 30, "max": 52,
                "text": "Kasbiy stress darajasi <b>o'rtacha</b>. "
                "Dam olishga va ish-hayot balansiga e'tibor qarating. 🟡",
            },
            {
                "min": 53, "max": 75,
                "text": "Kasbiy stress darajasi <b>yuqori</b>. "
                "Stress manbalarini aniqlash va mutaxassis bilan "
                "maslahatlashish tavsiya etiladi. 🔴",
            },
        ],
    },
    # ------------------------------------------------- ishdan qoniqish
    "job_satisfaction": {
        "title": "😊 Ishdan qoniqish darajasi",
        "description": (
            "Rozanova metodikasi — ishdan qoniqish darajasini aniqlash.\n"
            "Har bir savolga to'g'ri keladigan javobni belgilang."
        ),
        "questions": [
            {
                "text": "Siz ishlayotgan muassasadan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Ishxonangizdagi mavjud sharoitlardan "
                "(issiq, sovuq, shovqin va b.) qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "O'z ishingizdan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Hamkasblaringizning uyg'unlikdagi "
                "harakatlaridan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Rahbaringizning ish uslubidan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Rahbaringizning kasbiy malakasi va "
                "kompetentsiyasidan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Mehnatga to'lanayotgan ish haqingizdan "
                "qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Boshqa muassasalardagi shunaqa ish "
                "haqqi bilan solishtirganda, o'z ish haqingizdan "
                "qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Mavqeyingiz darajasidan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Ishingizni oldinga siljish "
                "imkoniyatlaridan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Ish faoliyatingizda o'z tajribangiz va "
                "qobiliyatingizdan foydalanish darajasidan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Ishda o'rnatilgan talablarning aqliy "
                "qobiliyatingizga mosligidan qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Ish kuni uchun belgilangan ish soatidan "
                "qoniqasizmi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
            {
                "text": "Agar boshqa ishga o'tish hohishingiz bo'lsa, "
                "ishingizdan qoniqishingiz qaror qabul qilishingizda "
                "qanchalik ta'sir qiladi?",
                "options": [
                    {"text": "To'liq qoniqaman", "score": 1},
                    {"text": "Qoniqaman", "score": 2},
                    {"text": "To'liq qoniqdim deyolmayman", "score": 3},
                    {"text": "Qoniqdim deyolmayman", "score": 4},
                    {"text": "Umuman qoniqdim deyolmayman", "score": 5},
                ],
            },
        ],
        "results": [
            {
                "min": 14, "max": 32,
                "text": "Ishdan qoniqish darajasi <b>yuqori</b>. "
                "Ish muhitingiz va sharoitlaringizdan mamnunsiz. 🟢",
            },
            {
                "min": 33, "max": 44,
                "text": "Ishdan qoniqish darajasi <b>o'rtacha</b>. "
                "Ba'zi sohalar yaxshilanishi mumkin — ularga e'tibor "
                "qarating. 🟡",
            },
            {
                "min": 45, "max": 70,
                "text": "Ishdan qoniqish darajasi <b>past</b>. "
                "Ish muhitingizda jiddiy muammolar mavjud. "
                "Rahbariyat yoki HR bilan ochiq muloqot foydali bo'lishi "
                "mumkin. 🔴",
            },
        ],
    },
}


def max_score(test: dict) -> int:
    """Berilgan test uchun mumkin bo'lgan maksimal ball."""
    return sum(
        max(option["score"] for option in question["options"])
        for question in test["questions"]
    )


def get_result_text(test: dict, score: int) -> str:
    """Ballga mos natija matnini qaytaradi."""
    for result in test["results"]:
        if result["min"] <= score <= result["max"]:
            return result["text"]
    return "Natija aniqlanmadi."

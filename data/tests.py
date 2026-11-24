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


def _options_never_rare_sometimes_often() -> list:
    """Stress uchun tipik javob variantlari (0..3)."""
    return [
        {"text": "Hech qachon", "score": 0},
        {"text": "Kamdan-kam", "score": 1},
        {"text": "Ba'zan", "score": 2},
        {"text": "Tez-tez", "score": 3},
    ]


def _options_over_last_2_weeks() -> list:
    """GAD-7 / PHQ-9 uchun tipik javob variantlari (0..3)."""
    return [
        {"text": "Umuman", "score": 0},
        {"text": "Bir necha kun", "score": 1},
        {"text": "Kunlarning yarmidan ko'pida", "score": 2},
        {"text": "Deyarli har kuni", "score": 3},
    ]


def _options_agreement() -> list:
    """Self-esteem uchun rozilik variantlari (0..3)."""
    return [
        {"text": "To'liq roz emasman", "score": 0},
        {"text": "Qisman roz emasman", "score": 1},
        {"text": "Rozman", "score": 2},
        {"text": "To'liq rozman", "score": 3},
    ]


TESTS = {
    # ---------------------------------------------------------------- stress
    "stress": {
        "title": "😰 Stress darajasi",
        "description": (
            "Oxirgi 1 oy davomida nechta holatda quyidagi "
            "tuyg'u va ahvollarni boshdan kechirgansiz?"
        ),
        "questions": [
            {
                "text": "Kutilmagan voqealar tufayli xafa bo'lgansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Hayotingizdagi muhim narsalarni nazorat qila "
                "olmasligingizni his qilgansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Asabiylashgan va stress ostida bo'lgansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Bir vaqtning o'zida qilishingiz kerak bo'lgan "
                "ko'p ishlarga yetisha olmasligingizni his qilgansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Hayotingizdagi asablilikni nazorat qila "
                "olmagansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Nazoratingizdan tashqari bo'lgan narsalar "
                "tufayli g'azablangansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Qiyinchiliklar to'planib, ularni yenga "
                "olmasligingizni his qilgansiz?",
                "options": _options_never_rare_sometimes_often(),
            },
            {
                "text": "Stress tufayli uyqushingiz buzilgan bo'lgan?",
                "options": _options_never_rare_sometimes_often(),
            },
        ],
        "results": [
            {
                "min": 0, "max": 8,
                "text": "Stress darajangiz past — yaxshi! "
                "Vaziyatni nazorat qila olasiz. 🟢",
            },
            {
                "min": 9, "max": 16,
                "text": "Stress darajangiz o'rtacha. Muntazam dam olish, "
                "sport va rejalar tuzish yordam beradi. 🟡",
            },
            {
                "min": 17, "max": 24,
                "text": "Stress darajangiz yuqori. Sog'ligingiz uchun "
                "g'amxo'rlik qiling va mutaxassis bilan maslahatlashing. 🔴",
            },
        ],
    },
    # --------------------------------------------------------------- anxiety
    "anxiety": {
        "title": "😟 Xavotir (anshedlik) darajasi",
        "description": (
            "Oxirgi 2 haftada nechta holatda quyidagi "
            "holatlarni boshdan kechirgansiz?"
        ),
        "questions": [
            {
                "text": "Asabiylashgan, xavotirga yoki tashvishga "
                "tushgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Xavotirlashni to'xtata olmagansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Turli narsalar haqida xavotirga tushib, "
                "bezovtalanib yurgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Asabiylashganlik tufayli dam ololmagan yoki "
                "uxlay olmagansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Asabiylashganlik tufayli o'tirish yoki "
                "harakatda bo'lish qiyin bo'lgan?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Tez-tez bezovtalanib, asabiylashib "
                "yurgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Qo'rquv yoki dahshatni his qilgandek "
                "bo'lgansiz?",
                "options": _options_over_last_2_weeks(),
            },
        ],
        "results": [
            {
                "min": 0, "max": 4,
                "text": "Xavotir darajangiz minimal — juda yaxshi! 🟢",
            },
            {
                "min": 5, "max": 9,
                "text": "Yengil xavotir. Nafas mashqlari va relaksatsiya "
                "yordam beradi. 🟡",
            },
            {
                "min": 10, "max": 14,
                "text": "O'rtacha xavotir. Mutaxassis bilan "
                "maslahatlashing foydali bo'lishi mumkin. 🟠",
            },
            {
                "min": 15, "max": 21,
                "text": "Yuqori xavotir. Iltimos, mutaxassisga "
                "murojaat qilishingizni maslahat beramiz. 🔴",
            },
        ],
    },
    # ------------------------------------------------------------ depression
    "depression": {
        "title": "😔 Depressiv belgilar",
        "description": (
            "Oxirgi 2 haftada nechta holatda quyidagi "
            "belgilarni boshdan kechirgansiz?"
        ),
        "crisis_note": (
            "🚨 Diqqat: agar o'zingizga zarar yetkazish haqida "
            "o'ylayotgan bo'lsangiz, darhol ishonchli inson yoki "
            "mutaxassisga murojaat qiling. Siz yolg'iz emassiz."
        ),
        "questions": [
            {
                "text": "Qiziqish yoki zavq olishda pasayish "
                "sezgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Tushkunlik, g'amginlik yoki umidsizlik "
                "his qilgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Uyqu muammosi (uxlay olmaslik yoki juda ko'p "
                "uxlash) bo'lgan?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Charchaganlik yoki energiya yetishmasligi "
                "his qilgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Ishtahaningiz o'zgargan (juda kam yoki "
                "juda ko'p ovqat yegan)?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "O'zingizni isbotchi yoki boshqalarga yuk "
                "bo'lgandek his qilgansiz?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Diqqatni jamlay olmaslik (kitob o'qish, "
                "televizor ko'rish kabi)?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "Juda sezilarli sekin harakatlar yoki aksincha "
                "tashvichli bezovtalanish bo'lgan?",
                "options": _options_over_last_2_weeks(),
            },
            {
                "text": "O'lish haqida yoki o'zingizga zarar yetkazish "
                "haqida fikrlar kelgan?",
                "options": _options_over_last_2_weeks(),
            },
        ],
        "results": [
            {
                "min": 0, "max": 4,
                "text": "Depressiv belgilar minimal. 🟢",
            },
            {
                "min": 5, "max": 9,
                "text": "Yengil belgilar. Dam oling va "
                "qo'llab-quvvatlovchi muhit yarating. 🟡",
            },
            {
                "min": 10, "max": 14,
                "text": "O'rtacha belgilar. Mutaxassis bilan "
                "maslahatlashing tavsiya etiladi. 🟠",
            },
            {
                "min": 15, "max": 27,
                "text": "Jiddiy belgilar. Iltimos, mutaxassisga "
                "(shifokor yoki psixolog) murojaat qiling. 🔴",
            },
        ],
    },
    # ----------------------------------------------------------- self-esteem
    "self_esteem": {
        "title": "💪 O'z-o'zini baholash (self-esteem)",
        "description": (
            "Quyidagi bayonotlarga qanchalik roz ekanligingizni "
            "belgilang. O'zingiz uchun halol javob bering."
        ),
        "questions": [
            {
                "text": "Men o'zim bilan faxrlanaman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men o'zimni qadrlayman.",
                "options": _options_agreement(),
            },
            {
                "text": "Menda ko'p ijobiy fazilatlar bor.",
                "options": _options_agreement(),
            },
            {
                "text": "Men ko'pchilik kishilardek qobiliyatliman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men o'zimni yaxshi xulqli inson deb "
                "bilaman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men yangi narsalarni o'rganishga qodirman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men muammolarni hal qila olaman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men o'z ko'rinishimdan mamnunman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men o'z qarorlarimga ishonaman.",
                "options": _options_agreement(),
            },
            {
                "text": "Men o'z kuchim va qobiliyatlarimdan "
                "mamnunman.",
                "options": _options_agreement(),
            },
        ],
        "results": [
            {
                "min": 0, "max": 12,
                "text": "Past o'z-o'zini baholash. O'zingiz haqingizda "
                "ijobiyroq fikr yurish va o'zingizni qadrlash ustida "
                "ishlash foydali. 🟠",
            },
            {
                "min": 13, "max": 22,
                "text": "O'rtacha o'z-o'zini baholash. Kuchli "
                "tomonlaringizga e'tibor qarating. 🟡",
            },
            {
                "min": 23, "max": 30,
                "text": "Yuqori o'z-o'zini baholash — yaxshi! "
                "O'zingizga ishonchingiz komil. 🟢",
            },
        ],
    },
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
                "text": "Iш kuni uchun belgilangan ish soatidan "
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

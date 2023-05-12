from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbekcha"),
            KeyboardButton("🇷🇺 Ruscha"),
            KeyboardButton("🇬🇧 Inglizcha")
            
            ],
    ],
    resize_keyboard=True
)

raqam = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Telefon raqamni yuboring...", request_contact=True)
            ],
    ],
    resize_keyboard=True
)

joylashuv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Joylashuvni yuboring ...", request_location=True)
            ],
    ],
    resize_keyboard=True
)

pastki_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Buyurtma berish")
        ],
        [
            KeyboardButton("Sozlamalar"),
            KeyboardButton("Biz bilan aloqa")
        ],
    ],
    resize_keyboard=True
)

#bosh menu

bosh_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Lavash", callback_data="lavash"),
            InlineKeyboardButton(text = "Xod-Dog", callback_data="xot-dog")
        ],
        [
            InlineKeyboardButton(text="Sendvich club", callback_data="sendvich"),
            InlineKeyboardButton(text="Shaurma", callback_data="shaurma")
        ],
        [
            InlineKeyboardButton(text="Burger", callback_data="burger"),
            InlineKeyboardButton(text="Donar", callback_data="donar")
        ],
        [
            InlineKeyboardButton(text="Gazaklar",callback_data="gazaklar"),
            InlineKeyboardButton(text="Ichimliklar",callback_data="ichimliklar")
        ],
        [
            InlineKeyboardButton(text="Desertlar",callback_data="desertlar"),
            InlineKeyboardButton(text="Pizza",callback_data="pitsa")
        ]
    ]
)

lavash_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mol Go'shtli ", callback_data="mol goshtli"),
            InlineKeyboardButton(text = "Qalampir mol go'sht 🥩🌶", callback_data="qalampir mol_goshtli")
        ],
        [
            InlineKeyboardButton(text="Tovuq Go'shtlik 🍗", callback_data="tovuq goshtli"),
            InlineKeyboardButton(text="Qalampirli tovuq go'sht 🍗🌶", callback_data="qalampir tovuq goshtli")
        ],
        [
            InlineKeyboardButton(text="Pishloqli tovuq Go'shti 🍗🧀", callback_data="pishloqli tovuq goshti"),
            InlineKeyboardButton(text="Pishloqli mol go'shti 🥩🧀", callback_data="tovuq_goshtli")
        ],
        [
            InlineKeyboardButton(text="Fitter 🥬", callback_data="fitter")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back1")
        ]
    ]
)

xod_dog_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Hod-Dog Baget Dabl 👍", callback_data="baget dabl"),
            InlineKeyboardButton(text = "Classic Hot-Dog 👍", callback_data="classic_hotdog")
        ],
        [
            InlineKeyboardButton(text="Korolevskiy 👍", callback_data="korolevskiy"),
            InlineKeyboardButton(text="Tovuqli Hot-Dog 👍", callback_data="Tovuqli hotdog")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_2")
        ]
    ]
)


sendvich_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Classic Sendvich Club 👍", callback_data="classic sendvich")
            # InlineKeyboardButton(text = "Tovuqli Sendvich 👍", callback_data="tovuqli sendvich")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_3")
        ]
    ]
)




shaurma_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mol Go'shtli Shaurma 👍", callback_data="mol go'shtli shaurma"),
            InlineKeyboardButton(text = "Tovuq Shaurma 👍", callback_data="tovuq shaurma")
        ],
        [
        InlineKeyboardButton(text = "Mol Go'sht Shaurma+qalampir 👍", callback_data="mol go'shtli shaurma+qalampir"),
        InlineKeyboardButton(text = "Tovuq Shaurma+qalampir 👍", callback_data="tovuq shaurma+qalampir")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_4")
        ]
    ]
)


burger_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Gamburger 👍", callback_data="gamburger"),
            InlineKeyboardButton(text = "Chizburger 👍", callback_data="chizburger")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_5")
        ]
    ]
)

donar_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Tovuqli 👍", callback_data="tovuqli donar"),
            InlineKeyboardButton(text = "Go'shtli 👍", callback_data="goshtli donar")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_6")
        ]
    ]
)

gazaklar_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "15 gram Fri 👍", callback_data="fri"),
            InlineKeyboardButton(text = "Kartoshka Derevenskiy 👍", callback_data="derevenskiy_k")
        ],
        [
            InlineKeyboardButton(text = "Guruch Katta 👍", callback_data="guruch katta"),
            InlineKeyboardButton(text = "Guruch kichik 👍", callback_data="guruch kichik")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_7")
        ]
    ]
)

ichimlik_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Choy va kofe 👍", callback_data="choy_kofe"),
            InlineKeyboardButton(text = "Yaxna ichimliklar 👍", callback_data="yaxna ichimlik")
        ],
        [
            InlineKeyboardButton(text = "Fresh va tabiiy soklar 👍", callback_data="fresh_sok")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_8")
        ]
    ]
)

desert_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Assalim 👍", callback_data="medovik"),
            InlineKeyboardButton(text = "Qulupnay 👍", callback_data="qulupnay")
        ],
        [
            InlineKeyboardButton(text = "Choko 👍", callback_data="choko")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_9")
        ]
    ]
)


pitsa_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Peperoni 👍", callback_data="peperoni"),
            InlineKeyboardButton(text = "Ananaslik 👍", callback_data="ananaslik")
        ],
        [
            InlineKeyboardButton(text = "Margaritta 👍", callback_data="margaritta")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_10")
        ]
    ]
)


size_lavashmol_gosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_molgosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_mol")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back2")
        ]
    ]
)

size_goshqalapmr_gosh_lavash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_qalamprgosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_qalamprgosh")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back3")
        ]
    ]
)

size_tovuq_gosh_lavash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_tovuqgosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_tovuqgosh")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back9")
        ]
    ]
)

size_tovuqqalapmr_gosh_lavash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_qalamprtovuqgosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_qalamprtovuqgosh")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back12")
        ]
    ]
)

size_pishloqtovuq_gosh_lavash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_pishloqtovuqgosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_pishloqtovuqgosh")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back15")
        ]
    ]
)

size_pishloqmol_gosh_lavash = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_pishloqmol_gosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_pishloqmol_gosh")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back18")
        ]
    ]
)



#miqdorlar lavash

miqdor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga")
        ]
    ]
)







miqdor_mini_lavash_molgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back4")
        ]
    ]
)



miqdor_classic_lavash_molgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back5")
        ]
    ]
)



miqdor_mini_lavash_qalampir_molgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back7")
        ]
    ]
)

miqdor_classic_lavash_qalampir_molgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga2")
        ]
    ]
)



miqdor_mini_lavash_tovuqgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back10")
        ]
    ]
)


miqdor_classic_lavash_tovuqgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back11")
        ]
    ]
)

miqdor_mini_lavash_tovuq_qalampirgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back13")
        ]
    ]
)

miqdor_classic_lavash_tovuq_qalampirgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back14")
        ]
    ]
)


miqdor_mini_lavash_tovuq_pishloqgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back16")
        ]
    ]
)


miqdor_classic_lavash_tovuq_pishloqgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back17")
        ]
    ]
)


miqdor_mini_lavash_molgosh_pishloq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back19")
        ]
    ]
)


miqdor_classic_lavash_molgosh_pishloq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back20")
        ]
    ]
)

miqdor_lavash_fitter = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back21")
        ]
    ]
)

###############
# miqdorlar hot-dog


miqdor_hotdog_bagetdabl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back22")
        ]
    ]
)


miqdor_hotdog_classic = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back23")
        ]
    ]
)


miqdor_hotdog_korolevskiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back24")
        ]
    ]
)


miqdor_hotdog_tovuqli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back25")
        ]
    ]
)


########
#senvich miqdor

miqdor_sendvich_classic = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back26")
        ]
    ]
)

miqdor_sendvich_tovuqli = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back27")
        ]
    ]
)


###########
#shaurma miqdor




miqdor_mini_shaurma_molgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back29")
        ]
    ]
)

miqdor_classic_shaurma_molgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back30")
        ]
    ]
)

miqdor_mini_shaurma_tovuqgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back32")
        ]
    ]
)

miqdor_classic_shaurma_tovuqgosh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back33")
        ]
    ]
)

miqdor_mini_shaurma_tovuqgosh_qalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back35")
        ]
    ]
)

miqdor_classic_shaurma_tovuqgosh_qalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back36")
        ]
    ]
)

miqdor_mini_shaurma_molgosh_qalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back38")
        ]
    ]
)

miqdor_classic_shaurma_molgosh_qalampir = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back39")
        ]
    ]
)

#############
#burger miqdor

miqdor_gamburger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back40")
        ]
    ]
)


miqdor_chizburger = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back41")
        ]
    ]
)

##########
# donar miqdor

miqdor_tovuqli_donar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back42")
        ]
    ]
)


miqdor_goshtli_donar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back43")
        ]
    ]
)


#######
# gazaklar miqdor 

miqdor_fri = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back44")
        ]
    ]
)

miqdor_derevenskiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back45")
        ]
    ]
)

miqdor_guruch_big = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back46")
        ]
    ]
)

miqdor_gurush_small = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back47")
        ]
    ]
)


#########
# ichimliklar miqdor

miqdor_americano = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back48")
        ]
    ]
)

miqdor_coppucino = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back49")
        ]
    ]
)

miqdor_cofe3v1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back50")
        ]
    ]
)


miqdor_latte = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back51")
        ]
    ]
)

miqdor_fanta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back52")
        ]
    ]
)

miqdor_sprite = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back53")
        ]
    ]
)

miqdor_coca_cola = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back54")
        ]
    ]
)

miqdor_nestle = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back55")
        ]
    ]
)


miqdor_bliss = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back56")
        ]
    ]
)

miqdor_fresh_olma_sabzi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back57")
        ]
    ]
)

########
#desertlar miqdor

miqdor_medovik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back58")
        ]
    ]
)

miqdor_qulupnay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back59")
        ]
    ]
)

miqdor_choko = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back60")
        ]
    ]
)


########
#pitsa miqdor


miqdor_pepperoni = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back61")
        ]
    ]
)

miqdor_ananas_pitsa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back62")
        ]
    ]
)

miqdor_margaritta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = " 1️⃣", callback_data="1"),
            InlineKeyboardButton(text = " 2️⃣", callback_data="2"),
            InlineKeyboardButton(text = " 3️⃣", callback_data="3")
        ],
        [
            InlineKeyboardButton(text = " 4️⃣", callback_data="4"),
            InlineKeyboardButton(text = " 5️⃣", callback_data="5"),
            InlineKeyboardButton(text = " 6️⃣", callback_data="6")
        ],
        [
            InlineKeyboardButton(text = " 7️⃣", callback_data="7"),
            InlineKeyboardButton(text = " 8️⃣", callback_data="8"),
            InlineKeyboardButton(text = " 9️⃣", callback_data="9")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back63")
        ]
    ]
)


#########




shaurma_molgosh_size = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_molgosh_shaurma"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_molgosh_shaurma")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back28")
        ]
    ]
)

shaurma_tovuqgosh_size = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_shaurma_tovuqgosh"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_shaurma_tovuqmolgosh")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back31")
        ]
    ]
)

shaurma_qalampir_molgosh_size = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_shaurma_molgosh+qalampir"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_shaurma_molgosh+qalampir")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back34")
        ]
    ]
)

shaurma_qalampir_tovuqgosh_size = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Mini 👍", callback_data="mini_shaurma_tovuqgosh+qalampir"),
            InlineKeyboardButton(text = "Classic 👍", callback_data="classic_shaurma_tovuqgosh+qalampir")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back37")
        ]
    ]
)

#ichimliklar

kofelar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Americano 👍", callback_data="americano"),
            InlineKeyboardButton(text = "Cappuccino 👍", callback_data="cappuccino")
        ],
        [
            InlineKeyboardButton(text = "Cofe 3v1 👍", callback_data="cofe3v1"),
            InlineKeyboardButton(text = "Latte 👍", callback_data="latte")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_cofelar")
        ]
    ]
)


yaxna_ichimlik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Fanta 👍", callback_data="fanta"),
            InlineKeyboardButton(text = "Sprite 👍", callback_data="sprite")
        ],
        [
            InlineKeyboardButton(text = "Coca cola 👍", callback_data="coca_cola"),
            InlineKeyboardButton(text = "Nestle 👍", callback_data="nestle")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_yaxna_ichimliklar")
        ] 
    ]
)


fresh_sok = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Bliss sok 1l 👍", callback_data="bliss"),
            InlineKeyboardButton(text = "Olma va sabzi fresh 👍", callback_data="fresh_o_s")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="ortga_fresh_sok")
        ]
    ]
)
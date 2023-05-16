

from buttons import *
from config import API_TOKEN
import logging

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6226627715:AAFOiN1uWnCXcQHl_aOVOp9tW-mBCoeGaAU'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Tilni tanlang!", reply_markup=til)



@dp.message_handler(text="🇺🇿 O'zbekcha")
async def echo(message: types.Message):

    await message.answer("Telefon raqamingizni yuboring...", reply_markup=raqam)

@dp.message_handler(content_types="contact")
async def echo(message: types.Message):

    await message.answer("📍 Joylashuvni yuboring...", reply_markup=joylashuv)

@dp.message_handler(content_types="location")
async def echo(message: types.Message):

    await message.answer("Siz ro'yxatdan o'tdingiz\n\nKategorilardan birini tanlang!",reply_markup=pastki_menyu)

@dp.message_handler(text="Buyurtma berish")
async def echo(message: types.Message):

    await message.answer("✅ Marhamat menu: ", reply_markup=bosh_menyu)

#mahsulotlar

@dp.callback_query_handler(text="lavash")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_menyu.jpg", "rb"),
        caption="✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

@dp.callback_query_handler(text="xot-dog")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat Xod-Doglar menusi!!!", reply_markup=xod_dog_menyu)

@dp.callback_query_handler(text="sendvich")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat Sendvichlar menusi!!!", reply_markup= sendvich_menyu)

@dp.callback_query_handler(text="shaurma")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/shaurma_menyu.jpg", "rb"),
        caption="✅ Marhamat shaurmalar menusi!!!", reply_markup= shaurma_menyu)



@dp.callback_query_handler(text="burger")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat burgerlar menusi!!!",reply_markup= burger_menyu)


@dp.callback_query_handler(text="donar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat donarlar menusi!!!", reply_markup=donar_menyu)



@dp.callback_query_handler(text="gazaklar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat gazaklar menusi!!!", reply_markup= gazaklar_menyu)



@dp.callback_query_handler(text="ichimliklar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat ichimliklar menusi!!!", reply_markup= ichimlik_menyu)


@dp.callback_query_handler(text="desertlar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/desert_menyu.jpg", "rb"),
        caption="✅ Marhamat desertlar menusi!!!", reply_markup= desert_menyu)

@dp.callback_query_handler(text="pitsa")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat pitsalar menusi!!!", reply_markup= pitsa_menyu)

#lavash_turlari

@dp.callback_query_handler(text="mol goshtli")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_lavashmol_gosh)

@dp.callback_query_handler(text="qalampir mol_goshtli")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_goshqalapmr_gosh_lavash)

@dp.callback_query_handler(text="tovuq goshtli")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_tovuq_gosh_lavash)

@dp.callback_query_handler(text="qalampir tovuq goshtli")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_tovuqqalapmr_gosh_lavash)

@dp.callback_query_handler(text="pishloqli tovuq goshti")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= 
size_pishloqtovuq_gosh_lavash)

@dp.callback_query_handler(text="tovuq_goshtli")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_pishloqmol_gosh_lavash)

@dp.callback_query_handler(text="fitter")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fitter_lav.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht, qarsildoq muztog' salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_lavash_fitter)


#miqdor lavash

@dp.callback_query_handler(text="mini_molgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_mol_gosh_mini.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_molgosh)


@dp.callback_query_handler(text="classic_mol")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_mol_gosh_mini.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_classic_lavash_molgosh)

@dp.callback_query_handler(text="mini_qalamprgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_molgosh_qalampir.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi::Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_qalampir_molgosh)

@dp.callback_query_handler(text="classic_qalamprgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_molgosh_qalampir.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm 
Tarkibi::Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_qalampir_molgosh)

@dp.callback_query_handler(text="mini_tovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuq_lav.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_tovuqgosh)

@dp.callback_query_handler(text="classic_tovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuq_lav.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_classic_lavash_tovuqgosh)

@dp.callback_query_handler(text="mini_qalamprtovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuq_qalampir_lav.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_tovuq_qalampirgosh)

@dp.callback_query_handler(text="classic_qalamprtovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuq_qalampir_lav.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_classic_lavash_tovuq_qalampirgosh)

@dp.callback_query_handler(text="mini_pishloqtovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pishloq_tovuqgosh_lav.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_tovuq_pishloqgosh)


@dp.callback_query_handler(text="classic_pishloqtovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pishloq_tovuqgosh_lav.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_classic_lavash_tovuq_pishloqgosh)

@dp.callback_query_handler(text="mini_pishloqmol_gosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pishloq_molgosh_lav.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_mini_lavash_molgosh_pishloq)

@dp.callback_query_handler(text="classic_pishloqmol_gosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pishloq_molgosh_lav.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm 
Tarkibi:Xamir,garimdori,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang""", reply_markup= miqdor_classic_lavash_molgosh_pishloq)

#xod-dog

@dp.callback_query_handler(text="baget dabl")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/bagetdabl_hd.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm 
Tarkibi:✅ Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup= miqdor_hotdog_bagetdabl)

@dp.callback_query_handler(text="classic_hotdog")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/classic_hd.jpg", "rb"),
        caption="""
Narxi:8000 ming so'm 
Tarkibi:✅ Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup= miqdor_hotdog_classic)

@dp.callback_query_handler(text="korolevskiy")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/korolevskiy_hd.jpg", "rb"),
        caption="""
Narxi:15000 ming so'm
Tarkibi:✅ Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup= miqdor_hotdog_korolevskiy)

@dp.callback_query_handler(text="Tovuqli hotdog")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuqli_hd.jpg", "rb"),
        caption="""
Narxi:17000 ming so'm
Tarkibi:✅ Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang""", reply_markup= miqdor_hotdog_tovuqli)

#sendvich

@dp.callback_query_handler(text="classic sendvich")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/classic_club_sen.jpg", "rb"),
        caption="""
Narxi:22000 ming so'm
Tarkibi:✅ Kulcha, tovuq go'shti, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_sendvich_classic)

# @dp.callback_query_handler(text="tovuqli sendvich")
# async def my_func(call: types.CallbackQuery):
#     await call.message.answer_photo(
#         photo=open("images/tovuqli_sen.jpg", "rb"),
#         caption="""
# Narxi:22000 ming so'm
# Tarkibi:✅ Kulcha, tovuq go'shti, pomidor, sous,  piyoz
# Miqdorini tanlang""", reply_markup= miqdor_sendvich_tovuqli)

#shaurma

@dp.callback_query_handler(text="mol go'shtli shaurma")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_molgosh_size)

@dp.callback_query_handler(text="mini_molgosh_shaurma")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/molgosh_shaur.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz.
Miqdorini tanlang""", reply_markup= miqdor_mini_shaurma_molgosh)

@dp.callback_query_handler(text="classic_molgosh_shaurma")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/molgosh_shaur.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz.
Miqdorini tanlang""", reply_markup= miqdor_classic_shaurma_molgosh)
    

@dp.callback_query_handler(text="tovuq shaurma")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_tovuqgosh_size)

@dp.callback_query_handler(text="mini_shaurma_tovuqgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuqgosh_shaur.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_mini_shaurma_tovuqgosh)
    

@dp.callback_query_handler(text="classic_shaurma_tovuqmolgosh")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuqgosh_shaur.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_classic_shaurma_tovuqgosh)

@dp.callback_query_handler(text="mol go'shtli shaurma+qalampir")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_qalampir_molgosh_size)

@dp.callback_query_handler(text="mini_shaurma_molgosh+qalampir")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/molgosh_qalampr_shaur.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_mini_shaurma_molgosh_qalampir)
    

@dp.callback_query_handler(text="classic_shaurma_molgosh+qalampir")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/molgosh_qalampr_shaur.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_classic_shaurma_molgosh_qalampir)


@dp.callback_query_handler(text="tovuq shaurma+qalampir")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_qalampir_tovuqgosh_size)

@dp.callback_query_handler(text="mini_shaurma_tovuqgosh+qalampir")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuqgosh_qalampr_shaur.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_mini_shaurma_tovuqgosh_qalampir)
    

@dp.callback_query_handler(text="classic_shaurma_tovuqgosh+qalampir")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuqgosh_qalampr_shaur.jpg", "rb"),
        caption="""
Narxi:20000 ming so'm
Tarkibi:✅ Kulcha, go'sht, pomidor, sous,  piyoz
Miqdorini tanlang""", reply_markup= miqdor_classic_shaurma_tovuqgosh_qalampir)

#burger

@dp.callback_query_handler(text="gamburger")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/gamburger.jpg", "rb"),
        caption="""
Narxi:21000 ming so'm
Tarkibi:✅ Yumshoq kulcha, yumshoq mol go'shtidan kotlet, tuzlangan bodringlar, yangi pomidorlar, qizil piyoz va ikkita maxsus qayla bilan qarsildoq muztog' salati
Miqdorini tanlang""", reply_markup= miqdor_gamburger)

@dp.callback_query_handler(text="chizburger")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/chizburger.jpg", "rb"),
        caption="""
Narxi:23000 ming so'm
Tarkibi:✅ Yumshoq kulcha, bir bo'lak eritilgan Cheddar pishlog'i bilan mol go'shtidan yumshoq kotlet, tuzlangan bodring, yangi pomidorlar, qizil piyoz va ikkita maxsus qayla bilan qarsildoq muztog' salati
Miqdorini tanlang""", reply_markup= miqdor_chizburger)

#donar

@dp.callback_query_handler(text="tovuqli donar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuqli_donar.jpg", "rb"),
        caption="""
Narxi:39000 ming so'm
Tarkibi:✅ Yumshoq tovuq go'shti, qovurilgan kartoshka, guruch va sabzavotli salatdan iborat to'yimli to'plam. Bizning pomidordan tayyorlangan maxsus qaylamiz bilan birga tortiladi
Miqdorini tanlang""", reply_markup= miqdor_tovuqli_donar)

@dp.callback_query_handler(text="goshtli donar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/goshtli_donar.jpg", "rb"),
        caption="""
Narxi:41000 ming so'm.
Tarkibi:✅ Yumshoq mol go'shti, qovurilgan kartoshka, guruch va sabzavot salatidan iborat to'yimli to'plam. Bizning pomidordan tayyorlangan maxsus qaylamiz bilan birga tortiladi
Miqdorini tanlang""", reply_markup= miqdor_goshtli_donar)

#gazaklar

@dp.callback_query_handler(text="fri")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fri.jpg", "rb"),
        caption="""
Narxi:13000 ming so'm
Miqdorini tanlang""", reply_markup= miqdor_fri)

@dp.callback_query_handler(text="derevenskiy_k")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/derevenskiy.jpg", "rb"),
        caption="""
Narxi:13000 ming so'm.
Qizdirilgan yogida qovurib olingan yupqa va qarsildoq kartoshka pallachalari.
Miqdorini tanlang""", reply_markup= miqdor_derevenskiy)

@dp.callback_query_handler(text="guruch katta")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/guruch_katta_kichik.jpg", "rb"),
        caption="""
Narxi:9000 ming so'm.
Qaynatilgan guruch.
Miqdorini tanlang""", reply_markup= miqdor_guruch_big)

@dp.callback_query_handler(text="guruch kichik")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/guruch_katta_kichik.jpg", "rb"),
        caption="""
Narxi:6000 ming so'm.
Qaynatilgan guruch.
Miqdorini tanlang""", reply_markup= miqdor_gurush_small)

#ichimliklar

@dp.callback_query_handler(text="choy_kofe")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= kofelar)


@dp.callback_query_handler(text="americano")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/americano.jpg", "rb"),
        caption="""
Narxi:12000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_americano)

@dp.callback_query_handler(text="cappuccino")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cappucino.jpg", "rb"),
        caption="""
Narxi:18000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_coppucino)
    

@dp.callback_query_handler(text="cofe3v1")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cofe3v1.jpg", "rb"),
        caption="""
Narxi:3000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_cofe3v1)

@dp.callback_query_handler(text="latte")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/latte.jpg", "rb"),
        caption="""
Narxi:15000 ming so'm.
✅ Latte big 120g ☕️
Miqdorini tanlang""", reply_markup= miqdor_latte)
    

@dp.callback_query_handler(text="yaxna ichimlik")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= yaxna_ichimlik)
    
@dp.callback_query_handler(text="fanta")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fanta.jpg", "rb"),
        caption="""
Narxi:11000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_fanta)

@dp.callback_query_handler(text="sprite")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/sprite.jpg", "rb"),
        caption="""
Narxi:11000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_sprite)

@dp.callback_query_handler(text="coca_cola")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cola.jpg", "rb"),
        caption="""
Narxi:11000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_coca_cola)

@dp.callback_query_handler(text="nestle")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/nestle.jpg", "rb"),
        caption="""
Narxi:4000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_nestle)

@dp.callback_query_handler(text="fresh_sok")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= fresh_sok)


@dp.callback_query_handler(text="bliss")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/bliss.jpg", "rb"),
        caption="""
Narxi:10000 ming so'm.
Miqdorini tanlang""", reply_markup= miqdor_bliss)
    

@dp.callback_query_handler(text="fresh_o_s")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fresh.jpg", "rb"),
        caption="""
Narxi:13000 ming so'm.
✅ Fresh Sabzi + olma
Miqdorini tanlang""", reply_markup= miqdor_fresh_olma_sabzi)

#desertlar

@dp.callback_query_handler(text="medovik")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/asalim.jpg", "rb"),
        caption="""
Narxi:14000 ming so'm.
✅ An'naviy ta'm - asal asosidagi biskvit va krem
Miqdorini tanlang""", reply_markup= miqdor_medovik)

@dp.callback_query_handler(text="qulupnay")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/qulupnaymuss.jpg", "rb"),
        caption="""
Narxi:14000 ming so'm.
✅ Qulupnayli Muss.
Miqdorini tanlang""", reply_markup= miqdor_qulupnay)

@dp.callback_query_handler(text="choko")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/choko.jpg", "rb"),
        caption="""
Narxi:14000 ming so'm.
✅ An'naviy ta'm - shokolat asosidagi biskvit va krem.
Miqdorini tanlang""", reply_markup= miqdor_choko)

#pizza

@dp.callback_query_handler(text="peperoni")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/peperoni.jpg", "rb"),
        caption="""
Narxi: 65000 ming so'm.
✅ Pitsa Pepperoni
Pitsa Pepperoni 33sm.
Sous tomat pitsa uchun
Yupqa xamir
pishloq 110 gr.
Miqdorini tanlang""", reply_markup= miqdor_pepperoni)

@dp.callback_query_handler(text="ananaslik")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/ananaslipitsa.jpg", "rb"),
        caption="""
Narxi: 65000 ming so'm.
✅ Ananasli Pitsa
Pitsa Kolbasali 33sm.
Sous tomatli pitsa uchun
3xil kolbasa 130gr.
Yupqa xamir
joxori
Pishloq 100gr
Miqdorini tanlang""", reply_markup= miqdor_ananas_pitsa)

@dp.callback_query_handler(text="margaritta")
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/margaritta.jpg", "rb"),
        caption="""
Narxi: 65000 ming so'm.
✅ Margaritta Pitsa
Pitsa Margaritta 33sm.
Sous tomatli pitsa uchun
Yupqa xamir
Pomidorlar
Pishloq 100gr
Miqdorini tanlang""", reply_markup= miqdor_margaritta)


########### ###########
#bosh_menu back1

@dp.callback_query_handler(text="back1")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu!!!", reply_markup= bosh_menyu)

# # lavash menu back2

# @dp.callback_query_handler(text="back2")
# async def my_func(call: types.CallbackQuery):
#     await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)
    
# mol gosht size back3

@dp.callback_query_handler(text="back3")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# mol gosht size mini back4

@dp.callback_query_handler(text="back4")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_lavashmol_gosh)

# mol gosht size classic back5

@dp.callback_query_handler(text="back5")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_lavashmol_gosh)

# lavash qalampir mol gosh back6

@dp.callback_query_handler(text="back6")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# lavash qalampir mol gosh size mini back_q_mg

@dp.callback_query_handler(text="back_q_mg")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_goshqalapmr_gosh_lavash)

# lavash qalampir mol gosh size classic backq_mg_c

@dp.callback_query_handler(text="backq_mg_c")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_goshqalapmr_gosh_lavash)

# lavash tovuq gosh back9

@dp.callback_query_handler(text="back9")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# lavash tovuq gosh size mini back10

@dp.callback_query_handler(text="back10")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_tovuq_gosh_lavash)

# lavash tovuq gosh size classic back11

@dp.callback_query_handler(text="back11")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_tovuq_gosh_lavash)

# lavash tovuq qalampir gosh back12

@dp.callback_query_handler(text="back12")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# lavash tovuq qalampir gosh size mini back13

@dp.callback_query_handler(text="back13")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_tovuqqalapmr_gosh_lavash)

# lavash tovuq qalampir gosh size classic back14


@dp.callback_query_handler(text="back14")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_tovuqqalapmr_gosh_lavash)

# lavash pishloq tovuq gosh back15

@dp.callback_query_handler(text="back15")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# lavash pishloq tovuq gosh size mini back16

@dp.callback_query_handler(text="back16")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_pishloqtovuq_gosh_lavash)

# lavash pishloq tovuq gosh size classic back17

@dp.callback_query_handler(text="back17")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_pishloqtovuq_gosh_lavash)

# lavash pishloq mol gosh back18

@dp.callback_query_handler(text="back18")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# lavash pishloq mol gosh size mini back19

@dp.callback_query_handler(text="back19")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_pishloqmol_gosh_lavash)

# lavash pishloq mol gosh size classic back20

@dp.callback_query_handler(text="back20")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= size_pishloqmol_gosh_lavash)

# lavash pishloq mol gosh back21

@dp.callback_query_handler(text="back21")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat lavashlar menusi!!!", reply_markup= lavash_menyu)

# bosh_menu xoddog ortga_2

@dp.callback_query_handler(text="ortga_2")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)


# xod-dog baget dabl back22

@dp.callback_query_handler(text="back22")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= xod_dog_menyu)

# xod-dog classic_hotdog back23

@dp.callback_query_handler(text="back23")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat Xod-Doglar menusi!!!", reply_markup= xod_dog_menyu)


# xod-dog korolevskiy back24

@dp.callback_query_handler(text="back24")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat Xod-Doglar menusi!!!", reply_markup= xod_dog_menyu)

# xod-dog korolevskiy back25

@dp.callback_query_handler(text="back25")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marxamat Xod-Doglar menusi!!!", reply_markup= xod_dog_menyu)

# bosh_menu sendvich ortga_3

@dp.callback_query_handler(text="ortga_3")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)

# sendvich classic back26

@dp.callback_query_handler(text="back26")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= sendvich_menyu)

# sendvich tovuqli back27

@dp.callback_query_handler(text="back27")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= sendvich_menyu)




# bosh_menu shaurma ortga_4

@dp.callback_query_handler(text="ortga_4")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)


# shaurma mol gosh back28

@dp.callback_query_handler(text="back28")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat shaurmalar menusi!!!", reply_markup= shaurma_menyu)

# shaurma mol gosh size mini back29

@dp.callback_query_handler(text="back29")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_molgosh_size)

# shaurma mol gosh size classic back30

@dp.callback_query_handler(text="back30")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_molgosh_size)

# shaurma tovuq gosh back31

@dp.callback_query_handler(text="back31")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat shaurmalar menusi!!!", reply_markup= shaurma_menyu)

# shaurma tovuq gosh size mini back32

@dp.callback_query_handler(text="back32")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_tovuqgosh_size)

# shaurma tovuq gosh size classic back33

@dp.callback_query_handler(text="back33")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_tovuqgosh_size)

# shaurma mol gosh+qalampir back34

@dp.callback_query_handler(text="back34")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat shaurmalar menusi!!!", reply_markup= shaurma_menyu)

# shaurma mol gosh+qalampir size mini back35

@dp.callback_query_handler(text="back35")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_qalampir_molgosh_size)

# shaurma mol gosh+qalampir size classic back36

@dp.callback_query_handler(text="back36")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_qalampir_molgosh_size)

# shaurma tovuq gosh+qalampir back37

@dp.callback_query_handler(text="back37")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat shaurmalar menusi!!!", reply_markup= shaurma_menyu)

# shaurma tovuq gosh+qalampi size mini back38

@dp.callback_query_handler(text="back38")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_qalampir_tovuqgosh_size)

# shaurma tovuq gosh+qalampi size classic back39

@dp.callback_query_handler(text="back39")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= shaurma_qalampir_tovuqgosh_size)


# bosh menu (burger) ortga_5

@dp.callback_query_handler(text="ortga_5")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)


# burger gamburger back40

@dp.callback_query_handler(text="back40")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat burgerlar menusi!!!", reply_markup= burger_menyu)

# burger chizburger back41

@dp.callback_query_handler(text="back41")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat burgerlar menusi!!!", reply_markup= burger_menyu)


# bosh menu donar ortga_6

@dp.callback_query_handler(text="ortga_6")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)

# donar tovuqli back42

@dp.callback_query_handler(text="back42")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat donarlar menusi!!!", reply_markup= donar_menyu)

# donar goshtli back43

@dp.callback_query_handler(text="back43")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat donarlar menusi!!!", reply_markup= donar_menyu)


# bosh menu gazaklar ortga_7

@dp.callback_query_handler(text="ortga_7")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)

# gazaklar fri back44

@dp.callback_query_handler(text="back44")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat gazaklar menusi!!!", reply_markup= gazaklar_menyu)

# gazaklar derevenskiy kartoshka back45

@dp.callback_query_handler(text="back45")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat gazaklar menusi!!!", reply_markup= gazaklar_menyu)

# gazaklar gurush katta back46

@dp.callback_query_handler(text="back46")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat gazaklar menusi!!!", reply_markup= gazaklar_menyu)

# gazaklar gurush kichkina back47

@dp.callback_query_handler(text="back47")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat gazaklar menusi!!!", reply_markup= gazaklar_menyu)


# bosh menu ichimliklar ortga_8

@dp.callback_query_handler(text="ortga_8")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu:", reply_markup= bosh_menyu)

#ichimliklar choy va foke ortga_cofelar

@dp.callback_query_handler(text="ortga_cofelar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat ichimliklar menusi!!!", reply_markup= ichimlik_menyu)

#ichimliklar choy va foke ortga_yaxna_ichimliklar

@dp.callback_query_handler(text="ortga_yaxna_ichimliklar")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marxamat ichimliklar menusi!!!", reply_markup= ichimlik_menyu)

#ichimliklar choy va foke ortga_fresh_sok

@dp.callback_query_handler(text="ortga_fresh_sok")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat ichimliklar menusi!!!", reply_markup= ichimlik_menyu)

# ichimliklar choy va kofe americano back48

@dp.callback_query_handler(text="back48")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= kofelar)

# ichimliklar choy va kofe cappucino back49

@dp.callback_query_handler(text="back49")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= kofelar)

# ichimliklar choy va kofe cofe3v1 back50

@dp.callback_query_handler(text="back50")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= kofelar)

# ichimliklar choy va kofe latte back51

@dp.callback_query_handler(text="back51")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= kofelar)


# ichimliklar yaxna ichimlik fanta back52

@dp.callback_query_handler(text="back52")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= yaxna_ichimlik)

# ichimliklar yaxna ichimlik sprite back53

@dp.callback_query_handler(text="back53")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= yaxna_ichimlik)

# ichimliklar yaxna ichimlik coca cola back54

@dp.callback_query_handler(text="back54")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= yaxna_ichimlik)

# ichimliklar yaxna ichimlik nestle back55

@dp.callback_query_handler(text="back55")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= yaxna_ichimlik)


# ichimliklar fresh sok bliss1l back56

@dp.callback_query_handler(text="back56")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= fresh_sok)

# ichimliklar fresh sok olma_sabzi fresh back57

@dp.callback_query_handler(text="back57")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Kategoriyalardan birini tanlang!!!", reply_markup= fresh_sok)


# bosh menu desert

@dp.callback_query_handler(text="ortga_9")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat menu", reply_markup= bosh_menyu)

# desertlar medovik back58

@dp.callback_query_handler(text="back58")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat desertlar menusi!!!", reply_markup= desert_menyu)

# desertlar qulupnay back59

@dp.callback_query_handler(text="back59")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat desertlar menusi!!!", reply_markup= desert_menyu)

# desertlar choko back60

@dp.callback_query_handler(text="back60")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat desertlar menusi!!!", reply_markup= desert_menyu)


# bosh menu pitsalar

@dp.callback_query_handler(text="ortga_10")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat  menu", reply_markup= bosh_menyu)

# pitsalar pepperoni back61

@dp.callback_query_handler(text="back61")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat pitsalar menusi!!!", reply_markup= pitsa_menyu)

# pitsalar ananaslik back62

@dp.callback_query_handler(text="back62")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat pitsalar menusi!!!", reply_markup= pitsa_menyu)

# pitsalar margaritta back63

@dp.callback_query_handler(text="back63")
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅ Marhamat pitsalar menusi!!!", reply_markup= pitsa_menyu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



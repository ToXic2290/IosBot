import time
from time import sleep
import telebot
from telebot import types # для указание типов
import caption

bot = telebot.TeleBot("5400897291:AAGCWphbUiKx7r1ntjHQNfL75WaWCRk6cvA")



whatsapp = 'BQACAgIAAxkBAAIBI2KiW-yxnpb2zbjXMIvDnFgiXbF0AAIaGgAC4fsISOMCXlTV1I1kJAQ' # Да
vk = 'BQACAgIAAxkBAANCYp-mYHCEN97WIzNKS3mt1hwxaJgAAokWAAI6g8BLar1MgfTpyGckBA' # Да
inst = 'BQACAgIAAxkBAANGYp-oRy9oMeccSPnrT2s2eDqO3FsAAj4PAAKnHMFKdM6RbZm5CCIkBA' # Да
tg = 'BQACAgIAAxkBAANEYp-m4B1puElbayEIDimXbQ7F5DEAAnYWAAL1GfhIzFScEUu08-IkBA' # Да
spotify = 'BQACAgIAAxkBAANKYp-q3AGtad0CFXhr6RGEKvyWHqoAAtcTAAImGzlI5TkFAAGoZIGLJAQ' # Да
launcher = 'BQACAgIAAxkBAANIYp-pVuyMYdiokBuGhsRgmIv0l50AArAYAAI_2CBJuDsrno8T6tQkBA' # Да
tt = 'BQACAgIAAxkBAANFYp-njX1ODzAtoXOP-e8NVR9naswAAmwaAALxI9BL68qKNbjPIsAkBA' # Да
clock = 'BQACAgIAAxkBAANJYp-qLsE-uO0RnDSJNXLJHNDK9NUAAsIQAAJOfqFKOZK_7-PbScgkBA' # Да
statusbar = "BQACAgIAAxkBAANLYp-rMvPHMssxDcDMhetxJ24yXgQAAhMWAAKj7_hKjcI5Ih1QQgEkBA" # Да
appstore = "BQACAgIAAxkBAANMYp-r_ggDlWenMLol80kAAWXoOKZJAAIbFQACs5MYS4zhiTNbm2CeJAQ" # Да
camera = "BQACAgIAAxkBAAIBFmKiWT8x36HCM0VKfxprarmQt-t3AAKbEAACWMBQS9u6w1rrI2nHJAQ" #
calc = "BQACAgIAAxkBAAIBF2KiWX2hq-kCv3FTzdYqOItlBqc8AAKZEAACWMBQSxO4Z8bUrVQ5JAQ" #
gallery = "BQACAgIAAxkBAAIBGGKiWa80fR-E5rw_aViuOC74LwPMAAKUEgACGQzgSFqCSCIKi1viJAQ" #
voice = "BQACAgIAAxkBAAIBGWKiWeefty-cWuLaSpbTE_fUHN_rAAKsEAACC2NISgW6RS4nkZObJAQ" #
clnd = "BQACAgIAAxkBAAIBGmKiWjBswZUdQJZXy1nki9qeVEXRAAJ3EAACWMBQS1CMCweO3yr_JAQ" #
msg = "BQACAgIAAxkBAAIBG2KiWmCpGEKZrQR6XjxDPXxKDnYLAAJCGAACZUwhSmU5Vfo4r8BnJAQ" #
contacts = "BQACAgIAAxkBAAIBHGKiWqjDrtklS3NUgkFjEyzMNHkIAAJ0EAACWMBQS-oVQtRii4DhJAQ" #
call = "BQACAgIAAxkBAAIBHWKiWsVehg34DAh8J2X-9uUbgt_PAAKSEgACGQzgSF3rSxfM7jWYJAQ" #
music = "BQACAgIAAxkBAAIBHmKiWuj9fmGA3Jk5Lvqa_VIDFHkpAAJ1EAACWMBQS0MMzkrmzwX-JAQ" #
kb = "BQACAgIAAxkBAAIBH2KiWw_CqPeAkVABaO47gd6PjldLAAIpFAAC6UlQSQm9ntnXvwlrJAQ" #
notes = "BQACAgIAAxkBAAIBIGKiWzYkuGOggwk4q6CZA9YXFKu_AAJBFQACXd3xStgQmC0scGyBJAQ" #
notify = "BQACAgIAAxkBAAIBIWKiW2jdp7iJzj4AAY-XwFriknLXuQACKhYAAl3d8UrboeWRu3ovsiQE" #

# Данные
bio = """🙃 Мини биография обо мне:
Псевдоним, а так-же мое имя во вселенной телеграма - Токсик
Настоящее имя скрываю :(

👾 Из увлечений могу скзаать только, что увлекаюсь написанием различных скриптов, модулей для юзерботов (Хикка в основном), изучаю основы создания игр 🤭

😮‍💨 Чаще всего обитаю в чатах Хакерфона ( @HPV_HOME ), поддержки Хикки ( @hikka_talks ) или в чате своего канала ( @AstroModulesChat )

🫠 Писать мне в лс не советую, но если все же хотите что-то спросить, посоветовать или пообщаться то пишите "С бота", чтобы бот вас пропустил - @ToXicUse"""

soc = """🔍  Все соц. сети создателя бота находятся ниже 🔎
    💎 —————> https://t.me/TxSocial <—————— 💎"""

donate = """🙁 В связи с ситуацией в Украине, раздел "Донат" временно отключен. Спасибо за понимание.

#stopwar #nowar"""





@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("😈 VK 😈")
    btn2 = types.KeyboardButton("🛩 TG 🛩")
    btn3 = types.KeyboardButton("🎵 TikTok 🎵")
    btn4 = types.KeyboardButton('📷 Instagram 📷')
    btn5 = types.KeyboardButton("🏠 Launcher 🏠")
    btn6 = types.KeyboardButton("🕙 Clock 🕙")
    btn7 = types.KeyboardButton("🎶 Spotify 🎶")
    btn8 = types.KeyboardButton("😍 Status Bar 😍")
    btn9 = types.KeyboardButton("🔢 Calculator 🔢")
    btn10 = types.KeyboardButton("📷 Camera 📷")
    btn13 = types.KeyboardButton("⚒ Инфо 🛠")
    btn14 = types.KeyboardButton("🖼️ Gallery 🖼️")
    btn15 = types.KeyboardButton("🎤 Диктофон 🎤")
    btn16 = types.KeyboardButton("📆 Календарь 📆")
    btn17 = types.KeyboardButton("💭 Messages 💭")
    btn18 = types.KeyboardButton("🙍‍♂️ Контакты 🙍‍♂️")
    btn19 = types.KeyboardButton("📞 Call 📞")
    btn20 = types.KeyboardButton("🎧 Music 🎧")
    btn21 = types.KeyboardButton("⌨️ Keyboard ⌨️")
    btn22 = types.KeyboardButton("📒 Notes 📒")
    btn23 = types.KeyboardButton("📩 Notifications  📩")
    btn25 = types.KeyboardButton("❤️‍🔥 WhatsApp ❤️‍🔥")
    markup.add(btn25, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23)
    markup.add(btn13)
    bot.send_message(message.chat.id, text='''Выбери любое приложение из списка ниже'''.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❤️‍🔥 WhatsApp ❤️‍🔥"):
        bot.send_document(message.chat.id, whatsapp)     
    elif(message.text == "😈 VK 😈"):
        bot.send_document(message.chat.id, vk, caption=caption.vkd)        
    elif(message.text == '📷 Instagram 📷'):
        bot.send_document(message.chat.id, inst, caption=captiom.instd)        
    elif(message.text == "🛩 TG 🛩"):
        bot.send_document(message.chat.id, tg, caption=caption.tgd)
    elif(message.text == "🎶 Spotify 🎶"):
        bot.send_document(message.chat.id, spotify, caption=caption.spd)
    elif(message.text == "🏠 Launcher 🏠"):
        bot.send_document(message.chat.id, launcher, caption=caption.ld)
    elif(message.text == "🎵 TikTok 🎵"):
        bot.send_document(message.chat.id, tt, caption=caption.ttd)
    elif(message.text == "🕙 Clock 🕙"):
        bot.send_document(message.chat.id, clock, caption=caption.cld)
    elif(message.text == "😍 Status Bar 😍"):
        bot.send_document(message.chat.id, statusbar, caption=caption.sbd)
    elif(message.text == "📷 Camera 📷"):
        bot.send_document(message.chat.id, camera, caption=caption.cad)
    elif(message.text == "🔢 Calculator 🔢"):
        bot.send_document(message.chat.id, calc, caption=caption.calcd)
    elif(message.text == "🖼️ Gallery 🖼️"):
        bot.send_document(message.chat.id, gallery, caption=caption.gald)
    elif(message.text == "🎤 Диктофон 🎤"):
        bot.send_document(message.chat.id, voice, caption=caption.voiced)
    elif(message.text == "📆 Календарь 📆"):
        bot.send_document(message.chat.id, clnd, caption=caption.clndd)
    elif(message.text == "💭 Messages 💭"):
        bot.send_document(message.chat.id, msg, caption=caption.msgd)
    elif(message.text == "🙍‍♂️ Контакты 🙍‍♂️"):
        bot.send_document(message.chat.id, contacts, caption=caption.cntd)
    elif(message.text == "📞 Call 📞"):
        bot.send_document(message.chat.id, call, caption=caption.calld)
    elif(message.text == "🎧 Music 🎧"):
        bot.send_document(message.chat.id, music, caption=caption.msd)
    elif(message.text == "⌨️ Keyboard ⌨️"):
        bot.send_document(message.chat.id, kb, caption=caption.kbd)
    elif(message.text == "📒 Notes 📒"):
        bot.send_document(message.chat.id, notes, caption=caption.ntd)
    elif(message.text == "📩 Notifications  📩"):
        bot.send_document(message.chat.id, notify, caption=caption.ntf)






        # Доп кнопки
    elif(message.text == "⚒ Инфо 🛠"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🫠 Биография")
        btn3 = types.KeyboardButton("🔗 Социальные сети")
        btn4 = types.KeyboardButton("💸 Донат")
        back = types.KeyboardButton("⛺️ Домой")
        markup.add(btn1, btn3, btn4, back)
        bot.send_message(message.chat.id, text="😙 Тут вы можете узнать некоторую информацию о создателе", reply_markup=markup)


    elif(message.text == "🫠 Биография"):
        bot.send_message(message.chat.id, bio)
    elif message.text == "💸 Донат":
        bot.send_message(message.chat.id, donate)
    elif message.text == "🔗 Социальные сети":
        bot.send_message(message.chat.id, soc)
    elif (message.text == "⛺️ Домой"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("😈 VK 😈")
        btn2 = types.KeyboardButton("🛩 TG 🛩")
        btn3 = types.KeyboardButton("🎵 TikTok 🎵")
        btn4 = types.KeyboardButton('📷 Instagram 📷')
        btn5 = types.KeyboardButton("🏠 Launcher 🏠")
        btn6 = types.KeyboardButton("🕙 Clock 🕙")
        btn7 = types.KeyboardButton("🎶 Spotify 🎶")
        btn8 = types.KeyboardButton("😍 Status Bar 😍")
        btn9 = types.KeyboardButton("🔢 Calculator 🔢")
        btn10 = types.KeyboardButton("📷 Camera 📷")
        btn13 = types.KeyboardButton("⚒ Инфо 🛠")
        btn14 = types.KeyboardButton("🖼️ Gallery 🖼️")
        btn15 = types.KeyboardButton("🎤 Диктофон 🎤")
        btn16 = types.KeyboardButton("📆 Календарь 📆")
        btn17 = types.KeyboardButton("💭 Messages 💭")
        btn18 = types.KeyboardButton("🙍‍♂️ Контакты 🙍‍♂️")
        btn19 = types.KeyboardButton("📞 Call 📞")
        btn20 = types.KeyboardButton("🎧 Music 🎧")
        btn21 = types.KeyboardButton("⌨️ Keyboard ⌨️")
        btn22 = types.KeyboardButton("📒 Notes 📒")
        btn23 = types.KeyboardButton("📩 Notifications  📩")
        btn25 = types.KeyboardButton("❤️‍🔥 WhatsApp ❤️‍🔥")
        markup.add(btn25, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn23)
        markup.add(btn13)
        bot.send_message(message.chat.id, text='''✨ Телепорт в главное меню произошел успешно 😊'''.format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="😔 Простите, но.. я не знаю что вам ответить на это...")


        
         
        
bot.infinity_polling()

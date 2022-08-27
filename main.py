import time
from time import sleep
import telebot
from telebot import types # для указание типов
import caption
import files

bot = telebot.TeleBot("5400897291:AAGCWphbUiKx7r1ntjHQNfL75WaWCRk6cvA")


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
    bot.send_message(message.chat.id, text='''🙃 Приветствую дорогой пользователь.
Выбери понравившейся приложение ниже'''.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❤️‍🔥 WhatsApp ❤️‍🔥"):
        bot.send_document(message.chat.id, whatsapp)     
    elif(message.text == "😈 VK 😈"):
        bot.send_document(message.chat.id, files.vk, caption=caption.vkd)        
    elif(message.text == '📷 Instagram 📷'):
        bot.send_document(message.chat.id, files.inst, caption=caption.instd)        
    elif(message.text == "🛩 TG 🛩"):
        bot.send_document(message.chat.id, files.tg, caption=caption.tgd)
    elif(message.text == "🎶 Spotify 🎶"):
        bot.send_document(message.chat.id, files.spotify, caption=caption.spd)
    elif(message.text == "🏠 Launcher 🏠"):
        bot.send_document(message.chat.id, files.launcher, caption=caption.ld)
    elif(message.text == "🎵 TikTok 🎵"):
        bot.send_document(message.chat.id, files.tt, caption=caption.ttd)
    elif(message.text == "🕙 Clock 🕙"):
        bot.send_document(message.chat.id, files.clock, caption=caption.cld)
    elif(message.text == "😍 Status Bar 😍"):
        bot.send_document(message.chat.id, files.statusbar, caption=caption.sbd)
    elif(message.text == "📷 Camera 📷"):
        bot.send_document(message.chat.id, files.camera, caption=caption.cad)
    elif(message.text == "🔢 Calculator 🔢"):
        bot.send_document(message.chat.id, files.calc, caption=caption.calcd)
    elif(message.text == "🖼️ Gallery 🖼️"):
        bot.send_document(message.chat.id, files.gallery, caption=caption.gald)
    elif(message.text == "🎤 Диктофон 🎤"):
        bot.send_document(message.chat.id, files.voice, caption=caption.voiced)
    elif(message.text == "📆 Календарь 📆"):
        bot.send_document(message.chat.id, files.clnd, caption=caption.clndd)
    elif(message.text == "💭 Messages 💭"):
        bot.send_document(message.chat.id, files.msg, caption=caption.msgd)
    elif(message.text == "🙍‍♂️ Контакты 🙍‍♂️"):
        bot.send_document(message.chat.id, files.contacts, caption=caption.cntd)
    elif(message.text == "📞 Call 📞"):
        bot.send_document(message.chat.id, files.call, caption=caption.calld)
    elif(message.text == "🎧 Music 🎧"):
        bot.send_document(message.chat.id, files.music, caption=caption.msd)
    elif(message.text == "⌨️ Keyboard ⌨️"):
        bot.send_document(message.chat.id, files.kb, caption=caption.kbd)
    elif(message.text == "📒 Notes 📒"):
        bot.send_document(message.chat.id, files.notes, caption=caption.ntd)
    elif(message.text == "📩 Notifications  📩"):
        bot.send_document(message.chat.id, files.notify, caption=caption.ntf)

    elif(message.text == "⚒ Инфо 🛠"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🫠 Биография")
        btn3 = types.KeyboardButton("🔗 Социальные сети")
        btn4 = types.KeyboardButton("💸 Донат")
        back = types.KeyboardButton("⛺️ Домой")
        markup.add(btn1, btn3, btn4, back)
        bot.send_message(message.chat.id, text="😙 Тут вы можете узнать некоторую информацию о создателе", reply_markup=markup)

    elif(message.text == "🫠 Биография"):
        bot.send_message(message.chat.id, caption.bio)
    elif message.text == "💸 Донат":
        bot.send_message(message.chat.id, caption.donate)
    elif message.text == "🔗 Социальные сети":
        bot.send_message(message.chat.id, caption.soc)
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
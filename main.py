import time
from time import sleep
import telebot
from telebot import types # для указание типов
import caption
import files
import sqlite3
import configure

# Авторизация в бота
client = telebot.TeleBot(configure.config['token'])


# Команда старт и запись айди в базу данных
@client.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")

    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        users_list = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", users_list)
        connect.commit()
    else:
        pass

    # кнопочки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("😈 𝕍𝕜 😈")
    btn2 = types.KeyboardButton("💎 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞 💎")
    btn3 = types.KeyboardButton("🎵 𝕋𝕚𝕜𝕋𝕠𝕜 🎵")
    btn4 = types.KeyboardButton('🎡 𝕀𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞 🎡')
    btn5 = types.KeyboardButton("🏠 𝕃𝕒𝕦𝕟𝕔𝕙𝕖𝕣 🏠")
    btn6 = types.KeyboardButton("⏰ ℂ𝕝𝕠𝕔𝕜 ⏰")
    btn7 = types.KeyboardButton("🎶 𝕊𝕡𝕠𝕥𝕚𝕗𝕪 🎶")
    btn8 = types.KeyboardButton("😍 𝕊𝕥𝕒𝕥𝕦𝕤 𝔹𝕒𝕣 😍")
    btn9 = types.KeyboardButton("🧷 ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣 🧷")
    btn10 = types.KeyboardButton("🔐 𝕚𝕃𝕠𝕔𝕜 🔐")
    btn11 = types.KeyboardButton("🧭 𝕚ℂ𝕠𝕞𝕡𝕒𝕤𝕤 🧭")
    btn13 = types.KeyboardButton("⚒ 𝕀𝕟𝕗𝕠 🛠")
    btn14 = types.KeyboardButton("🖼️ 𝔾𝕒𝕝𝕝𝕖𝕣𝕪 🖼️")
    btn15 = types.KeyboardButton("🎤 𝕚𝕍𝕠𝕚𝕔𝕖 🎤")
    btn17 = types.KeyboardButton("💭 𝕄𝕖𝕤𝕤𝕒𝕘𝕖𝕤 💭")
    btn18 = types.KeyboardButton("🙍‍♂️ ℂ𝕠𝕟𝕥𝕒𝕔𝕥𝕤 🙍‍♂️")
    btn19 = types.KeyboardButton("📱 ℂ𝕒𝕝𝕝𝕤 📱")
    btn20 = types.KeyboardButton("🎧 𝕄𝕦𝕤𝕚𝕔 🎧")
    btn21 = types.KeyboardButton("⌨️ 𝕂𝕖𝕪𝕓𝕠𝕒𝕣𝕕 ⌨️")
    btn22 = types.KeyboardButton("📒 ℕ𝕠𝕥𝕖𝕤 📒")
    btn23 = types.KeyboardButton("💌ℕ𝕠𝕥𝕚𝕗𝕚𝕔𝕒𝕥𝕚𝕠𝕟𝕤💌")
    btn25 = types.KeyboardButton("❤️‍🔥𝕎𝕙𝕒𝕥𝕤𝔸𝕡𝕡❤️‍🔥")
    markup.add(btn25)
    markup.add(btn3, btn7)
    markup.add(btn1, btn2, btn4)
    markup.add(btn9, btn6)
    markup.add(btn8)
    markup.add(btn19, btn18)
    markup.add(btn21, btn23, btn17)
    markup.add(btn5, btn10)
    markup.add(btn22)
    markup.add(btn11)
    markup.add(btn14, btn15, btn20)
    markup.add(btn13)
    client.send_message(message.chat.id, text=caption.welcome.format(message.from_user), reply_markup=markup)

    # действия на кнопочки
@client.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❤️‍🔥𝕎𝕙𝕒𝕥𝕤𝔸𝕡𝕡❤️‍🔥"):
        client.send_document(message.chat.id, files.whatsapp)     
    elif(message.text == "😈 𝕍𝕜 😈"):
        client.send_document(message.chat.id, files.vk, caption=caption.vkd)
    elif(message.text == "🔐 𝕚𝕃𝕠𝕔𝕜 🔐"):
        client.send_document(message.chat.id, files.ilock, caption=caption.ilockd)  
    elif(message.text == '🎡 𝕀𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞 🎡'):
        client.send_document(message.chat.id, files.inst, caption=caption.instd)        
    elif(message.text == "💎 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞 💎"):
        client.send_document(message.chat.id, files.tg, caption=caption.tgd)
    elif(message.text == "🎶 𝕊𝕡𝕠𝕥𝕚𝕗𝕪 🎶"):
        client.send_document(message.chat.id, files.spotify, caption=caption.spd)
    elif(message.text == "🏠 𝕃𝕒𝕦𝕟𝕔𝕙𝕖𝕣 🏠"):
        client.send_document(message.chat.id, files.launcher, caption=caption.ld)
    elif(message.text == "🎵 𝕋𝕚𝕜𝕋𝕠𝕜 🎵"):
        client.send_document(message.chat.id, files.tt, caption=caption.ttd)
    elif(message.text == "⏰ ℂ𝕝𝕠𝕔𝕜 ⏰"):
        client.send_document(message.chat.id, files.clock, caption=caption.cld)
    elif(message.text == "😍 𝕊𝕥𝕒𝕥𝕦𝕤 𝔹𝕒𝕣 😍"):
        client.send_document(message.chat.id, files.statusbar, caption=caption.sbd)
    elif(message.text == "🧷 ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣 🧷"):
        client.send_document(message.chat.id, files.calc, caption=caption.calcd)
    elif(message.text == "🖼️ 𝔾𝕒𝕝𝕝𝕖𝕣𝕪 🖼️"):
        client.send_document(message.chat.id, files.gallery, caption=caption.gald)
    elif(message.text == "🎤 𝕚𝕍𝕠𝕚𝕔𝕖 🎤"):
        client.send_document(message.chat.id, files.voice, caption=caption.voiced)
    elif(message.text == "💭 𝕄𝕖𝕤𝕤𝕒𝕘𝕖𝕤 💭"):
        client.send_document(message.chat.id, files.msg, caption=caption.msgd)
    elif(message.text == "🙍‍♂️ ℂ𝕠𝕟𝕥𝕒𝕔𝕥𝕤 🙍‍♂️"):
        client.send_document(message.chat.id, files.contacts, caption=caption.cntd)
    elif(message.text == "📱 ℂ𝕒𝕝𝕝𝕤 📱"):
        client.send_document(message.chat.id, files.call, caption=caption.calld)
    elif(message.text == "🎧 𝕄𝕦𝕤𝕚𝕔 🎧"):
        client.send_document(message.chat.id, files.music, caption=caption.msd)
    elif(message.text == "⌨️ 𝕂𝕖𝕪𝕓𝕠𝕒𝕣𝕕 ⌨️"):
        client.send_document(message.chat.id, files.kb, caption=caption.kbd)
    elif(message.text == "📒 ℕ𝕠𝕥𝕖𝕤 📒"):
        client.send_document(message.chat.id, files.notes, caption=caption.ntd)
    elif(message.text == "💌ℕ𝕠𝕥𝕚𝕗𝕚𝕔𝕒𝕥𝕚𝕠𝕟𝕤💌"):
        client.send_document(message.chat.id, files.notify, caption=caption.ntf)
    elif(message.text == "🧭 𝕚ℂ𝕠𝕞𝕡𝕒𝕤𝕤 🧭"):
        client.send_document(message.chat.id, files.cmps, caption=caption.cmpsd)
    

    # инфа обо мне и повторная попытка записи в бд если человек не нажимал старт после обновы
    elif(message.text == "⚒ 𝕀𝕟𝕗𝕠 🛠"):

        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            id INTEGER
        )""")

        connect.commit()

        people_id = message.chat.id
        cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
        data = cursor.fetchone()
        if data is None:
            users_list = [message.chat.id]
            cursor.execute("INSERT INTO login_id VALUES(?);", users_list)
            connect.commit()
        else:
            pass

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🫠 Биография")
        btn3 = types.KeyboardButton("🔗 Социальные сети")
        btn4 = types.KeyboardButton("💸 Донат")
        back = types.KeyboardButton("⛺️ Домой")
        markup.add(btn1, btn3, btn4, back)
        client.send_message(message.chat.id, text="😙 Тут вы можете узнать некоторую информацию о создателе", reply_markup=markup)

    elif(message.text == "🫠 Биография"):
        client.send_message(message.chat.id, caption.bio)
    elif message.text == "💸 Донат":
        client.send_message(message.chat.id, caption.donate)
    elif message.text == "🔗 Социальные сети":
        client.send_message(message.chat.id, caption.soc)
    elif (message.text == "⛺️ Домой"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("😈 𝕍𝕜 😈")
        btn2 = types.KeyboardButton("💎 𝕋𝕖𝕝𝕖𝕘𝕣𝕒𝕞 💎")
        btn3 = types.KeyboardButton("🎵 𝕋𝕚𝕜𝕋𝕠𝕜 🎵")
        btn4 = types.KeyboardButton('🎡 𝕀𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞 🎡')
        btn5 = types.KeyboardButton("🏠 𝕃𝕒𝕦𝕟𝕔𝕙𝕖𝕣 🏠")
        btn6 = types.KeyboardButton("⏰ ℂ𝕝𝕠𝕔𝕜 ⏰")
        btn7 = types.KeyboardButton("🎶 𝕊𝕡𝕠𝕥𝕚𝕗𝕪 🎶")
        btn8 = types.KeyboardButton("😍 𝕊𝕥𝕒𝕥𝕦𝕤 𝔹𝕒𝕣 😍")
        btn9 = types.KeyboardButton("🧷 ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣 🧷")
        btn10 = types.KeyboardButton("🔐 𝕚𝕃𝕠𝕔𝕜 🔐")
        btn13 = types.KeyboardButton("⚒ 𝕀𝕟𝕗𝕠 🛠")
        btn11 = types.KeyboardButton("🧭 𝕚ℂ𝕠𝕞𝕡𝕒𝕤𝕤 🧭")
        btn14 = types.KeyboardButton("🖼️ 𝔾𝕒𝕝𝕝𝕖𝕣𝕪 🖼️")
        btn15 = types.KeyboardButton("🎤 𝕚𝕍𝕠𝕚𝕔𝕖 🎤")
        btn17 = types.KeyboardButton("💭 𝕄𝕖𝕤𝕤𝕒𝕘𝕖𝕤 💭")
        btn18 = types.KeyboardButton("🙍‍♂️ ℂ𝕠𝕟𝕥𝕒𝕔𝕥𝕤 🙍‍♂️")
        btn19 = types.KeyboardButton("📱 ℂ𝕒𝕝𝕝𝕤 📱")
        btn20 = types.KeyboardButton("🎧 𝕄𝕦𝕤𝕚𝕔 🎧")
        btn21 = types.KeyboardButton("⌨️ 𝕂𝕖𝕪𝕓𝕠𝕒𝕣𝕕 ⌨️")
        btn22 = types.KeyboardButton("📒 ℕ𝕠𝕥𝕖𝕤 📒")
        btn23 = types.KeyboardButton("💌ℕ𝕠𝕥𝕚𝕗𝕚𝕔𝕒𝕥𝕚𝕠𝕟𝕤💌")
        btn25 = types.KeyboardButton("❤️‍🔥𝕎𝕙𝕒𝕥𝕤𝔸𝕡𝕡❤️‍🔥")
        markup.add(btn25)
        markup.add(btn3, btn7)
        markup.add(btn1, btn2, btn4)
        markup.add(btn9, btn6)
        markup.add(btn8)
        markup.add(btn19, btn18)
        markup.add(btn21, btn23, btn17)
        markup.add(btn5, btn10)
        markup.add(btn22)
        markup.add(btn11)
        markup.add(btn14, btn15, btn20)
        markup.add(btn13)
        client.send_message(message.chat.id, text='''✨ Телепорт в главное меню прошел успешно 😊'''.format(message.from_user), reply_markup=markup)
    else:
        client.send_message(message.chat.id, text="😔 Простите, но.. я не знаю что вам ответить на это...")
     





# вечная работа бота
client.infinity_polling()
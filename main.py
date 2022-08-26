import time
from time import sleep
import telebot
from telebot import types # для указание типов


bot = telebot.TeleBot("5400897291:AAGCWphbUiKx7r1ntjHQNfL75WaWCRk6cvA")
admins = [1484386024, 5184725450]


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
    btn11 = types.KeyboardButton("🔎 App Store 🔎")
    btn12 = types.KeyboardButton("⁤⁤ ")
    btn13 = types.KeyboardButton("Инфо")
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
    btn26 = types.KeyboardButton(" ⁤")
    markup.add(btn25, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn11, btn9, btn10, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn26, btn23,  btn12,  btn13)
    bot.send_message(message.chat.id, text='''Выбери любое приложение из списка ниже'''.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "❤️‍🔥 WhatsApp ❤️‍🔥"):
        bot.send_document(message.chat.id, whatsapp)

    elif(message.text == "😈 VK 😈"):
        bot.send_message(message.chat.id, """🔥 SOVA RE — модифицированный клиент вконтакте в стиле ios с большим количеством настроек.
🔹 Преимущества:
- Нечиталка, которую можно самому настроить.
- Неписалка, которую также можно настроить.
- Вечный онлайн.
- Частично скрыть свой онлайн. (Будет показано только если вы обновите страницу и т.п.)
- Скачивание и прослушивание музыки без подписки
- и многое другое
""")
        sleep(0.7)
        bot.send_document(message.chat.id, vk)
    elif(message.text == '📷 Instagram 📷'):
        bot.send_message(message.chat.id, """📷 Instander — крутой и функциональный мод на официальную версию инстаграм с множеством крутым функций.
🔹 Преимущества:
- Нечиталка
- Неписалка
- Скрыть просмотр сторис
- Скрыть просмотр трансляций
- Скачивание публикаций, сторисов, reels
- Улучшение качество фотографий
- и так далее...""")
        sleep(0.7)
        bot.send_document(message.chat.id, inst)
    elif(message.text == "🛩 TG 🛩"):
        bot.send_message(message.chat.id, """✈️ Ibreym-Telegram — долгожданный мод на телеграм, оптимизированный и улучшенный мною, в котором шикарный дизайн, и русский язык.
🔷 Преимущества:
— Возможность менять шрифты, выбирать разные темы и цвета, красивый, и удобный ios дизайн.
— На русском языке.
— Без рекламы.
— Добавлены IOS смайлы
и т.д.""")
        sleep(0.7)
        bot.send_document(message.chat.id, tg)
    elif(message.text == "🎶 Spotify 🎶"):
        bot.send_message(message.chat.id, '''🎵 Spotify 8.7.2.1205 - Интернет-сервис потокового аудио, позволяющий легально и бесплатно прослушивать более 50 миллионов музыкальных композиций, аудиокниг и подкастов.
🔹 Преимущества:
* Разблокировано очень высокое качество звука
* Разлочен импорт ваших музыкальных файлов
* Неограниченное перемешивание
* Разблокирован Spotify Connect
* Режим повтора
* Отключена реклама
* Некоторые функции на стороне сервера все же требуют платной подписки.''')
        sleep(0.7)
        bot.send_document(message.chat.id, spotify)
    elif(message.text == "🏠 Launcher 🏠"):
        bot.send_message(message.chat.id, """🔥Apple Launcher  — приложение с помощью которого вы можете превратить свой рабочий стол андроида в айфон. Меняет иконки, стиль, запись экрана на ios.""")
        sleep(0.7)
        bot.send_document(message.chat.id, launcher)
    elif(message.text == "🎵 TikTok 🎵"):
        bot.send_message(message.chat.id, """🎵 Tik-Tok. Крупное приложение с огромным количеством коротких но позитивных видео.
🔹 Преимущества
* Можно скачивать любые видео без водяных знаков.
* Айфоновские смайлы
* Улучшено качество видео
* Требует меньше трафика
* и так далее...""")
        sleep(0.7)
        bot.send_document(message.chat.id, tt)
    elif(message.text == "🕙 Clock 🕙"):
        bot.send_message(message.chat.id, """🕙 Clock
Будильник, таймер, секундомер и просто часы как на айфоне.
🔹 Преимущества:
* Удалена реклама.
* Удалено лишнее.
* Тёмные и светлые темы.
* Оригинальное название, иконка.
* И другое...""")
        sleep(0.7)
        bot.send_document(message.chat.id, clock)
    elif(message.text == "😍 Status Bar 😍"):
        bot.send_message(message.chat.id, """🔥Ibreym-Status-Bar — айфоновский статус бар на любой андроид, с крутыми фишками и настройками, который также кстати перекрывает ваш обычный бар андроида.""")
        sleep(0.7)
        bot.send_document(message.chat.id, statusbar)
    elif(message.text == "🔎 App Store 🔎"):
        bot.send_message(message.chat.id, """🔥Ibreym-Status-Bar — айфоновский статус бар на любой андроид, с крутыми фишками и настройками, который также кстати перекрывает ваш обычный бар андроида.""")
        sleep(0.7)
        bot.send_document(message.chat.id, appstore)
    elif(message.text == "📷 Camera 📷"):
        bot.send_message(message.chat.id, """🔥Ibreym-Status-Bar — айфоновский статус бар на любой андроид, с крутыми фишками и настройками, который также кстати перекрывает ваш обычный бар андроида.""")
        sleep(0.7)
        bot.send_document(message.chat.id, camera)
    elif(message.text == "🔢 Calculator 🔢"):
        bot.send_message(message.chat.id, """🚀iCalculator PRO — это калькулятор в стиле ios на андроид с различными функциями, возможностями и с поддержкой темной и светлой темы.""")
        sleep(0.7)
        bot.send_document(message.chat.id, calc)
    elif(message.text == "🖼️ Gallery 🖼️"):
        bot.send_message(message.chat.id, """🔥iPhoto — ещё одна красивая и удобная галерея в стиле ios на android. С ios дизайн, шрифтом и с открытой pro версией. Доступна тёмная тема, корзина и возможность скрыть файлы.""")
        sleep(0.7)
        bot.send_document(message.chat.id, gallery)
    elif(message.text == "🎤 Диктофон 🎤"):
        bot.send_message(message.chat.id, """🚀iVoice Pro — диктофон в стиле ios в полным дизайном и функционалом iphone на android. Доступны тёмная и светлая тема, выбор качества и полная версия без рекламы.""")
        sleep(0.7)
        bot.send_document(message.chat.id, voice)
    elif(message.text == "📆 Календарь 📆"):
        bot.send_message(message.chat.id, """📆 iCalendar Pro — календарь с интерфейсом в стиле ios на ваш android. Поддержка темной и светлой темы, выбор формата времени, напоминания и прочее.""")
        sleep(0.7)
        bot.send_document(message.chat.id, clnd)
    elif(message.text == "💭 Messages 💭"):
        bot.send_message(message.chat.id, """🔥iMessage Pro — если вам наскучил обычный дизайн ваших сообщений, это приложение для вас! Это сообщения в стиле ios с разными темами и красивейшим ios дизайном.""")
        sleep(0.7)
        bot.send_document(message.chat.id, msg)
    elif(message.text == "🙍‍♂️ Контакты 🙍‍♂️"):
        bot.send_message(message.chat.id, """🚀iContacts Pro — это крутая прога, контакты в стиле ios на android, дизайн ios, доступны темная, светлая, или авто темы и прочее, без рекламы.""")
        sleep(0.7)
        bot.send_document(message.chat.id, contacts)
    elif(message.text == "📞 Call 📞"):
        bot.send_message(message.chat.id, """🔥iCallScreen Pro — если вам надоел обычный экран звонков на вашем телефоне, данное приложение поможет изменить экран звонка на стиль ios""")
        sleep(0.7)
        bot.send_document(message.chat.id, call)
    elif(message.text == "🎧 Music 🎧"):
        bot.send_message(message.chat.id, """🚀Музыкальный плеер ios на android.
iMusic —  отличная замена для вашего обычного музыкального плеера на плеер с красивым стилем ios. С поддержкой темных и светлых тем, и другими функциями.""")
        sleep(0.7)
        bot.send_document(message.chat.id, music)
    elif(message.text == "⌨️ Keyboard ⌨️"):
        bot.send_message(message.chat.id, """🔥Ibreym Keyboard - удобная клавиатура как на айфоне на ваш androd. В приложении 4 разных тем, русский язык и ios смайлы.""")
        sleep(0.7)
        bot.send_document(message.chat.id, kb)
    elif(message.text == "📒 Notes 📒"):
        bot.send_message(message.chat.id, """🔥iNotes — это приложение для создания заметок в стиле ios на android с ios 14.5 эмоджи! Отлично работает, поддерживает чёрную, и светлую тему, а также для вас открыта полная версия.""")
        sleep(0.7)
        bot.send_document(message.chat.id, notes)
    elif(message.text == "📩 Notifications  📩"):
        bot.send_message(message.chat.id, """🔥Floatify — приложение для настройки уведомлений на вашем андроид устройстве как на айфоне, где можно выбрать три разных версий ios, а также настроить по своему усмотрению.""")
        sleep(0.7)
        bot.send_document(message.chat.id, notify)








        # Доп кнопки
    elif(message.text == "Инфо"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Создатель")
        btn2 = types.KeyboardButton("Канал создателя")
        btn3 = types.KeyboardButton("Соц. сети автора")
        btn4 = types.KeyboardButton("Донат")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Информация о создателе", reply_markup=markup)




    elif(message.text == "Создатель"):
        bot.send_message(message.chat.id, "Привет! Я Токсик. Такой-же простой паренёк как и вы. \nМне 16 лет. Некоторые из моих увлечений: \n* Создание ботов \n* Создание сайтов \n* Скрипты \n* Модули для юзерботов \n* и многое другое. \n\n Работаю на языке программирования 'Python', и частично изучаю HTML. \nСвязаться со мной вы можете нажав на кнопку 'Соц. сети автора'.  \n\n С уважением, Токсик")
    elif message.text == "Канал создателя":
        bot.send_message(message.chat.id, text="Я являюсь админом такого проекта как ХакерФон (@HACKER_PHONE_VIP) Можешь зайти туда и пообщаться со мной и с другими добрыми людьми как и я.")
    elif message.text == "Донат":
        bot.send_message(message.chat.id, "Хочешь задонатить Токсику или просто скинуть рубль на киви? \nЯ не такой человек чтобы выпрашивать, поэтому ссылку ставить не буду. \nНо если все-таки есть желание сделать мне приятнее, то вот ник киви: TOXIC2290")
    elif message.text == "Соц. сети автора":
        bot.send_message(message.chat.id, text="""
✨ Все соц. сети автора:
VK = https://vk.com/toxyy
TG = https://t.me/ToXicUse
TG (2) = https://t.me/SecureTox
Discord = https://discord.gg/kBUcfepVHq
Instagram = https://instagram.com/zxctoxicuse
Site = http://gg.gg/Toxicuse""")
    elif (message.text == "Вернуться в главное меню"):
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
        btn11 = types.KeyboardButton("🔎 App Store 🔎")
        btn12 = types.KeyboardButton("⁤⁤ ")
        btn13 = types.KeyboardButton("Инфо")
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
        btn26 = types.KeyboardButton(" ⁤")
        markup.add(btn25, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn11, btn9, btn10, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22, btn26, btn23, btn12,  btn13)
        bot.send_message(message.chat.id, text='''Вы в главном меню'''.format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="К сожалению, я не знаю что вам на это ответить:(")


        
        
@bot.message_handler(commands=['send'])
def notify(message):
    command_sender = message.from_user.id
    if command_sender in admins:
        with open(r'C:\id.txt') as ids:
            for line in ids:
                user_id = int(line.strip("\n"))
                try:
                    bot.send_message(user_id,  f'уведомление от {command_sender}')
                except Exception as e:
                    bot.send_message(command_sender, f'ошибка отправки сообщения юзеру - {user_id}')
    else:
        bot.send_message(command_sender, f'у вас нет прав для запуска команды')
        
        
bot.infinity_polling()

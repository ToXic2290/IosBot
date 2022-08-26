import telebot

bot = telebot.TeleBot("5400897291:AAGCWphbUiKx7r1ntjHQNfL75WaWCRk6cvA")

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, text='''⚙️ Бот на перезагрузке...''')
  
@bot.message_handler(content_types=['text'])
def func(message):
  if(message.text == "❤️‍🔥 WhatsApp ❤️‍🔥"):
    bot.send_document(message.chat.id, "⚙️ Бот на перезагрузке...")
  else:
    bot.send_document(message.chat.id, "⚙️ Бот на перезагрузке...")

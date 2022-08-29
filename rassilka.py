joinedFile = open("IosBot/users.db", 'r')
joinedUsers = set ()

@bot.message_handler(commands=["special"])
def mess(message):
	for user in joinedUsers:
		bot.send_message(user, message.text[message.text.find(' '):])
		
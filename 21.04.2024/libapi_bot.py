import telebot
token = '7034065280:AAF3jmtTIBhQSRMlLFC7ivse2-0ezn8RzY4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Как твои дела Когда приедет женя')

@bot.message_handler(content_types='text')
def reverse_text(message):
    text = message.text[::-1]
    bot.reply_to(message, text)

bot.polling()


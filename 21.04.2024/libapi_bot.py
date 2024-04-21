import telebot
import time
token = '7034065280:AAF3jmtTIBhQSRMlLFC7ivse2-0ezn8RzY4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Как твои дела Когда приедет женя')

@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i+1)

@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'глеб' in message.text.lower():
        bot.reply_to(message, 'В тексте имеется слово глеб')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)


@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, 'f***{text.upper()}!***')


bot.polling()


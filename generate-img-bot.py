import telebot
from g4f.client import Client
from generateimgsber import gen

bot = telebot.TeleBot('7071800191:AAGIs28xt9bsQonvemOezuxjG0K1M9U9nGI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, чем я могу помочь тебе сегодня?.")

# Обработка геопозиции
@bot.message_handler(func=lambda callback: True)
def handle_location(message):
    try:
        # необходимо заменить 'api_key', 'secret_key' на собственные
        content = gen(message.text, 'api_key', 'secret_key')
        bot.send_photo(message.chat.id, content)
    except:
        bot.send_message(message.chat.id, 'Извините, я вас не понял')

bot.polling()

from generate_img_with_sber import gen_img

import telebot
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, чем я могу помочь тебе сегодня?.")

# Обработка всех сообщений
@bot.message_handler(func=lambda callback: True)
def handle_location(message):
    try:
        # необходимо заменить 'api_key', 'secret_key' на собственные
        content = gen_img(message.text, api_key, secret_key)
        bot.send_photo(message.chat.id, content)
    except:
        bot.send_message(message.chat.id, 'Извините, я вас не понял')

bot.polling()
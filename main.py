import telebot
from g4f.client import Client

bot = telebot.TeleBot('7071800191:AAGIs28xt9bsQonvemOezuxjG0K1M9U9nGI')


def get_info_wolfram(query):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
    )
    return response.choices[0].message.content


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, чем я могу помочь тебе сегодня?.")

# Обработка геопозиции
@bot.message_handler(func=lambda callback: True)
def handle_location(message):
    try:
        content = get_info_wolfram(message.text)
        bot.send_message(message.chat.id, content)
    except:
        bot.send_message(message.chat.id, 'Извините, я вас не понял')

bot.polling()

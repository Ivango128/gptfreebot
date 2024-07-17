from g4f.client import Client

def get_info_wolfram(query):
    # создаем экземпляр чат-бота
    client = Client()
    # подготавливаем запрос
    # ВНИМАНИЕ! лучше оставить даннные настройтки по умолчанию
    response = client.chat.completions.create(
        # указываем модуль чат-gpt
        model="gpt-3.5-turbo",
        # подставляем текст запроса, под ключ content
        messages=[{"role": "user", "content": query}],
    )
    # возвращаем ответ от чат-gpt
    return response.choices[0].message.content

import telebot

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, чем я могу помочь тебе сегодня?.")

# Обработка всех сообщений
@bot.message_handler(func=lambda callback: True)
def handle_location(message):
    try:
        content = get_info_wolfram(message.text)
        bot.send_message(message.chat.id, content)
    except:
        bot.send_message(message.chat.id, 'Извините, я вас не понял')

bot.polling()

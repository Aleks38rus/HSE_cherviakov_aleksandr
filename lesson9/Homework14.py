import random

"""
Создайте бот-справочник с красивым меню (используйте KeyBoardButton и ReplyKeyboardMarkup).

Разделы можете придумать самостоятельно — самое главное, чтобы через меню, которое возвращает бот, можно было переходить между разделами и получать информацию от бота. 

Если у вас нет данных, чтобы добавить добавить в справочную информацию, вы можете использовать тексты-заглушки (например, «Lorem Ipsum»). Достаточно реализовать функционал, а наполнение остаётся на ваше усмотрение.
"""
import telebot
from telebot import types

bot_token = '' # bot father токен
f = open('advice.txt', 'r', encoding='UTF-8')
advice = f.read().split('\n')
f.close()
f = open('jokes.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Совет 🦉")
    item2 = types.KeyboardButton("Шутка 🤡")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nСовет чтобы получить совет дня\nШутка — для получения смешной шутки ',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip().find('Совет') != -1:
        bot.send_message(message.chat.id, random.choice(advice))
    elif message.text.strip().find('Шутка') != -1:
        bot.send_message(message.chat.id, random.choice(jokes))


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

"""
Создайте Telegram-бота для анкетирования пользователей.

Вопросы и данные придумайте самостоятельно.

"""
import sqlite3

import telebot
from telebot import types

connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Answers (
chat_id INTEGER,
answer TEXT NOT NULL)
''')

bot_token = ''  # bot father токен
bot = telebot.TeleBot(bot_token)


def insert(chat_id: int, answer: str):
    cursor.execute('INSERT INTO Answers (chat_id, answer) VALUES (?, ?)', (chat_id, answer))
    connection.commit()


def get_answers(chat_id: int):
    cursor.execute('SELECT answer  FROM Answers WHERE chat_id = ?', (chat_id,))
    return cursor.fetchall()


@bot.message_handler(commands=["start"])
def start(m, res=False):
    chatId = m.chat.id

    bot.send_message(chatId, 'Какой ваш любимый цвет?')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    chat_id = message.chat.id

    if message.text.strip().find('Мой ответы') != -1:
        bot.send_message(message.chat.id, get_answers(chat_id))
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Мой ответы"))
        answer = message.text.strip()
        insert(chat_id, answer)
        bot.send_message(message.chat.id, "Записано!", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

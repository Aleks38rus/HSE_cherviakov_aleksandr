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
answer TEXT,
question TEXT NOT NULL
)
''')

bot_token = '7255438902:AAGSGrtUeHI_2OYEGMTefJL94AS0cvEvf34' # bot father токен
bot = telebot.TeleBot(bot_token)

question1 = 'Какого цвета нет в светофоре?'
answers1 = ['Красный', 'Желтый', 'Черный']

question2 = 'Кто всю ночь по крыше бьёт Да постукивает, И бормочет, и поёт, убаюкивает?'
answers2 = ['Кот', 'Дождь', 'Компьютер']

question3 = 'Сколько будет 10+10*2'
answers3 = ['22', '30', 'Не знаю']


def insert(chat_id: int, answer: str, question: str):
    cursor.execute('INSERT INTO Answers (chat_id, answer, question) VALUES (?, ?, ?)', (chat_id, answer, question))
    connection.commit()


def get_answers(chat_id: int):
    cursor.execute('SELECT question || answer FROM Answers WHERE chat_id = ?', (chat_id,))
    return cursor.fetchall()


def make_answer_markup(answers: list):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for answer in answers:
        markup.add(types.KeyboardButton(answer))
    return markup


@bot.message_handler(commands=["start"])
def start(m, res=False):
    chatId = m.chat.id

    bot.send_message(chatId, question1, reply_markup=make_answer_markup(answers1))


@bot.message_handler(content_types=["text"])
def handle_text(message):
    chat_id = message.chat.id
    answer = message.text.strip()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Мои ответы"))

    if answer.find('Мои ответы') != -1:
        result_answers = '\n'.join(str(x) for x in get_answers(chat_id))
        bot.send_message(message.chat.id, result_answers)
    elif answer in answers1 != -1:
        insert(chat_id, answer, question1)
        bot.send_message(message.chat.id, question2, reply_markup=make_answer_markup(answers2))
    elif answer in answers2 != -1:
        insert(chat_id, answer, question2)
        bot.send_message(message.chat.id, question3, reply_markup=make_answer_markup(answers3))
    elif answer in answers3 != -1:
        insert(chat_id, answer, question3)
        bot.send_message(message.chat.id, 'Записано!', reply_markup=markup)
    else:
        answer = message.text.strip()
        bot.send_message(message.chat.id, answer + ' это не правильный ответ!', reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

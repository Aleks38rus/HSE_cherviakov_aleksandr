import csv
import json
import re

"""
1. Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле
traders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла
traders.txt в файл traders.csv.
"""


def task_1():
    with open("traders.txt", "r") as file:
        inns = [i.rstrip() for i in file.readlines()]
    with open("traders.json", "r") as file:
        traders = json.load(file)
    traders = {i["inn"]: i for i in traders}

    result = []

    for inn in inns:
        result.append(traders[inn])

    with open('traders.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['ИНН', 'ОГРН', 'Адрес'])
        for i in result:
            writer.writerow([i['inn'], i['ogrn'], i['address']])


task_1()

"""
Напишите регулярное выражение для поиска email-адресов в тексте.
Для этого напишите функцию, которая принимает в качестве аргумента текст в виде
строки и возвращает список найденных email-адресов или пустой список, если
email-адреса не найдены.
Используйте датасет на 1 000 сообщений из Единого федерального реестра сведений
о банкротстве (ЕФРСБ) для практики.
Текст сообщений можно найти по ключу msg_text.
Найдите все email-адреса в датасете и соберите их в словарь, где ключом будет
выступать ИНН опубликовавшего сообщение publisher_inn, а в значении будет
храниться множество set() с email-адресами.
Сохраните собранные данные в файл emails.json.
"""


def find_emails(text):
    pattern = re.compile(r'[a-zA-Z.-]+@[\w.-]+')
    return re.findall(pattern, text)


def task_2():
    with open("1000_efrsb_messages.json", "r") as file:
        data = json.load(file)
        result = {}
        for item in data:
            emails = find_emails(item['msg_text'])
            for email in emails:
                email = email.lower()
                inn = item['publisher_inn']
                value = result.pop(inn, set())
                value.add(email)
                result.update({inn: value})
        with open('emails.json', "w") as f:
            json.dump({str(key): str(value) for key, value in result.items()}, f)


task_2()

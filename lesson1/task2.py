"""
2.	Пользователь вводит время в секундах.
Рассчитайте время и сохраните отдельно в каждую переменную количество часов, минут и секунд.
Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
Используйте приведение типов для перевода строк в числовые типы.
Предусмотрите проверку строки на наличие только числовых данных через встроенный строковый метод .isdigit().
"""

print("Введите секунды")
input = input()

if input.isdigit():
    seconds = int(input)
    print("seconds:" + str(seconds))
    minutes = seconds / 60
    print("minutes: " + str(minutes))
    hour = minutes / 60
    print("hour: " + str(hour))
else:
    print(input + " не число")

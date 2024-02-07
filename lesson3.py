"""
3.	Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.

Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

Выведите данные в консоль.
"""
print(" Введите число от 1 до 9")

inputValue = input()
if not inputValue.isdigit() or (int(inputValue) < 1 or int(inputValue) > 9):
    print("Число не подходит")
else:
    firstInt = int(inputValue)
    secondInt = firstInt + firstInt * 10
    thirdInt = secondInt + firstInt * 100
    print("Результат: ")
    print(firstInt + secondInt + thirdInt)

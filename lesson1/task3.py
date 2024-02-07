"""
3.	Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.

Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

Выведите данные в консоль.
"""
print(" Введите число от 1 до 9")

input_value = input()
if not input_value.isdigit() or (int(input_value) < 1 or int(input_value) > 9):
    print("Число не подходит")
else:
    first_int = int(input_value)
    second_int = first_int + first_int * 10
    third_int = second_int + first_int * 100
    print("Результат: ")
    print(first_int + second_int + third_int)

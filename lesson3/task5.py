"""
Создайте ряд функций для проведения математических вычислений:
● функция вычисления факториала числа (произведение натуральных чисел от 1
до n). Принимает в качестве аргумента число, возвращает его факториал;
● поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из
трёх чисел, возвращает наибольшее из них;
● расчёт площади прямоугольного треугольника. Принимает в качестве аргумента
размер двух катетов треугольника. Возвращает площадь треугольника.
"""


def factorial(n):
    result = 1
    for number in range(1, n + 1):
        result = result * number

    return result


def max_of(first, second, third):
    fist_max = max(first, second)
    second_max = max(second, third)
    return max(fist_max, second_max)


def triangle_square(first, second):
    return (first * second) / 2

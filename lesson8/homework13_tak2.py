"""
Задание 2
Напишите функцию, которая будет принимать в себя тип данных int (число) и
возвращать тип bool, если переданное число является палиндромом.
 """


def is_palindrome(str):
    for i in range(0, len(str)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    print("121 =", is_palindrome('121'))
    print("-121 =", is_palindrome('-121'))

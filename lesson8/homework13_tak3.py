"""
Задание 3
Напишите функцию, которая в качестве аргументов принимает массив (list) с числами
и целевое число. Функция должна возвращать индексы элементов, которые в сумме
дают целевое число.
 """


def test_array(nums: list, target: int):
    result = list()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)

    return result


if __name__ == "__main__":
    print("nums = [2,7,11,15], target = 9", test_array([2, 7, 11, 15], 9))
    print("nums = [3,2,4], target = 6", test_array([3, 2, 4], 6))
    print("nums = [3,3], target = 6", test_array([3, 3], 6))

# Task 1
# Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13

# 1,2,4,8,16,32
# 1,3,9,27

# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

import math

def is_arithmetic(sequence: list) -> bool:  # Функція для перевірки чи це арифметична послідовність
    if len(sequence) < 2:
        return False
    d = sequence[1] - sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != d:
            return False
    return True

def is_arithmetic_res(sequence: list) -> int:  # функція для розрахунку наступного числа ар.послідовності
    result = sequence[1] - sequence[0] + sequence[-1]
    return result


def is_geometric(sequence: list) -> bool:  # Функція для перевірки чи це геометрична послідовність
    if len(sequence) < 2:
        return False
    d = sequence[1] // sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i + 1] // sequence[i] != d:
            return False
    return True

def is_geometric_res(sequence: list) -> int:  # функція для розрахунку наступного числа геом.послідовності
    result = sequence[1] // sequence[0] * sequence[-1]
    return result


def is_square_numbers(sequence: list) -> bool:  # Функція для перевірки чи це послід. квадрата натуральних чисел
    if len(sequence) < 2:
        return False
    d = math.sqrt(sequence[1]) - math.sqrt(sequence[0])
    for i in range(len(sequence) - 1):
        if math.sqrt(sequence[i + 1]) - math.sqrt(sequence[i]) != d:
            return False
    return True


def is_square_numbers_res(sequence: list) -> int:  # функція для розрахунку наступного числа квадр.натур.чис
    d = math.sqrt(sequence[1]) - math.sqrt(sequence[0])
    result = (math.sqrt(sequence[-1]) + d) ** 2
    return result


def is_cubic_numbers(sequence: list) -> bool:  # Функція для перевірки чи це послід. куб. натуральних чисел
    if len(sequence) < 2:
        return False
    d = math.pow(sequence[1], 1 / 3) - math.pow(sequence[0], 1 / 3)
    for i in range(len(sequence) - 1):
        if math.pow(sequence[i + 1], 1 / 3) - math.pow(sequence[i], 1 / 3) != d:
            return False
    return True


def is_cubic_numbers_res(sequence: list) -> int:  # функція для розрахунку наступного числа куб.натур.чис
    d = math.pow(sequence[1], 1 / 3) - math.pow(sequence[0], 1 / 3)
    result = (math.pow(sequence[-1], 1 / 3) + d) ** 3
    return result


def sequence_proc(sequence: list) -> int:  # функція перевірки послідовності і результату результату
    if is_arithmetic(user_numbers):
        return is_arithmetic_res(user_numbers)
    if is_geometric(user_numbers):
        return is_geometric_res(user_numbers)
    if is_square_numbers(user_numbers):
        return is_square_numbers_res(user_numbers)
    if is_cubic_numbers(user_numbers):
        return is_cubic_numbers_res(user_numbers)
    return 'ERROR'

while True:
    user_numbers = input('enter numbers = ').strip().replace(',', ' ').split()
    user_numbers = list(map(int, user_numbers))
    print(f'Next item: {int(sequence_proc(user_numbers))}')


# Task 2
# Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел:
# 9009 = 91 × 99. Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.

#
# def palindrome(start: int, stop: int):
#     if start > stop:
#         stop, start = start, stop
#     res = []
#     for i in range(start, stop):
#         for j in range(start, stop):
#             tmp = str(i * j)
#             if tmp == tmp[::-1]:
#                 res.append((i * j, i, j))
#     return max(res)
# print(*palindrome(10, 100))
# print(*palindrome(10, 100))

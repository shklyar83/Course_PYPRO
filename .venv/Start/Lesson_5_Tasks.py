# Домашнє завдання (UA)
# Task 1
# Напишіть скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7.

# a = 1
# while a <= 100:
#     if a % 7 == 0:
#         print(a)
#     a += 1
# else:
#     print('finish')

# Task 2
# Напишіть скрипт для визначення суми цілих непарних чисел від 1 до 99 за допомогою оператора for.
# Використовуйте цілочисельні змінні sum і count.

# suma = 0
# count= 0
# for num in range(100):
#     if num // 2 != 0:
#         suma += num
#         count += 1
# print(suma)
# print(count)

# Task 3
# Напишіть скрипт, який виводить цілі числа від 1 до 200, використовуючи цикл while.
# В одному рядку необхідно виведити лише п’ять цілих чисел.
# Наприклад,
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# ...

# a = 1
# while a <= 200:
#     print(a, end = ' ')
#     if a % 5 == 0:
#         print(end = '\n')
#     a += 1

# Task 4
# Напишіть скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).

# n = int(input('enter number = '))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# Task 5
# Напишіть скрипт, який виводить на екран таблицю множення на 5.
# Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...
#
# for i in range(1, 10):
#     result = i * 5
#     print(f'{i} х 5 = {result}')

# Task 6
# Напишіть скрипт, який виводить на екран прямокутник із '*'. Висота і ширина прямокутника вводяться з клавіатури.
# Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5.
# *****
# *   *
# *   *
# *****

# a = int(input('ширина прямокутника = '))
# b = int(input('висота прямокутника = '))
# for i in range(b):
#     if i == 0 or i == b - 1:
#         print('*' * a)
#     else:
#         print('*' + ' ' * (a-2) + "*")

# Task 7
# Є список [0, 5, 2, 4, 7, 1, 3, 19].
# Напишіть скрипт для підрахунку непарних цифр у ньому.
#
# a = [0, 5, 2, 4, 7, 1, 3, 19, 23, 25, 27, 29]
# count = 0
# for i in a:
#     if i % 2 != 0:
#         count += 1
# print(f'Count ODD {count}')


# Task 8
# Створіть список випадкових чисел (розміром 4 елементи).
# Створіть другий список у два рази більше першого, де перші 4 елементи повинні дорівнювати елементам першого списку,
# а решта елементів - подвоєним значенням початкових.
# Наприклад,
# Було → [1,4,7,2]
# Стало → [1,4,7,2,2,8,14,4]
#
# import random
# first_list = [random.randint(1, 10) for i in range(4)]
# second_list = first_list + [num * 2 for num in first_list]
# print(f'first_list: {first_list}')
# print(f'second_list: {second_list}')

# Task 9
# Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
# Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.


# salary = [12500, 11000, 14500, 16000, 11500, 17000,
#           13500, 15500, 12000, 10000, 18700, 20000]
# avg = sum(salary) / len(salary)
#
# print(salary)
# print(f'average salary:  {avg:.2f}')


# Task 10
# Є матриця
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9, 10, 11, 12]
# [13, 14, 15, 16]
# Напишіть скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.

# matrix = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12],
#          [13, 14, 15, 16]]
#
# for i in range(4):
#     for j in range(4):
#         print(matrix[i][j], end=' ')
#     print(end = '\n')

# Task 11
# Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
# Список може бути довільною довжиною.

# x = [7,2,9,4]
# y = x[::-1]
# print(x)
# print(y)

# Task 12
# За допомогою циклів вивести на екран усі прості числа від 1 до 100.

# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# Task 13
# Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується з клавіатури (число непарне).
# У прикладі ширина дорівнює 5.
# *****
#  ***
#   *
#  ***
# *****

# n = int(input('n = '))
# stars = n  # start '*'
# spaces = 0  # start 'space'
#
# for i in range(n):
#     print(" " * spaces + "*" * stars)
#
#     if i < n // 2:  # до середини
#         spaces += 1
#         stars -= 2
#     else:  # після середини
#         spaces -= 1
#         stars += 2


#################  Рішення від Тренера

# Task 1
# i = 7
# while i < 100:
#     print(i)
#     i += 7
#
# for i in range(7, 100, 7):
#     print(i)
#
# # Task 2
# summa = 0
# count = 0
# for i in range(1, 100, 2):
#     summa += i
#     count += 1
# print(summa, count)
#
# print(sum(range(1, 100, 2)))
# print(len(range(1, 100, 2)))
#
# # Task 3
# i = 0
# while i <= 200:
#     print(i, end='\t')
#     i += 1
#     if i % 5 == 0:
#         print()
#
# i = 0
# while i <= 200:
#     if i % 5:
#         print(i, end='\t')
#     else:
#         print()
#     i += 1
#
# # Task 4
# n = int(input('n='))
# if n >= 0:
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
#     print(res)
# else:
#     print('Error')
#
# # Task 5
# for j in range(1, 11):
#     for i in range(1, 11):
#         print(f'{j} * {i} = {j * i}')
#     print('*' * 10)
#
# # Task 6
n, m = int(input('n=')), int(input('m='))
res = f"{'*' * n}\n" + f"*{' ' * (n - 2)}*\n" * (m - 2) + f"{'*' * n}\n"
print(res)
#
# # Task 7
# x = [0, 58573, 2, 4, 73, 11, 3, 19]
# count = 0
# for item in x:
#     tmp = [digit for digit in str(item) if int(digit) % 2]
#     count += len(tmp)
# print(count)
#
# # Task 8
# y = [1, 4, 7, 2]
# x = y + [item * 2 for item in y]
# print(y)
# print(x)
#
# # Task 9
# import random
# salary = [random.randint(1000, 10000000) for _ in range(12)]
# res = sum(salary) / len(salary)
# print(f'{res:.2f}')
#
# # Task 10
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# summa = 0
# for row in matrix:
#     summa += sum(row)
#     print(*row, sep='\t')
# print(summa)
#
# # Task 11
# x = [1, 2, 3, 4]
# print(x[::-1])
# print(x)
#
# x = [5, 6, 7, 8]
# x.reverse()
# print(x)
#
# for i in reversed(x):
#     print(i)
#
# # Task 12
# for n in range(1, 100):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n)
#
#
# n = int(input('n='))
# res = []
#
# space = 0
# for star in range(n, 0, -2):
#     res.append(f"{space * ' '}{star * '*'}")
#     space += 1
#
# res += res[-2::-1]
# print('\n'.join(res))
# print('\n'.join(res))

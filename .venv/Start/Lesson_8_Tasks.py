# Task 1
# Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.

#
# def suma(a, b, c):
#     y = a + b
#     concat = c + str(y)
#     return concat
# x, n, m = int(input('enter number x= ')), int(input('enter number n= ')), input('enter text= ')
# print(suma(x, n, m))

# Task 2
# Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.

# def rectangle(n, m):
#     res = f"{'*' * n}\n" + f"*{' ' * (n - 2)}*\n" * (m - 2) + f"{'*' * n}\n"
#     return res
# w, e = int(input('enter the width =')), int(input('enter the height ='))
# print(rectangle(w, e))

# Task 3
# Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».

# # створюємо список
# x = [i for i in range(1, 100)]
#
# # створюємо функцію
# def search(num):
#     res = x.index(num) if num in x else -1
#     return res
#
# # викликаємо функцію пошуку
# while True:
#     user_num = int(input('enter your number for search = '))
#     print(search(user_num))

# Task 4
# Напишіть функцію, яка поверне кількість слів у текстовому рядку.
#
# def count_words(text):
#     res = len(text.split())
#     return res
# user_text = input('enter your text ')
# print(f'count words in your text = {count_words(user_text)}')

# #
# Task 5
# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents
#
#Створюємо словники для одиниць, десятків, сотень, тисяч
# vocabulary_units = {
#     0: "",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
#     10: "ten",
#     11: "eleven",
#     12: "twelve",
#     13: "thirteen",
#     14: "fourteen",
#     15: "fifteen",
#     16: "sixteen",
#     17: "seventeen",
#     18: "eighteen",
#     19: "nineteen",
#     20: "twenty"}
# vocabulary_tens_of = {
#     3: "thirty",
#     4: "forty",
#     5: "fifty",
#     6: "sixty",
#     7: "seventy",
#     8: "eighty",
#     9: "ninety"}
# vocabulary_hundreds = {
#     1: "one hundred",
#     2: "two hundred",
#     3: "three hundred",
#     4: "four hundred",
#     5: "five hundred",
#     6: "six hundred",
#     7: "seven hundred",
#     8: "eight hundred",
#     9: "nine hundred"}
# vocabulary_thousands = {
#     1: "one thousand",
#     2: "two thousand",
#     3: "three thousand",
#     4: "four thousand",
#     5: "five thousand",
#     6: "six thousand",
#     7: "seven thousand",
#     8: "eight thousand",
#     9: "nine thousand"}

# функція для визначення цілих значень доларів (максимум до 10000)
# def doll_calc(a):
#     money_rozr = str(money).split('.')
#     money_rozr = int(money_rozr[0])
#     if money_rozr <=20:
#         return f'{vocabulary_units[money_rozr]} dollars' # одиниці
#     elif money_rozr < 100:
#         a = money_rozr // 10 # десятки
#         b = money_rozr % 10 # одиниці
#         return f'{vocabulary_tens_of[a]} {vocabulary_units[b]} dollars'
#     elif money_rozr < 1000:
#         aa = money_rozr // 100 # сотні
#         bb = money_rozr // 10 - money_rozr // 100 * 10 # десятки
#         cc = money_rozr % 10 # одиниці
#         return f'{vocabulary_hundreds[aa]} {vocabulary_tens_of[bb]} {vocabulary_units[cc]} dollars'
#     elif money_rozr < 10000:
#         www = money_rozr // 1000 # тисячі
#         aaa = money_rozr // 100  - money_rozr // 1000 * 10 # сотні
#         bbb = money_rozr // 10 - money_rozr // 100 * 10  # десятки
#         ccc = money_rozr % 10  # одиниці
#         return f'{vocabulary_thousands[www]} {vocabulary_hundreds[aaa]} \
#         {vocabulary_tens_of[bbb]} {vocabulary_units[ccc]} dollars'
#
# # функція для визначення центів
# def cents_calc(a):
#     money_rozr = str(a).split('.')
#     money_rozr = int(money_rozr[1])
#     if money_rozr <=20:
#         return f'{vocabulary_units[money_rozr]} cents'
#     elif money_rozr < 100:
#         a = money_rozr // 10
#         b = money_rozr % 10
#         return f'{vocabulary_tens_of[a]} {vocabulary_units[b]} cents'
#     # return money_rozr
#
# money = float(input('enter the amount of money = '))
# while 0 < money < 10000:
#     print(f'{doll_calc(money)} {cents_calc(money)}', end='\n')
# else:
#     print('error')

#Task 6
# Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22

# def roman_to_decimal(roman_numeral):
#     roman_dict = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#
#     decimal_num = 0
#     previous_value = 0
#
#     for char in reversed(roman_numeral):
#         value = roman_dict[char]
#
#         if value >= previous_value:
#             decimal_num += value
#         else:
#             decimal_num -= value
#
#         previous_value = value
#
#     return decimal_num
#
#
# roman_numeral = input('enter roman number = ')
# decimal_num = roman_to_decimal(roman_numeral)
# print(decimal_num)
# print(decimal_num)


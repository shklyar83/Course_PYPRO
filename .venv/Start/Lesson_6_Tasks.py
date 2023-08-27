# Task 1
# Напишіть скрипт, який порахує скільки літер «b» у введеному рядку тексту.
#
#
# text = input('enter your message ')
# count = text.count('b')
# print(f' count of letters "b" {count}')


# Task 2
# Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки введеного ім'я на валідність
# (мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно починатися з великої літери,
# за якою повинні йти маленькі).

# import string
#
# text = input('enter your message ')
# for i in string.punctuation:
#     while i in text:
#         text = text.replace(i, '')
# if any(char.isdigit() for char in text):
#     print(f'Name {text} isn`t correct')
# elif text.istitle():
#     print(f'Name {text} is correct')
# else:
#     print(f'Name {text} isn`t correct')

# Task 3
# Напишіть скрипт, який обчислює суму всіх кодів символів рядка.

# text = input('enter your message= ')
# suma = 0
# for c in text:
#     c = ord(c)
#     suma += c
# print(suma)


# Task 4
# Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути 2 знаки після коми,
# у другому 3 і так далі.
#
# import math
#
# for i in range(2, 12):
#     pi_value = round(math.pi, i)
#     print(pi_value)


# Task 5
# Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
#
# text = input('enter your message= ')
# words = text.split()
# longest_word = ""
#
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word
#
# print(longest_word)

# Task 6
# Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери).
# Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту.
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# ititititit - Вовочка писав слово - "it"
# catcatcatcat - Вовочка писав слово - "cat"
def word_detect(text: str):
    for i in range(1, len(text) // 2 + 1):
        word = text[:i]
        if text.count(word) * len(word) == len(text):
            return word
    return None


print(word_detect('pythonpython1'))
print(word_detect('pythonpython1'))
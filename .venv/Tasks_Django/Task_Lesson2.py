# Task 1
# Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, 
# що складаються з однієї літери R, за якою слідує одна або більше літер b, 
# за якою одна r. Враховувати верхній та нижній регістр.

# import re

# text = input('enter your text')
# pattern = r'[Rr]b+[Rr]'
# matches = re.findall(pattern, text)
# print(matches)


# Task 2
# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).

# import re

# def card_validator(number):
#     pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
#     if re.match(pattern, number):
#         return f'Your card is active'
#     else:
#         return f'Invalid number'
 
# num_card = card_validator(input('enter card number: '))
# print(num_card)


# Task 3
# Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

# import re

# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9]+[a-zA-Z0-9_-]*@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    
#     if re.match(pattern, email):
#         if email.count('-') > 1 or (email.count('-') == 1 and email[0] == '-'):
#             return f'incorrect email'
#         return 'e-mail accept'
#     else:
#         return 'incorrect email'

# email_input = input('Enter an email address: ')

# print(validate_email(email_input))


# Task 4
# Напишіть функцію, яка перевіряє правильність логіну. 
# Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.


# import re

# def validate_login(login):
#     pattern = r'^[a-zA-Z0-9]{2,10}$'
#     if re.match(pattern, login):
#         return 'login accept'
#     else:
#         return 'incorrect login'

# login_input = input('Enter your login: ')

# print(validate_login(login_input))

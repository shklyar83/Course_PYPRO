# Task 1
# Напишіть програму, яка приймає рядок тексту і повертає словник,
# де ключами є слова, а значеннями - кількість входжень кожного слова в тексті.
#
# text = input('enter text = ')
# words = text.split()
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# for word, count in word_count.items():
#     print(f'{word}: {count}')



# Task 2
# Реалізуйте простий перекладач, який використовує словник для збереження пар слів.
# Користувач може вводити слово, а програма повертає його переклад.
# У цьому випадку, словник може використовуватись для збереження відповідностей між словами у різних мовах.

# Приклад:

# translations = {
#     'hello': 'привіт',
#     'goodbye': 'до побачення',
#     'cat': 'кіт',
#     'dog': 'собака'}
# word = input('enter english word = ')
# print(translations[word])


# Task 3
# Реалізуйте просту програму для збереження контактів.
# Кожен контакт може мати ім"я як ключ та номер телефону як значення. Дозвольте користувачу додавати нові контакти,
# видаляти існуючі та отримувати номер телефону за ім'ям.


#
options = {1: 'Add contact', 2: 'Delete contact', 3: 'Get phone number by Name', 4: 'Exit'}

contacts = {}

while True:
    for key, value in options.items():
        print(f'{key}. {value}')

    choice = input('Enter you function: ')

    if choice == '1':
        name = input('Enter contact name: ')
        phone = input('Enter phone number: ')
        contacts[name] = phone
        print('Contact added')

    elif choice == '2':
        name = input('Enter contact name for delete: ')
        if name in contacts:
            del contacts[name]
            print('Contact deleted.')
        else:
            print('Contact error.')

    elif choice == '3':
        name = input('Enter phone number for extract name: ')
        if name in contacts:
            phone = contacts[name]
            print(f'Phone number {name}: {phone}')
        else:
            print('Contact error.')

    elif choice == '4':
        print('Finish')
        break

    else:
        print('Error, try again')
        print('Error, try again')
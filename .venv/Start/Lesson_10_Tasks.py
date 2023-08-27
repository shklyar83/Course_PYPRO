# Task 1
# Необхідно підготувати звіт про витрати членів родини на новорічні свята.
# Дані по витратам наведено у файлі hw_10_test.txt у форматі:
# Номер за переліком Прізвище та ім'я (або ім'я) Сума Категорія товару
# Звіт повинен включати наступне:
# 1. Яка загальна сума витрат по кожній категорії товарів?
# 2. Скільки грошей витратив кожен член родини?
# 3. Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини?

# Функція 1. Загальна сума витрат по кожній категорії товарів


def total_expenses_by_categories(file_name: str):
    category_expenses = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            cost = float(parts[-2].rstrip('$'))
            category = parts[-1]
            if category in category_expenses:
                category_expenses[category] += cost
            else:
                category_expenses[category] = cost
    result = ''
    for category, expense in category_expenses.items():
        result += f'{category}: {expense:.2f}$\n'
    return result


# Функція 2 Скільки грошей витратив кожен член родини


def total_expenses_by_family_members(file_name: str):
    family_expenses = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            member = ' '.join(parts[1:-2])
            cost = float(parts[-2].rstrip('$'))
            if member in family_expenses:
                family_expenses[member] += cost
            else:
                family_expenses[member] = cost
    result = ''
    for member, expense in family_expenses.items():
        result += f'{member}: {expense:.2f}$\n'
    return result


# Функція 3 Яку кількість покупок та на яку загальну суму зробив введений користувачем через input член родини


def total_expenses_by_one_member(file_name: str, member_name: str):
    count = 0
    sum_expenses = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            member = ' '.join(parts[1:-2])
            cost = float(parts[-2].rstrip('$'))
            if member.lower() == member_name.lower():
                count += 1
                sum_expenses += cost
    return f'count expenses: {count}; sum expenses: {sum_expenses:.2f}$'

# дивимось звіт на вибір користувача
menu = {1: 'Report by category', 2: 'Report by Users', 3: 'Report by one user'}
for key, value in menu.items():
    print(f'{key}. {value}')
user_function = int(input('Select number of Report\n-> '))
if user_function == 1:
    print(f'Report by category:\n{total_expenses_by_categories("hw_10_test.txt")}')
elif user_function == 2:
    print(f'Report by Users:\n{total_expenses_by_family_members("hw_10_test.txt")}')
elif user_function == 3:
    name = input('Enter user name\n-> ').lower()
    user_report = total_expenses_by_one_member('hw_10_test.txt', name)
    print(f'Report by User {user_report}')
    # print(f'Report by User {name}:\n{total_expenses_by_one_member("hw_10_test.txt", "{name}")}')
else:
    print('there is no such report')
    print('there is no such report')


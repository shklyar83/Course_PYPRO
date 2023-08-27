# Task 1
# Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.

def geometric_progression(a, r):
    term = a
    while True:
        yield term
        term *= r

a = 2
r = 3

gp_generator = geometric_progression(a, r)

for i in range(5):
    print(next(gp_generator))


# Task 2
# Реалізуйте свій аналог генераторної функції range().

def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start

    while start < stop:
        yield start
        start += step

for num in my_range(1, 10, 2):
    print(num)

# Task 3
# Напишіть генераторну функцію, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(limit):
    for num in range(2, limit):
        if is_prime(num):
            yield num


for prime in prime_generator(50):
    print(prime, end=' ')


# Task 4
# Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2 до вказаної вами величини.

limit = 14  # Задана величина
cubes_list = [x ** 3 for x in range(5, limit + 1)]

print(cubes_list)


# Task 5
# Реалізуйте генераторну функцію, яка повертатиме елементи послідовності чисел Фібоначчі.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()

for _ in range(10):
    print(next(fibonacci))

# Task 6
# Реалізуйте генераторну функцію для генерації послідовності дат. Початкова та кінцеві дати мають бути задані параметрами цієї функції.

from datetime import datetime, timedelta

def date_range_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 10)

date_range = date_range_generator(start_date, end_date)

for date in date_range:
    print(date.strftime('%Y-%m-%d'))

# Домашнє завдання
# Task 1
# Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача. Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовностю. Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.

def custom_sequence_generator(first_value, sequence_function, num_elements):
    current_value = first_value
    generated_elements = 0

    while generated_elements < num_elements:
        yield current_value
        current_value = sequence_function(current_value)
        generated_elements += 1


def custom_sequence_rule(value):
    return value * 2 + 1

first_value = 1
num_elements = 5

sequence_generator = custom_sequence_generator(first_value, custom_sequence_rule, num_elements)

for value in sequence_generator:
    print(value)

# Task 2
# Використовуючи замикання, реалізуйте такий прийом програмування як Мемоізація - https://en.wikipedia.org/wiki/Memoization .
# Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі. Порівняйте швидкість виконання із просто рекурсивним підходом.

def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper

@memoize
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is {result}")

# Task 3
# Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.
def apply_function_and_sum(numbers, user_function):
    result = sum(user_function(number) for number in numbers)
    return result

def square(x):
    return x ** 2


def reciprocal(x):
    return 1 / x

numbers = [1, 2, 3, 4, 5]

sum_of_squares = apply_function_and_sum(numbers, square)
print(f"Sum of squares: {sum_of_squares}")

sum_of_reciprocals = apply_function_and_sum(numbers, reciprocal)
print(f"Sum of reciprocals: {sum_of_reciprocals}")




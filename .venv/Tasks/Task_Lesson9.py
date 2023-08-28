# Task 1
# Напишіть декоратор, який виконує певну дію перед і після виконанням функції.

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# @my_decorator
# def my_function(x, y, c):
#     return x * y + c

# result = my_function(5, 7, 8)
# print(result)


# Task 2
# Напишіть декоратор, який зберігає результати обчислення функції у файл для подальшого використання.

# def save_result(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         with open(".venv\\Tasks\\result.txt", "w") as file:
#             file.write(str(result))
#         return result
#     return wrapper

# @save_result
# def multiply(x, y):
#     return x * y

# result = multiply(5, 7)
# print(result)

# Task 3
# Напишіть декоратор, який перехоплює та обробляє виключення, що виникають у функції.

# def handle_exceptions(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(f"Error: {e}")
#     return wrapper

# @handle_exceptions
# def divide(a, b):
#     return a / b

# divide(5, 0)

# Task 4
# Напишіть декоратор, який вимірює час виконання функції.

# import time

# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"function execution time: {execution_time:.4f}")
#         return result
#     return wrapper

# @measure_time
# def some_function():
#     time.sleep(2)
# some_function()


# Task 5
# Напишіть декоратор, який логує аргументи та результати функції.


# def log_arguments_results(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"args:{args}, result {result}")
#         return result
#     return wrapper

# @log_arguments_results
# def add_numbers(a, b):
#     return a + b
# add_numbers(3, 4)

# Task 6
# Напишіть декоратор, який обмежує кількість викликів функції.

# def limit_calls(max_calls):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if wrapper.calls < max_calls:
#                 wrapper.calls += 1
#                 return func(*args, **kwargs)
#             else:
#                 print(f"call limit has expired, max limit - {max_calls}")
#         wrapper.calls = 0
#         return wrapper
#     return decorator

# @limit_calls(3)
# def some_function():
#     print('add func')

# some_function()
# some_function()
# some_function()
# some_function()
# some_function()

# Task 7
# Напишіть декоратор, який кешує результати обчислення функції і повертає їх з кешу при наступних викликах з тими самими аргументами.

# def cache_results(func):
#     cache = {}
#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             result = func(*args)
#             cache[args] = result
#             return result
#     return wrapper

# @cache_results
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))  
# print(fibonacci(10))





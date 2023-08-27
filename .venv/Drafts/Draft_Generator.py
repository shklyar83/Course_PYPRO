OST, [08.08.2023 20:13]
def gen_numbers(start, stop, step=1):
    while start < stop:
        yield start
        start += step


for item in gen_numbers(2, 20, 3):
    print(item)

OST, [08.08.2023 20:38]
def exponent_gen(n):
    index = 0
    exponent = 2
    while index < n:
        tmp = yield index ** exponent
        if tmp:
            exponent = tmp
        index += 1


x = exponent_gen(10)
for item in x:
    print(item)
    if item > 25:
        tmp = x.send(3)
        print(tmp)

OST, [08.08.2023 21:00]
import timeit

# Var 1
stmt_1 = """
with open('test.txt', encoding='utf-8') as file:
    data = file.readlines()
    summa = 0
    for item in data:
        if item.strip().isdigit():
            summa += int(item)
"""

# Var 2
stmt_2 = """
with open('test.txt', encoding='utf-8') as file:
    summa = 0
    for item in file:
        if item.strip().isdigit():
            summa += int(item)
"""


# Var 3
stmt_3 = """
with open('test.txt', encoding='utf-8') as file:
    res = (int(item) for item in file if item.strip().isdigit())
    summa = sum(res)
"""


print(timeit.timeit(stmt=stmt_1, number=10))
print(timeit.timeit(stmt=stmt_2, number=10))
print(timeit.timeit(stmt=stmt_3, number=10))
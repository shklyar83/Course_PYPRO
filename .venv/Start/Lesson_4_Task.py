# Task 1
# Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
# Примітка: щасливим квитком називається число, у якому, при парній кількості цифр, сума цифр його лівої половини дорівнює сумі цифр його правої половини.
# Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.

# number = input('Enter your ticket number ')
# number = list(map(int, number))
# part_1 = number[ : len(number) // 2 : ]
# part_2 = number[len(number) // 2 :  : ]
# if sum(part_1) == sum(part_2):
#     print('Congratulations, your ticket is lucky :-)')
# else:
#     print ('Sorry, try again :-(')

# Task 2
# З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
# Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
# Наприклад, це числа 143341, 5555, 7117 і т.д.

# number = input('Enter number ')
# if number == number[ :  : -1]:
#      print('Паліндром')
# else:
#      print ('Не паліндром')

# Task 3
# Дано коло з центром на початку координат та радіусом 4.
# Користувач вводить з клавіатури координати точки x та y.
# Написати програму, яка визначить, лежить ця точка всередині кола чи ні.
#
# Формула: x^2 + y^2 <= r^2

# R = 4
# x = float(input('Enter the coordinates of point X='))
# y = float(input('Enter the coordinates of point Y='))
#
# if x**2 +y**2 <= R**2:
#     print('The point is on the circle')
# else:
#     print('The point isn`t on the circle')
#     print('The point isn`t on the circle')
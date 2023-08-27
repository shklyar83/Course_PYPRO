# Task 1
# Створіть клас "Правильна Дріб" і реалізуйте методи порівняння, додавання, віднімання та множення
# для екземплярів цього класу.

import math


class Rational:

    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError('Value "a" must be int')
        if not isinstance(b, int):
            raise TypeError('Value "b" must be int')
        if b == 0:
            raise ZeroDivisionError('division by 0 is impossible')
        self.__a = a
        self.__b = b

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return Rational(self.__a * other.__a, self.__b * other.__b)

    def __eq__(self, other):
        tmp = math.gcd(self.__a, self.__b)
        self.__a //= tmp
        self.__b //= tmp

        tmp = math.gcd(other.__a, other.__b)
        other.__a //= tmp
        other.__b //= tmp

        return self.__a == other.__a and self.__b == other.__b

    def __str__(self):
        sign = '' if self.__a * self.__b >= 0 else '-'
        a, b = abs(self.__a), abs(self.__b)
        tmp = math.gcd(a, b)
        a //= tmp
        b //= tmp
        if a == b:
            return f'{sign}1'
        if a > b:
            return f'{sign} {a // b} {a % b}/{b}'
        return f'{sign} {a}/{b}'


x = Rational(5, 7)
y = Rational(1, -2)

res = x * y
print(x, y, res, sep='\n')
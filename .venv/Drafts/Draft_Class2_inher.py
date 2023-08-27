# И еще несколько примеров применения наследования:

class Account(object):
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFundsError
        self.balance -= amount

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)

class SavingsAccount(Account):
    def __init__(self, account_number, balance, owner, interest_rate):
        super().__init__(account_number, balance, owner)
        self.interest_rate = interest_rate

    def accrue_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance, owner, monthly_fee):
        super().__init__(account_number, balance, owner)
        self.monthly_fee = monthly_fee

    def deduct_monthly_fee(self):
        self.balance -= self.monthly_fee

my_savings_account = SavingsAccount("1234567890", 1000, "John Doe", 0.05)
my_checking_account = CheckingAccount("9876543210", 500, "Jane Doe", 10)

my_savings_account.deposit(100)
my_savings_account.accrue_interest()
print(my_savings_account.balance)

my_checking_account.withdraw(20)
my_checking_account.deduct_monthly_fee()
print(my_checking_account.balance)

В этом примере класс Account является родительским классом, а классы SavingsAccount и CheckingAccount являются
дочерними классами. Класс Account определяет общие методы deposit(), withdraw() и transfer(),
которые могут использоваться всеми типами счетов. Классы SavingsAccount и CheckingAccount переопределяют метод
accrue_interest() и deduct_monthly_fee(), чтобы они соответствовали их собственным уникальным потребностям.


class Shape:
    def __init__(self, color):
        self.__color = color

    def color(self):
        return self.__color

    def area(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    def area(self):
        return self.a * self.a


class Rectangle(Shape):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, color, r):
        super().__init__(color)
        self.r = r

    def area(self):
        import math
        return math.pi * self.r ** 2

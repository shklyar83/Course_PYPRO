#1
class Product:

    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price

    def __delattr__(self, item):
        ...

    def __setattr__(self, key: str, value):
        if key == 'price':
            if not isinstance(value, int | float):
                raise TypeError()
            if value <= 0:
                raise ValueError()
        elif key == 'description':
            ...
        elif key == 'title':
            if not isinstance(value, str):
                raise TypeError()
        self.__dict__[key] = value

    def __getattribute__(self, item):
        try:
            return object.__getattribute__(self, item)
        except:
            if item == 'size':
                return 'Not defined for this product'
            if item == 'color':
                return 'red'
            return None

    def __str__(self):
        return f'{self.title} x {self.price}'
    

#2
from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for quantity, price in zip(self.quantities, self.prices):
            total += quantity * price
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        ...


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class USDTPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, order):
        print("Processing USDT payment type")
        print(f"Verifying email: {self.email}")
        order.status = "paid"


def payment(processor: PaymentProcessor, order):
    processor.pay(order)


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = USDTPaymentProcessor("test@gmail.com")
payment(processor, order)


product = Product('apple', 'very', 23)
product.price = 24
del product.price
print(product)
print(product.size)
print(product.color)
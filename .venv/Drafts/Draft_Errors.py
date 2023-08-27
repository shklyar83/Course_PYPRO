# #1
class Student:

    def __init__(self, name):
        self.name = name


class GroupLimitException(Exception):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def __str__(self):
        return f'Group limit student exceeded. Max limit is {self.limit}.'


class Group:
    def __init__(self, limit=10):
        self.students = []
        self.limit = limit

    def add_student(self, student: Student):
        if len(self.students) >= self.limit:
            raise GroupLimitException(self.limit)
        self.students.append(student)


st1 = Student('Ivan 1')
st2 = Student('Ivan 2')

gr = Group(1)
try:
    gr.add_student(st1)
    gr.add_student(st2)
except GroupLimitException as error:
    print(error)


# #2
class NegativePriceError(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class Product:

    def __init__(self, name, price):
        if price <= 0:
            raise NegativePriceError('Price must be positive number, but negative got!')

        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price:.2f}'


class Cart:

    def __init__(self):
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity=1):
        if not isinstance(product, Product):
            raise TypeError('Error in Product datatype')
        if not isinstance(quantity, int | float):
            raise TypeError('Error in quantity of Product')
        if quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got.')
        self.__products.append(product)
        self.__quantities.append(quantity)

    def total(self):
        summa = 0
        for item, quantity in zip(self.__products, self.__quantities):
            summa += item.price * quantity
        return summa

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        res = ''
        for item, quantity in zip(self.__products, self.__quantities):
            res += f'{item} x {quantity} = {item.price * quantity} UAH\n'

        res += f'Total = {self.total()} UAH'
        return res


if __name__ == '__main__':
    try:
        pr1 = Product('apple', 30)
        pr2 = Product('apple lux', 60)
        pr3 = Product('banana', 50)
        pr4 = Product('orange', 40)

        cart_1 = Cart()
        cart_1.add_product(pr1, 2)
        cart_1.add_product(pr4)
        cart_1.add_product(pr3, 3)

        print(cart_1)
    except NegativePriceError as error:
        print(error)
    except TypeError as error:
        print(error)
    except:
        print('Error')
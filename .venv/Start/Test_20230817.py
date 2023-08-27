import logging
logger = logging.getLogger('add_processing')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Supermarket_logs.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class IncorrectDiscount(Exception):
    """Ініціалізація помилки у разі введення розміру дисконту не в межах 0-100%"""

    def __init__(self, discount_size: int):
        super().__init__()
        self.discount_size = discount_size

    def __str__(self):
        return f'The Discount {self.discount_size}% can range from 0 to 100%'


class IncorrectPrice(Exception):
    """Ініціалізація помилки у разі введення ціни <= 0"""

    def __init__(self, price):
        super().__init__()
        self.price = price

    def __str__(self):
        return f'The price {self.price} can`t be less than or equal to zero'


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price:.2f}'


class CartIter: #my
    def __init__(self, products, quantities):
        self.__products = products
        self.__quantities = quantities
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__products):
            self.index += 1
            return self.__products[self.index - 1], self.__quantities[self.index - 1]
        raise StopIteration()

# class CartIter:
#     def __init__(self, products, quantities):
#         self.__products = products
#         self.__quantities = quantities
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.__products):
#             self.index += 1
#             return self.__products[self.index - 1], self.__quantities[self.index - 1]
#         raise StopIteration()


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
        if product.price <= 0:
            raise IncorrectPrice(product.price)
        self.__products.append(product)
        self.__quantities.append(quantity)

    def total(self):
        summa = 0
        for item, quantity in zip(self.__products, self.__quantities):
            summa += item.price * quantity
        return summa

    def __iter__(self):
        return CartIter(self.__products, self.__quantities)

    def process(self):
        logger.info(f'{self.__products}, {self.__quantities}')

    def __str__(self):
        res = ''
        for item, quantity in zip(self.__products, self.__quantities):
            res += f'{item} x {quantity} = {item.price * quantity} UAH\n'

        res += f'Total = {self.total()} UAH'
        return res


if __name__ == '__main__':
    pr1 = Product('apple', 20)
    pr2 = Product('apple lux', 60)
    pr3 = Product('banana', 50)
    pr4 = Product('orange', 40)

    cart = Cart()
    cart.add_product(pr1, 2)
    cart.add_product(pr4, 40)
    cart.add_product(pr3, 3)

    cart.process()
    print(cart)
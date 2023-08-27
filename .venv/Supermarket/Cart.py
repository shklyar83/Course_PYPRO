import Supermarket.Products as modprod
import Errors as moderr
import logging

logger = logging.getLogger('add_processing')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Supermarket_logs.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class CartIter:
    def __init__(self, product, quantity):
        self.__products = product
        self.__quantities = quantity
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__products):
            self.index += 1
            return self.__products[self.index - 1], self.__quantities[self.index - 1]
        raise StopIteration()


class Cart:

    def __init__(self):
        self.__products = []
        self.__quantities = []

    def add_product(self, product: modprod.Product, quantity=1):
        if not isinstance(product, modprod.Product):
            raise TypeError('Error in Product datatype')
        if not isinstance(quantity, int | float):
            raise TypeError('Error in quantity of Product')
        if quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got.')
        if product.price <= 0:
            raise moderr.IncorrectPrice(product.price)
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



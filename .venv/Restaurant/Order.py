import Restaurant.Menu
import Discount
import logging

logger = logging.getLogger('add_processing')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('Restaurant_logs.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class OrderIter:

    def __init__(self, dishes, quantity):
        self.__dishes = dishes
        self.__quantity = quantity
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__dishes):
            self.index += 1
            return self.__dishes[self.index - 1], self.__quantity[self.index - 1]
        raise StopIteration()


class Order:
    """ Замовлення """

    def __init__(self):
        self.__dishes = []
        self.__quantity = []

    def add_dish(self, dish: Restaurant.Menu.Dish, quantity=1):
        if not isinstance(dish, Restaurant.Menu.Dish):
            raise TypeError('Error in Dish datatype')
        if not isinstance(quantity, int):
            raise TypeError('Error in quantity of dishes')
        if quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got.')
        self.__dishes.append(dish)
        self.__quantity.append(quantity)

    def total_price(self, discount: Restaurant.Menu.Discount):
        suma = 0
        for item, quantity in zip(self.__dishes, self.__quantity):
            suma += item.price * quantity
        return suma * discount.discount()

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__dishes[item]
        if isinstance(item, slice):
            return self.__dishes[item]
        raise TypeError('Error in datatype')

    def __len__(self):
        return len(self.__dishes)

    def __iter__(self):
        return OrderIter(self.__dishes, self.__quantity)

    def process(self):
        logger.info(f'{self.__dishes}, {self.__quantity}')

    def __str__(self):
        result = ''
        for dish, quantity in zip(self.__dishes, self.__quantity):
            result += f'{dish} х {quantity} = {quantity * dish.price} UAH\n'
        return result

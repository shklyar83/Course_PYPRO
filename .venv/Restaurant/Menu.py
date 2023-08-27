import Errors
import logging

logger = logging.getLogger('add_processing')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Restaurant_logs.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Dish:
    """Список страв в меню"""

    def __init__(self, dish_name: str, description: str, dish_price: int | float):
        self.name = dish_name
        self.description = description
        self.price = dish_price

    def __str__(self):
        return f'{self.name}: {self.price}'


class Category:
    """Категорії страв у меню"""

    def __init__(self, name: str):
        self.category_name = name
        self.dishes = []

    def add_dish(self, dish: Dish):
        if not isinstance(dish, Dish):
            raise TypeError('Error in Dish datatype')
        if dish.price <= 0:
            raise Errors.IncorrectPrice(dish.price)
        self.dishes.append(dish)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.dishes[item]
        if isinstance(item, slice):
            return self.dishes[item]
        raise TypeError('Error in datatype')

    def __len__(self):
        return len(self.dishes)

    def process(self):
        logger.info(f'{self.category_name}, {self.dishes}')

    def __str__(self):
        return f'{self.category_name}\n' + '\n'.join(map(str, self.dishes))


class Menu:
    """Наприклад назва меню у ресторані"""

    def __init__(self):
        self.categories = []

    def add_category(self, category: Category):
        if not isinstance(category, Category):
            raise TypeError('Error in Category datatype')
        self.categories.append(category)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.categories[item]
        if isinstance(item, slice):
            return self.categories[item]
        raise TypeError('Error in datatype')

    def __len__(self):
        return len(self.categories)

    def process(self):
        logger.info(f'{self.categories}')

    def __str__(self):
        return '\n'.join(map(str, self.categories))
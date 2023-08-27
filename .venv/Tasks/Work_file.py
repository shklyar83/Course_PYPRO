class Product:

    def __init__(self, title, description, price):
        self.__price = price

    def __str__(self):
        ...

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise TypeError()
        self.__price = value

    @price.deleter
    def price(self):
        ...

prod = Product()

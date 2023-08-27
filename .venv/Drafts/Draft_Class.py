class Product:

    def __init__(self, name, price):
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

    def __str__(self):
        res = ''
        for item, quantity in zip(self.__products, self.__quantities):
            res += f'{item} x {quantity} = {item.price * quantity} UAH\n'

        res += f'Total = {self.total()} UAH'
        return res


if __name__ == '__main__':
    pr1 = Product('apple', 30)
    pr2 = Product('apple lux', 60)
    pr3 = Product('banana', 50)
    pr4 = Product('orange', 40)

    cart = Cart()
    cart.add_product(pr1, 2)
    cart.add_product(pr4)
    cart.add_product(pr3, 3)

    print(cart)
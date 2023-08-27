OST, [08.08.2023 19:58]
class OrderIter:
    def __init__(self, products, quantities, prices):
        self.__products = products
        self.__quantities = quantities
        self.__prices = prices
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.__products):
            self.index += 1
            return self.__products[self.index - 1],\
                   self.__quantities[self.index - 1],\
                   self.__prices[self.index - 1]

        raise StopIteration()


class Order:

    def __init__(self):
        self.__products = []
        self.__quantities = []
        self.__prices = []

    def add(self, product, quantity, price):
        self.__products.append(product)
        self.__quantities.append(quantity)
        self.__prices.append(price)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__products[item]

    def __iter__(self):
        return OrderIter(self.__products, self.__quantities, self.__prices)

    def __str__(self):
        res = ''
        for product, quantity, price in self:
            res += f'{product}: {quantity} x {price} = {quantity * price}\n'
        return res


x = Order()
x.add('apple', 2, 20)
x.add('TV', 3, 30)
x.add('smartphone', 4, 40)
x.add('cable', 5, 50)
for item in x:
    print(*item)

print(x)

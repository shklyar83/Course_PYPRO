#1
class Student:
    def __init__(self, name: str, surname: str):

        if not isinstance(surname, str):
            raise TypeError()
        if not surname:
            raise ValueError()
        self.name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name.upper()

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError()
        if not value:
            raise ValueError()
        self.__name = value

    @name.deleter
    def name(self):
        ...

    def __str__(self):
        return f'{self.surname} {self.name}'


student = Student('Ivan', 'Ivanov')
del student.name
print(student.name)


#2
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


product = Product('apple', 'very', 23)
product.price = 24
del product.price
print(product)
print(product.size)
print(product.color)

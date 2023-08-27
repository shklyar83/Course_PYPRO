import Errors


class Discount:
    """ Батьківський клас дисконту """

    def __init__(self, discount_size=0):
        self.discount_size = discount_size

    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    """Класична карта"""

    def __init__(self, discount_size=5):
        super().__init__(discount_size)

    def discount(self):
        if self.discount_size > 100 or self.discount_size <= 0:
            raise Errors.IncorrectDiscount(self.discount_size)
        return 1 - self.discount_size / 100


class SilverDiscount(Discount):
    """Срібна карта"""

    def __init__(self, discount_size=10):
        super().__init__(discount_size)

    def discount(self):
        if self.discount_size > 100 or self.discount_size <= 0:
            raise Errors.IncorrectDiscount(self.discount_size)
        return 1 - self.discount_size / 100


class GoldDiscount(Discount):
    """Золота карта"""

    def __init__(self, discount_size=20):
        super().__init__(discount_size)

    def discount(self):
        if self.discount_size > 100 or self.discount_size <= 0:
            raise Errors.IncorrectDiscount(self.discount_size)
        return 1 - self.discount_size / 100
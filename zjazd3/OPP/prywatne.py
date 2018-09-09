class Product:
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self.price = price
        self._discount = 0

    @property
    def name(self):
        return self._name

    @property
    def discount_price(self):
        '''coś tam działa'''
        return self.price * (1 - self._discount)

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) == float or type(value) == int:
            if 0 <= value <= 0.3:
                self._discount = value

    @discount.deleter
    def discount(self):
        self._discount = 0


pr1 = Product(1, 'bułka', 10)

print(pr1.price)
print(pr1._id)
print(pr1.name)
pr1.name = 'ala ma kota'
print(pr1._name)

pr1.discount = 0.3
print(pr1.discount)
print(pr1.discount_price)
help(Product.discount_price)
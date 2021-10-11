class FruitType:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def __str__(self):
        return '{} : {} €/Kg'.format(self.name, self.price)
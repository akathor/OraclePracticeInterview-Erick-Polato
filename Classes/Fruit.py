class Fruit:
    def __init__(self, FruitType, weight):
        self.FruitType = FruitType
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_type(self):
        return self.FruitType.get_name()

    def get_price(self):
        price = self.weight * self.FruitType.get_price() / 1000
        return price

    def __str__(self):
        return '{} {}g at {} €/Kg'.format(self.FruitType.name, self.weight, self.FruitType.get_price())
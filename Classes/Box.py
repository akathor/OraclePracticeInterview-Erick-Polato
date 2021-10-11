class Box:
    def __init__(self):
        self.fruits = []
        self.weight = 0
        self.price = 0

    def insert_fruit(self, fruit):
        self.fruits.append(fruit)
        self.weight += fruit.get_weight()
        self.price += fruit.get_price()

    def get_box_weight(self):
        return self.weight

    def get_box_price(self):
        return round(self.price, 2)

    def get_box_fruits(self):
        return self.fruits

    def add_fee(self, fee):
        self.price += fee


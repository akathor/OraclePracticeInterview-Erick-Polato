class Box:
    def __init__(self, max_box_weight, package_fee):
        self.fruits = []
        self.weight = 0
        self.price = 0
        self.status = 'open'
        self.max_box_weight = max_box_weight
        self.package_fee = package_fee

    def insert_fruit(self, fruit):
        self.fruits.append(fruit)
        self.weight += fruit.get_weight()
        self.price += fruit.get_price()

    def get_box_weight(self):
        return self.weight

    def get_box_max_weight(self):
        return self.max_box_weight

    def get_box_price(self):
        return round(self.price, 2)

    def get_box_price_no_fee(self):
        if self.status == 'open':
            return round(self.price, 2)
        else:
            return round(self.price - self.package_fee, 2)

    def get_box_fruits(self):
        return self.fruits

    def close_box(self):
        self.status = 'closed'
        self.price += self.package_fee


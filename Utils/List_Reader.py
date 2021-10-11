from Classes.FruitType import FruitType
from Classes.Fruit import Fruit


def instance_fruit_types_list(fruit_types_list):
    fruit_types = []
    for t in fruit_types_list:
        fruit_types.append(FruitType(t["name"], t["price"]))
    return fruit_types

def instance_fruit_list(fruit_list):
    fruits = []
    for f in fruit_list:
        for t in fruit_types:
            if f["type"] == t.get_name():
                fruits.append(Fruit(t, f["weight"]))
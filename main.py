from Classes.Fruit import Fruit
from Classes.FruitType import FruitType
from Classes.Box import Box
from Utils.List_Reader import *
from Utils.Box_Utilities import *


##### Initial lists and fee #####
max_box_weight = 1000      # maximum box weight in grams
packaging_fee = 1.10
fruit_types_list = [
    {"name": "banana", "price": 2.95},
    {"name": "pear", "price": 3.95},
    {"name": "apple", "price": 2.99},
    {"name": "coconut", "price": 7.15},
    {"name": "grapes", "price": 2.50},
    {"name": "passionfruit", "price": 4.24},
    {"name": "tomato", "price": 0.97},
    {"name": "strawberry", "price": 3.50}
]
fruit_list = [
    {"type": "banana", "weight": 100},
    {"type": "pear", "weight": 75},
    {"type": "apple", "weight": 85},
    {"type": "coconut", "weight": 415},
    {"type": "grapes", "weight": 120},
    {"type": "passionfruit", "weight": 65},
    {"type": "tomato", "weight": 40},
    {"type": "strawberry", "weight": 10},
    {"type": "banana", "weight": 110},
    {"type": "pear", "weight": 134},
    {"type": "apple", "weight": 99},
    {"type": "coconut", "weight": 71},
    {"type": "grapes", "weight": 120},
    {"type": "passionfruit", "weight": 24},
    {"type": "tomato", "weight": 197},
    {"type": "strawberry", "weight": 50},
    {"type": "banana", "weight": 195},
    {"type": "pear", "weight": 95},
    {"type": "apple", "weight": 99},
    {"type": "coconut", "weight": 215},
    {"type": "grapes", "weight": 50},
    {"type": "passionfruit", "weight": 24},
    {"type": "tomato", "weight": 197},
    {"type": "strawberry", "weight": 50},
    {"type": "banana", "weight": 195},
    {"type": "pear", "weight": 195},
    {"type": "apple", "weight": 99},
    {"type": "coconut", "weight": 515},
    {"type": "grapes", "weight": 50},
    {"type": "passionfruit", "weight": 24},
    {"type": "tomato", "weight": 37},
    {"type": "strawberry", "weight": 50}
]


##### Transforming json lists into instances lists #####
fruit_types = instance_fruit_types_list(fruit_types_list)

# Uncomment to print list
#for f in fruit_types:
#    print(f)

fruits = instance_fruit_list(fruit_list)

# Uncomment to print list
#for f in fruits:
#    print(f)

##### Packaging #####

boxes = package_into_boxes(fruits)

print_boxes(boxes, packaging_fee)

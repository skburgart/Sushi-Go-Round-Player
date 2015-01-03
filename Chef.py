import time

import Cookbook
import Mouse
import Coords
import Inventory
from Customer import Customer
from Game import NUM_SEATS

customers = [Customer(i) for i in range(NUM_SEATS)]


def prepare_orders():
    for customer in customers:
        order = customer.get_order()
        if order is not 'none' and customer.can_order() and has_ingredients(order):
            prepare(order)
            customer.order_prepared()


def clear_plates():
    for customer in customers:
        customer.clear_plate()


def prepare(food):
    add_ingredients(food)
    finish()


def has_ingredients(food):
    recipe = Cookbook.recipe[food]
    for ingredient, amount in recipe.items():
        if Inventory.stock[ingredient]['amount'] < amount:
            return False
    return True


def add_ingredients(food):
    recipe = Cookbook.recipe[food]
    for ingredient, amount in recipe.items():
        for i in range(amount):
            add_ingredient(ingredient)


def add_ingredient(ingredient):
    Inventory.stock[ingredient]['amount'] -= 1
    Mouse.click_pos(Coords.FOOD[ingredient])


def finish():
    Mouse.click_pos(Coords.MAT)
    time.sleep(1.25)

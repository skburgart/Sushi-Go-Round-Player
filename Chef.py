import time

import Cookbook
import Mouse
import Coords
import Inventory
from Customer import Customer


class Chef(object):
    def __init__(self, seats):
        self.customers = []
        for i in range(seats):
            self.customers.append(Customer(i))

    def prepare_orders(self):
        for customer in self.customers:
            order = customer.get_order()
            if order is not 'none' and customer.can_order() and has_ingredients(order):
                prepare(order)
                customer.order_prepared()
        Inventory.restock()
        Inventory.check_inventory()
        self.clear_plates()

    def clear_plates(self):
        for customer in self.customers:
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

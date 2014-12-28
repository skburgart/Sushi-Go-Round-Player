import time

from Cookbook import Cookbook
from Mouse import Mouse
from Coords import Coords
from Inventory import Inventory
from Customer import Customer


class Chef(object):
    def __init__(self, seats):
        self.customers = []
        for i in range(seats):
            self.customers.append(Customer(i))

    def prepare_orders(self):
        print("Checking orders")
        for customer in self.customers:
            order = customer.get_order()
            if order is not 'none':
                print("Preparing %s for %d" % (order, customer.get_seat()))
                Chef.prepare(order)
                Inventory.restock()

    @staticmethod
    def prepare(food):
        Chef.add_ingredients(food)
        Chef.finish()

    @staticmethod
    def add_ingredients(food):
        recipe = Cookbook.recipe[food]
        for ingredient, amount in recipe.items():
            for i in range(amount):
                Chef.add_ingredient(ingredient)

    @staticmethod
    def add_ingredient(ingredient):
        Inventory.stock[ingredient] -= 1
        Mouse.click_pos(Coords.FOOD[ingredient])

    @staticmethod
    def finish():
        Mouse.click_pos(Coords.MAT)
        time.sleep(1)

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
            if order is not 'none' and customer.can_order() and Chef.has_ingredients(order):
                print("Preparing %s for %d" % (order, customer.get_seat()))
                Chef.prepare(order)
                customer.order_prepared()
                Inventory.restock()
        self.clear_plates()
        Inventory.check_inventory()

    def clear_plates(self):
        for customer in self.customers:
            customer.clear_plate()

    @staticmethod
    def prepare(food):
        Chef.add_ingredients(food)
        Chef.finish()

    @staticmethod
    def has_ingredients(food):
        recipe = Cookbook.recipe[food]
        for ingredient, amount in recipe.items():
            if Inventory.stock[ingredient]['amount'] < amount:
                return False
        return True

    @staticmethod
    def add_ingredients(food):
        recipe = Cookbook.recipe[food]
        for ingredient, amount in recipe.items():
            for i in range(amount):
                Chef.add_ingredient(ingredient)

    @staticmethod
    def add_ingredient(ingredient):
        Inventory.stock[ingredient]['amount'] -= 1
        Mouse.click_pos(Coords.FOOD[ingredient])

    @staticmethod
    def finish():
        Mouse.click_pos(Coords.MAT)
        time.sleep(1)

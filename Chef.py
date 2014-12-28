from Cookbook import Cookbook
from Mouse import Mouse
from Coords import Coords
from Inventory import Inventory
from Image import Image
import time


class Chef(object):

    SEATS = 6
    @staticmethod
    def prepare_orders():
        print("Checking orders")
        for seat in range(Chef.SEATS):
            order = Chef.get_order(seat)
            if order is not 'none':
                print("Preparing %s for %d" % (order, seat + 1))
                Chef.prepare(order)

    @staticmethod
    def get_order(seat):
        order_bubble = Image.screen_grab(Coords.order_area(seat))
        order = Image.ORDER_HASH[Image.get_hash(order_bubble)]
        return order

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

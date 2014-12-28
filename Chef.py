from Cookbook import Cookbook
from Mouse import Mouse
from Coords import Coords
from Inventory import Inventory

class Chef(object):
    @staticmethod
    def cook(food):
        Chef.add_ingredients(food)
        Chef.finish()

    @staticmethod
    def add_ingredients(food):
        recipe = Cookbook.recipe[food]
        for ingredient, amount in recipe.iterkeys():
            for i in range(amount):
                Chef.add_ingredient(ingredient)

    @staticmethod
    def add_ingredient(ingredient):
        Inventory.stock[ingredient] -= 1
        Mouse.click_pos(Coords.FOOD[ingredient])

    @staticmethod
    def finish():
        Mouse.click_pos(Coords.MAT)

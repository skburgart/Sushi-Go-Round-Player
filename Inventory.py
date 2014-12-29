import time

from Mouse import Mouse
from Coords import Coords
from Image import Image


class Inventory(object):
    RESTOCK_THRESHOLD = 4
    RESTOCK_TIMEOUT = 5

    stock = {
        'shrimp': {
            'amount': 5,
            'timeout': 0,
            'restock': 5
        },
        'rice': {
            'amount': 10,
            'timeout': 0,
            'restock': 10
        },
        'nori': {
            'amount': 10,
            'timeout': 0,
            'restock': 10
        },
        'roe': {
            'amount': 10,
            'timeout': 0,
            'restock': 10
        },
        'salmon': {
            'amount': 5,
            'timeout': 0,
            'restock': 5
        },
        'unagi': {
            'amount': 5,
            'timeout': 0,
            'restock': 5
        }
    }

    @staticmethod
    def restock():
        for ingredient, info in Inventory.stock.items():
            if info['amount'] <= Inventory.RESTOCK_THRESHOLD and info['timeout'] == 0:
                Inventory.restock_ingredient(ingredient)

    @staticmethod
    def restock_ingredient(ingredient):
        Mouse.click_pos(Coords.PHONE)
        if ingredient == 'rice':
            Mouse.click_pos(Coords.PHONE_RICE)
            if Inventory.can_restock(ingredient):
                Mouse.click_pos(Coords.PHONE_RICE_ORDER)
                Mouse.click_pos(Coords.PHONE_ORDER_CONFIRM_FREE)
                Inventory.stock[ingredient]['timeout'] = time.time()
            else:
                Mouse.click_pos(Coords.PHONE_RICE_SAKE_CANCEL)
        else:
            Mouse.click_pos(Coords.PHONE_TOPPING)
            if Inventory.can_restock(ingredient):
                Mouse.click_pos(Coords.PHONE_TOPPINGS[ingredient])
                Mouse.click_pos(Coords.PHONE_ORDER_CONFIRM_FREE)
                Inventory.stock[ingredient]['timeout'] = time.time()
            else:
                Mouse.click_pos(Coords.PHONE_TOPPINGS_CANCEL)

    @staticmethod
    def can_restock(ingredient):
        img = Image.screen_grab(Coords.topping_order_area(ingredient))
        return Image.get_hash(img) == Image.CAN_RESTOCK_HASH[ingredient]

    @staticmethod
    def check_inventory():
        for ingredient, info in Inventory.stock.items():
            if info['timeout'] is not 0 and info['timeout'] + Inventory.RESTOCK_TIMEOUT < time.time():
                info['amount'] += info['restock']
                info['timeout'] = 0

import time

from Image import Image
from Coords import Coords


class Customer(object):
    ORDER_TIMEOUT = 15

    def __init__(self, seat):
        self.seat = seat
        self.last_order = 0

    def get_order(self):
        order_bubble = Image.screen_grab(Coords.order_area(self.seat))
        order = Image.ORDER_HASH[Image.get_hash(order_bubble)]
        if order is 'none' or not self.can_order():
            return 'none'
        self.last_order = time.time()
        return order

    def can_order(self):
        return time.time() - self.last_order > Customer.ORDER_TIMEOUT

    def get_seat(self):
        return self.seat

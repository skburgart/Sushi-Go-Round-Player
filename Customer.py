import time

from Image import Image
from Coords import Coords
from Mouse import Mouse

class Customer(object):
    ORDER_TIMEOUT = 20

    def __init__(self, seat):
        self.seat = seat
        self.last_order = 0

    def get_order(self):
        order_bubble = Image.screen_grab(Coords.order_area(self.seat))
        image_hash = Image.get_hash(order_bubble)
        if image_hash not in Image.ORDER_HASH.keys():
            Image.save(order_bubble, str(image_hash))
            return 'none'
        return Image.ORDER_HASH[image_hash]

    def clear_plate(self):
        Mouse.click_pos(Coords.plate_pos(self.seat))

    def can_order(self):
        return time.time() - self.last_order > Customer.ORDER_TIMEOUT

    def order_prepared(self):
        self.last_order = time.time()

    def get_seat(self):
        return self.seat

import time

import Image
import Mouse
import Coords
from Game import NUM_SEATS


class Customer(object):
    DELAY_DELTA = 2.65
    DELAY_INITIAL = 2
    DELAY_FEEDER = 6

    ORDER_TIMEOUT = []
    for i in range(NUM_SEATS):
        ORDER_TIMEOUT.append(DELAY_INITIAL + DELAY_FEEDER + DELAY_DELTA * i)

    def __init__(self, seat):
        self.seat = seat
        self.last_order = 0

    def get_order(self):
        order_bubble = Image.screen_grab(Coords.order_area(self.seat))
        image_hash = Image.get_hash(order_bubble)
        if image_hash not in Image.ORDER_HASH.keys():
            return 'none'
        return Image.ORDER_HASH[image_hash]

    def clear_plate(self):
        Mouse.click_pos(Coords.plate_pos(self.seat))

    def can_order(self):
        return time.time() - self.last_order > Customer.ORDER_TIMEOUT[self.seat]

    def order_prepared(self):
        self.last_order = time.time()

    def get_seat(self):
        return self.seat

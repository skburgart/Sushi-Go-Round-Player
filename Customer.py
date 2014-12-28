from enum import Enum

from Image import Image
from Coords import Coords


class CustomerState(Enum):
    EMPTY = 0
    ORDERED = 1
    SERVED = 2
    LEFT = 3


class Customer(object):

    def __init__(self, seat):
        self.state = CustomerState.EMPTY
        self.seat = seat

    def get_state(self):
        return self.state

    def get_order(self):
        order_bubble = Image.screen_grab(Coords.order_area(self.seat))
        order = Image.ORDER_HASH[Image.get_hash(order_bubble)]
        return order

    def get_seat(self):
        return self.seat

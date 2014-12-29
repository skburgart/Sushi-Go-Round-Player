import time

import Mouse
import Coords
import Chef
import Inventory


def play():
    start_game()
    while True:
        Chef.prepare_orders()
        Inventory.restock()
        Inventory.check_inventory()
        Chef.clear_plates()
        time.sleep(1)


def start_game():
    Mouse.click_pos(Coords.START_PLAY)
    Mouse.click_pos(Coords.START_CONTINUE)
    Mouse.click_pos(Coords.START_SKIP)
    Mouse.click_pos(Coords.START_CONTINUE)


if __name__ == '__main__':
    play()

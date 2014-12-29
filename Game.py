import time

import Mouse
import Coords
from Chef import Chef

NUM_SEATS = 6


def play():
    start_game()
    chef = Chef(NUM_SEATS)
    while True:
        chef.prepare_orders()
        time.sleep(1)


def start_game():
    Mouse.click_pos(Coords.START_PLAY)
    Mouse.click_pos(Coords.START_CONTINUE)
    Mouse.click_pos(Coords.START_SKIP)
    Mouse.click_pos(Coords.START_CONTINUE)


if __name__ == '__main__':
    play()

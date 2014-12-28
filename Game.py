import time

from Mouse import Mouse
from Coords import Coords
from Image import Image
from Chef import Chef


class Game(object):
    SEATS = 6

    @staticmethod
    def play():
        Game.start_game()
        for i in range(15):
            Chef.prepare_orders()
            time.sleep(1)


    @staticmethod
    def start_game():
        Mouse.click_pos(Coords.START_PLAY)
        Mouse.click_pos(Coords.START_CONTINUE)
        Mouse.click_pos(Coords.START_SKIP)
        Mouse.click_pos(Coords.START_CONTINUE)


if __name__ == '__main__':
    for i in range(6):
        Game.play()

import time

from Mouse import Mouse

from Coords import Coords
from Chef import Chef


class Game(object):
    NUM_SEATS = 6

    @staticmethod
    def play():
        Game.start_game()
        chef = Chef(Game.NUM_SEATS)
        for i in range(15):
            chef.prepare_orders()
            time.sleep(1)

    @staticmethod
    def start_game():
        Mouse.click_pos(Coords.START_PLAY)
        Mouse.click_pos(Coords.START_CONTINUE)
        Mouse.click_pos(Coords.START_SKIP)
        Mouse.click_pos(Coords.START_CONTINUE)


if __name__ == '__main__':
    Game.play()

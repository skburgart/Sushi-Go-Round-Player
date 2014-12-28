import time

from Image import Image
from Mouse import Mouse
from Coords import Coords


class Game(object):
    @staticmethod
    def start_game():
        Mouse.set_and_click(Coords.START_PLAY)
        time.sleep(0.3)
        Mouse.set_and_click(Coords.START_CONTINUE)
        time.sleep(0.3)
        Mouse.set_and_click(Coords.START_SKIP)
        time.sleep(0.3)
        Mouse.set_and_click(Coords.START_CONTINUE)

if __name__ == '__main__':
    Game.start_game()

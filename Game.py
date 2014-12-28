from Mouse import Mouse
from Coords import Coords


class Game(object):
    @staticmethod
    def play():
        Game.start_game()

    @staticmethod
    def start_game():
        Mouse.click_pos(Coords.START_PLAY)
        Mouse.click_pos(Coords.START_CONTINUE)
        Mouse.click_pos(Coords.START_SKIP)
        Mouse.click_pos(Coords.START_CONTINUE)


if __name__ == '__main__':
    Game.play()

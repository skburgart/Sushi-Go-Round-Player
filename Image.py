import ImageGrab

from Coordinates import Coordinates


def screen_grab():
    im = ImageGrab.grab(Coordinates.GAME_WINDOW)
    im.show()
from Mouse import Mouse
from Image import Image
from Coords import Coords
import time

def main():
    #print(Mouse.get_pos())
    #Image.screen_show(Coords.GAME_AREA)
    Mouse.set_and_click(Coords.START_PLAY)
    time.sleep(0.3)
    Mouse.set_and_click(Coords.START_CONTINUE)
    time.sleep(0.3)
    Mouse.set_and_click(Coords.START_SKIP)
    time.sleep(0.3)
    Mouse.set_and_click(Coords.START_CONTINUE)


if __name__ == '__main__':
    main()
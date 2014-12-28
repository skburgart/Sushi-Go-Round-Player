import time

import ImageGrab


class Image(object):
    SAVE_PATH = 'C:\\Users\\Steven\\Documents\\PycharmProjects\\SushiGoRound'

    @staticmethod
    def screen_grab(area=None):
        return ImageGrab.grab(area)

    @staticmethod
    def screen_save(area=None):
        Image.screen_grab(area).save(Image.SAVE_PATH + '\\screen_' + str(int(time.time())) + '.png', 'PNG')

    @staticmethod
    def screen_show(area=None):
        Image.screen_grab(area).show()

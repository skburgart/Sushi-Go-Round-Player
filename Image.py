import ImageOps

import ImageGrab


class Image(object):
    SAVE_PATH = 'C:\\Users\\Steven\\Documents\\PycharmProjects\\SushiGoRound'

    ORDER_HASH = {
        260134: 'onigiri',
        277110: 'caliroll',
        224360: 'gunkan',
        234448: 'salmonroll',
        185636: 'shrimpsushi'
    }

    CAN_RESTOCK_HASH = {
        'rice': 98382,
        'shrimp': 70591,
        'unagi': 67216,
        'nori': 49847,
        'roe': 76151,
        'salmon': 71961
    }

    @staticmethod
    def screen_grab(area=None):
        return ImageGrab.grab(area)

    @staticmethod
    def screen_save(area=None, filename='grab'):
        image = Image.screen_grab(area)
        Image.save(image, filename)

    @staticmethod
    def save(image, filename):
        full_path = Image.SAVE_PATH + "\\" + filename + '.png'
        image.save(full_path, 'PNG')

    @staticmethod
    def screen_show(area=None):
        Image.screen_grab(area).show()

    @staticmethod
    def get_hash(image):
        # convert to grayscale
        gray_image = ImageOps.grayscale(image)

        # get intensities as array
        intensities = gray_image.getcolors()

        # hash is sum of intensities
        image_hash = Image.sum_intensities(intensities)

        return image_hash

    @staticmethod
    def sum_intensities(intensities):
        total = 0
        for count, color in intensities:
            total += count * color
        return total

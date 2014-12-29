import ImageOps

import ImageGrab


SAVE_PATH = 'C:\\Users\\Steven\\Documents\\PycharmProjects\\SushiGoRound'

ORDER_HASH = {
    260134: 'onigiri',
    277110: 'caliroll',
    224360: 'gunkan',
    234448: 'salmonroll',
    185636: 'shrimpsushi',
    183992: 'unagiroll',
    224232: 'dragonroll',
    201224: 'combo'
}

CAN_RESTOCK_HASH = {
    'rice': 98382,
    'shrimp': 70591,
    'unagi': 67216,
    'nori': 49847,
    'roe': 76151,
    'salmon': 71961
}


def screen_grab(area=None):
    return ImageGrab.grab(area)


def screen_save(area=None, filename='grab'):
    image = screen_grab(area)
    save(image, filename)


def save(image, filename):
    full_path = SAVE_PATH + "\\" + filename + '.png'
    image.save(full_path, 'PNG')


def screen_show(area=None):
    screen_grab(area).show()


def get_hash(image):
    # convert to grayscale
    gray_image = ImageOps.grayscale(image)

    # get intensities as array
    intensities = gray_image.getcolors()

    # hash is sum of intensities
    image_hash = sum_intensities(intensities)

    return image_hash


def sum_intensities(intensities):
    total = 0
    for count, color in intensities:
        total += count * color
    return total

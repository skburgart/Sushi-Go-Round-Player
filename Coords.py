# padding
PAD_X = 200
PAD_Y = 238

# Game area
GAME_WIDTH = 639
GAME_HEIGHT = 479
GAME_AREA = (PAD_X + 1, PAD_Y + 1, PAD_X + GAME_WIDTH, PAD_Y + GAME_HEIGHT)

# Game start
START_PLAY = (300, 200)
START_SKIP = (572, 450)
START_CONTINUE = (314, 388)

# Food
MAT = (205, 351)
FOOD = {
    'shrimp': (40, 330),
    'rice': (90, 330),
    'nori': (40, 390),
    'roe': (90, 390),
    'salmon': (40, 450),
    'unagi': (90, 450)
}

# Phone
PHONE = (550, 350)
PHONE_TOPPING_WIDTH = 20
PHONE_TOPPING = (500, 271)
PHONE_TOPPINGS = {
    'shrimp': (492, 224),
    'unagi': (580, 224),
    'nori': (492, 277),
    'roe': (580, 277),
    'salmon': (490, 332),
    'rice': (538, 280)
}
PHONE_TOPPINGS_CANCEL = (596, 336)
PHONE_RICE = (500, 295)
PHONE_RICE_ORDER = (543, 282)
PHONE_RICE_SAKE_CANCEL = (584, 333)
PHONE_SAKE = (500, 319)
PHONE_ORDER_CONFIRM_FREE = (488, 296)

ORDER_WIDTH = 54
ORDER_HEIGHT = 24
ORDER_PAD_Y = 56
ORDER_PAD_X = 30
ORDER_OFFSET = 101


def get_offset_area(area):
    return area[0] + PAD_X, \
           area[1] + PAD_Y, \
           area[2] + PAD_X, \
           area[3] + PAD_Y,


def order_area(seat):
    left = ORDER_PAD_X + ORDER_OFFSET * seat
    top = ORDER_PAD_Y
    right = left + ORDER_WIDTH
    bottom = top + ORDER_HEIGHT
    return get_offset_area((left, top, right, bottom))


def topping_order_area(topping):
    point = PHONE_TOPPINGS[topping]
    return get_offset_area((
        point[0],
        point[1],
        point[0] + PHONE_TOPPING_WIDTH,
        point[1] + PHONE_TOPPING_WIDTH
    ))


PLATE_PAD_Y = 207
PLATE_PAD_X = 80
PLATE_OFFSET = 100


def plate_pos(seat):
    x = PLATE_PAD_X + (PLATE_OFFSET * seat)
    return x, PLATE_PAD_Y

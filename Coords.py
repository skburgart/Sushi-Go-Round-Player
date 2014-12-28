class Coords():
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
        'sushi': (40, 330),
        'rice': (90, 330),
        'nori': (40, 390),
        'roe': (90, 390),
        'salmon': (40, 450),
        'unagi': (90, 450)
    }

    # Phone
    PHONE = (550, 350)
    PHONE_TOPPING = (500, 271)
    PHONE_TOPPINGS = {
        'shrimp': (492, 224),
        'unagi': (580, 224),
        'nori': (492, 277),
        'roe': (580, 277),
        'salmon': (490, 332)
    }
    PHONE_RICE = (500, 295)
    PHONE_SAKE = (500, 319)

    ORDER_WIDTH = 54
    ORDER_HEIGHT = 24
    ORDER_PAD_Y = 56
    ORDER_PAD_X = 30
    ORDER_OFFSET = 101

    @staticmethod
    def get_offset_area(area):
        return area[0] + Coords.PAD_X, \
               area[1] + Coords.PAD_Y, \
               area[2] + Coords.PAD_X, \
               area[3] + Coords.PAD_Y,


    @staticmethod
    def order_area(seat):
        left = Coords.ORDER_PAD_X + Coords.ORDER_OFFSET * seat
        top = Coords.ORDER_PAD_Y
        right = left + Coords.ORDER_WIDTH
        bottom = top + Coords.ORDER_HEIGHT
        return Coords.get_offset_area((left, top, right, bottom))

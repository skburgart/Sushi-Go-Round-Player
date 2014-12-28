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
    FOOD_SUSHI = (40, 330)
    FOOD_RICE = (90, 330)
    FOOD_NORI = (40, 390)
    FOOD_ROE = (90, 390)
    FOOD_SALMON = (40, 450)
    FOOD_UNAGI = (90, 450)

    # Phone
    PHONE = (550, 350)
    PHONE_TOPPING = (500, 271)
    PHONE_TOPPING_SHRIMP = (492, 224)
    PHONE_TOPPING_UNAGI = (580, 224)
    PHONE_TOPPING_NORI = (492, 277)
    PHONE_TOPPING_ROE = (580, 277)
    PHONE_TOPPING_SALMON = (490, 332)
    PHONE_RICE = (500, 295)
    PHONE_SAKE = (500, 319)

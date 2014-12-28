class Inventory(object):
    RESTOCK_THRESHOLD = 2
    ORDER_TIMEOUT = 4

    stock = {
        'sushi': 5,
        'rice': 10,
        'nori': 10,
        'roe': 10,
        'salmon': 5,
        'unagi': 5
    }

    @staticmethod
    def restock():
        for ingredient, amount in Inventory.stock.items():
            if amount <= Inventory.RESTOCK_THRESHOLD:
                print("%s is low, ordering more" % ingredient)
                Inventory.order(ingredient)

    @staticmethod
    def order(ingredient):
        if ingredient == 'rice':
            pass
        else:
            pass

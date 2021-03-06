import Mouse
import Coords
import Chef
import Inventory

NUM_SEATS = 6


def play():
    start_game()
    while True:
        Chef.prepare_orders()
        Inventory.order_low_stock()
        Inventory.restock()
        Chef.clear_plates()


def start_game():
    Mouse.click_pos(Coords.START_PLAY)
    Mouse.click_pos(Coords.START_CONTINUE)
    Mouse.click_pos(Coords.START_SKIP)
    Mouse.click_pos(Coords.START_CONTINUE)


if __name__ == '__main__':
    play()

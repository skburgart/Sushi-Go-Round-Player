import win32api
import time

import win32con

import Coords


CLICK_SLEEP = 0.1


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(CLICK_SLEEP)


def set_pos(pos):
    padded_pos_x = pos[0] + Coords.PAD_X
    padded_pos_y = pos[1] + Coords.PAD_Y
    win32api.SetCursorPos((padded_pos_x, padded_pos_y))


def get_pos():
    pos = win32api.GetCursorPos()
    padded_pos_x = pos[0] - Coords.PAD_X
    padded_pos_y = pos[1] - Coords.PAD_Y
    return padded_pos_x, padded_pos_y


def click_pos(pos):
    set_pos(pos)
    left_click()

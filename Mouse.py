import win32api

import time

import win32con

from Coords import Coords


class Mouse(object):
    CLICK_SLEEP = 0.05

    @staticmethod
    def left_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(Mouse.CLICK_SLEEP)

    @staticmethod
    def set_pos(pos):
        padded_pos_x = pos[0] + Coords.PAD_X
        padded_pos_y = pos[1] + Coords.PAD_Y
        win32api.SetCursorPos((padded_pos_x, padded_pos_y))

    @staticmethod
    def get_pos():
        pos = win32api.GetCursorPos()
        padded_pos_x = pos[0] - Coords.PAD_X
        padded_pos_y = pos[1] - Coords.PAD_Y
        return padded_pos_x, padded_pos_y

    @staticmethod
    def click_pos(pos):
        Mouse.set_pos(pos)
        Mouse.left_click()

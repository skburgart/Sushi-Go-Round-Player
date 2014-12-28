import win32api
import time

import win32con


class Mouse(object):
    @staticmethod
    def left_click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    @staticmethod
    def set_pos(pos):
        win32api.SetCursorPos(pos[0], pos[1])

    @staticmethod
    def get_pos():
        return win32api.GetCursorPos()

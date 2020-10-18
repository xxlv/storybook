#!/usr/bin/python3
# -*- coding:utf-8-*-
import time

from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as Mouse
from deviceUtil import Device
from position import Position

import os
import time
import pyautogui as pag

keyboarder = Controller()
M = Mouse()


def found_mouse():
    try:
        while True:
            # screenWidth, screenHeight = pag.size()
            x, y = pag.position()
            posStr = "(" + str(x).rjust(4) + ',' + str(y).rjust(4) + ")"
            print(posStr)
            os.system("clear ")
            time.sleep(1)

    except KeyboardInterrupt:
        pass


def open_package():
    """
    # 打开背包
    # 按下组合键 CTRL+E 即可
    """
    found_mouse()
    with keyboarder.pressed(Key.cmd):
        keyboarder.press('e')
        keyboarder.release('e')


if __name__ == '__main__':
    open_package()

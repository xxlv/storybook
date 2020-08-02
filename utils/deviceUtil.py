#!/usr/bin/python3
# -*- coding:utf-8-*-
from pynput import keyboard
from pynput.keyboard import KeyCode, Key
from pynput.mouse import Button, Controller
from timeUtil import TimeWait
from logUtil import Log

"""
设备工具
持有 鼠标/键盘
"""

M = Controller()
B = keyboard.Controller()


class Device(object):
    REAL_DEVICE = True

    @staticmethod
    def _before():
        pass

    @staticmethod
    def move(pos):
        Device._before()
        Device._move(pos)

    @staticmethod
    def click(pos, direction, count):
        Device._before()
        if pos is None:
            return

        Device._move(pos)
        btn = Button.right
        if direction <= 0:
            btn = Button.left
        while True:
            if count < 0:
                break
            count -= 1
            Device._click(btn)

    @staticmethod
    def typeof(message):
        Device._before()
        Device._type(message)

    @staticmethod
    def key(key):
        Device._before()
        Device._key(key)

    @staticmethod
    def _move(pos):
        Device._before()
        Log.log("鼠标移动到 【{}】".format(pos))

        if not Device.REAL_DEVICE:
            return
        if pos is None:
            return
        if M is not None:
            M.position = (0, 0)
            M.move(int(pos.X), int(pos.Y))

    @staticmethod
    def _click(btn):
        Log.log("点击按钮 【{}】".format(btn))
        if not Device.REAL_DEVICE:
            return

        if M is not None:
            M.press(btn)
            TimeWait.wait(1)
            M.release(btn)

    @staticmethod
    def _key(k):
        Log.log("按下键 【{}】".format(k))
        if not Device.REAL_DEVICE:
            return
        try:
            if B is not None:
                if k in Key.__dict__:
                    k = Key.__dict__[k]
                    B.press(k)
                    B.release(k)
        except KeyError as e:
            print(e)

    @staticmethod
    def _type(message):
        if message is None:
            return

        if not Device.REAL_DEVICE:
            return
        Log.log("输入文字 【{}】".format(message))
        if B is not None:
            B.type(message)

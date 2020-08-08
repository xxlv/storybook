#!/usr/bin/python3
# -*- coding:utf-8-*-

from datetime import datetime
from tkinter import END

from gui.context import GuiContext

"""
日志工具
"""


class Log(object):
    text = None
    root = None

    @staticmethod
    def warn(s):
        dt = datetime.now()
        print("[{}]  -> {}".format(dt.strftime("%Y-%m-%d %H:%M:%S"), s))

    @staticmethod
    def log(s):
        dt = datetime.now()
        info = "[{}]  -> {}".format(dt.strftime("%Y-%m-%d %H:%M:%S"), s)
        if Log.text is not None and Log.root is not None:
            Log.text.insert(END, info + "\n")
            Log.text.see(END)
            Log.root.update()
        print(info)


if __name__ == '__main__':
    Log.log("Hello")

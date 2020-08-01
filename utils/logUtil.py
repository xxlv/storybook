#!/usr/bin/python3
# -*- coding:utf-8-*-

from datetime import datetime

"""
日志工具
"""


class Log(object):

    @staticmethod
    def warn(s):
        dt = datetime.now()
        print("[{}]  -> {}".format(dt.strftime("%Y-%m-%d %H:%M:%S"), s))

    @staticmethod
    def log(s):
        dt = datetime.now()
        print("[{}]  -> {}".format(dt.strftime("%Y-%m-%d %H:%M:%S"), s))


if __name__ == '__main__':
    Log.log("Hello")

#!/usr/bin/python3
# -*- coding:utf-8-*-

import time
from logUtil import Log

"""
时间工具
负责Sleep 等操作
"""


class TimeWait(object):
    @staticmethod
    def wait(sec, prefix=""):
        try:
            sec = int(sec)
        except ValueError as e:
            Log.warn("无法将{} 转换成时间，默认0".format(sec))
            sec = 0
        if sec <= 0:
            return
        while True:
            if sec > 1:
                Log.log("[{}] 剩余时间 {}".format(prefix, sec))
            time.sleep(1)
            sec -= 1
            if sec <= 0:
                break


if __name__ == '__main__':
    TimeWait.wait(10)

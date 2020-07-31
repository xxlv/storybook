#!/usr/bin/python3
# -*- coding:utf-8-*-

import time
from logUtil import Log

"""
时间工具
"""


class TimeWait(object):

    @staticmethod
    def wait(sec, prefix="系统"):
        if sec <= 0:
            return

        while True:
            Log.log("[{}] 剩余时间 {}".format(prefix, sec))

            time.sleep(1)
            sec -= 1
            if sec <= 0:
                break


if __name__ == '__main__':
    TimeWait.wait(10)

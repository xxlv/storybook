#!/usr/bin/python3
# -*- coding:utf-8-*-
import time

from condition import Condition
from utils.logUtil import Log
from utils.positionUtil import PosUtil


class NotMoveCondition(Condition):

    def __init__(self, name):
        super().__init__(name)
        self._init()

    def _init(self):
        self.cond = self.notmove

    def notmove(self):
        Log.log("正在检查条件是否满足")
        while True:
            #  todo 鼠标获取当前屏幕焦点
            # 截图 与指定位置图片比较 如果存在并且一样，则表示位置没变动
            # 如果不一致 则将当前的图片设置为目标图片
            # 坐标位置
            checked = PosUtil.check_if_same((60, 50), 80, 20)
            if checked:
                return
            print(".", end="")
            time.sleep(3)


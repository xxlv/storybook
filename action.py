#!/usr/bin/python3
# -*- coding:utf-8-*-

from enum import Enum
from utils.deviceUtil import Device
from utils.timeUtil import TimeWait
from utils.logUtil import Log


class ActionEnum(Enum):
    # 不做任何事
    DO_NOTHING = 0
    # 右键点击
    R_CLICK = 1
    # 左键点击
    L_CLICK = 2
    # 右键双击
    R_D_CLICK = 4
    # 左键双击
    L_D_CLICK = 5

    # 键盘按下
    K_PRESS = 10
    # 键盘松开
    K_RELEASE = 11
    # 键盘按下并且松开
    K_PRESS_AND_RELEASE = 12


class Action(object):
    """
        定义了Action
        一个Action，如，在指定的位置点击
        | position 位置
        | action 执行动作
        | time_wait 执行完毕等待时间
    """

    def __init__(self, position, action_enum, time_wait, name=None):
        self.position = position
        self.action_enum = action_enum
        self.time_wait = time_wait
        if name is None:
            m = {v: k for k, v in dict(ActionEnum.__dict__).items()}
            if m.has_key(action_enum):
                act_desc = m.get(action_enum)
            else:
                act_desc = "->{}".format(action_enum)

            name = "@{}({},{})-sleep-{}".format(act_desc, position.Y, position.Y, time_wait)
        self.action_name = name

    def run(self, container=None):
        Log.log("[{}]执行Action {}".format(container, self.action_name))
        if self.action_enum == ActionEnum.R_CLICK:
            Device.click(self.position, 0, 1)
            TimeWait.wait(self.time_wait)

    def __str__(self):
        return " @action in position({},{}) ,action type is {} ,will wait for {} sec".format(self.position.X,
                                                                                             self.position.Y,
                                                                                             self.action_enum,
                                                                                             self.time_wait)

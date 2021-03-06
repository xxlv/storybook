#!/usr/bin/python3
# -*- coding:utf-8-*-

from utils.deviceUtil import Device
from utils.timeUtil import TimeWait
from utils.logUtil import Log
from conditions.condition import Condition
from conditions.notmove_condition import NotMoveCondition


class ActionEnum(object):
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
    # 鼠标移动
    M_MOVE = 6
    # 睡眠
    T_SLEEP = 7
    # 注释
    N_COMMENT = 8
    # 键盘按下
    K_PRESS = 10
    # 键盘松开
    K_RELEASE = 11
    # 键盘按下并且松开
    K_PRESS_AND_RELEASE = 12
    # 特殊键按下
    K_KEY = 13
    # 键盘输入
    K_TYPE = 14
    # 条件
    CONDITION = 15
    # 循环
    LOOP = 16
    # 结束循环
    END_LOOP = 17


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
            if action_enum in m:
                act_desc = m.get(action_enum)
            else:
                act_desc = "->{}".format(action_enum)
            if position is not None:
                name = "@{}({},{})-sleep-{}".format(act_desc, position.Y, position.Y, time_wait)
            else:
                name = "@{}-sleep-{}".format(act_desc, time_wait)
        self.action_name = name

    def bindmetadata(self, metadata):
        self.metadata = metadata
        return self

    def run(self, container=None, runner=None):
        Device.RUNNER = runner
        Log.log("[{}]执行Action {}".format(container, self.action_name))

        if self.action_enum == ActionEnum.R_CLICK:
            Device.click(self.position, 1, 1)
            TimeWait.wait(self.time_wait)

        if self.action_enum == ActionEnum.L_CLICK:
            Device.click(self.position, -1, 1)
            TimeWait.wait(self.time_wait)

        if self.action_enum == ActionEnum.R_D_CLICK:
            Device.click(self.position, 1, 2)
            TimeWait.wait(self.time_wait)

        if self.action_enum == ActionEnum.L_D_CLICK:
            Device.click(self.position, -1, 2)

        if self.action_enum == ActionEnum.M_MOVE:
            Device.move(self.position)

        if self.action_enum == ActionEnum.K_KEY:
            if self.metadata is not None:
                Device.key(self.metadata)

        if self.action_enum == ActionEnum.K_TYPE:
            if self.metadata is not None:
                Device.typeof(self.metadata)

        if self.action_enum == ActionEnum.CONDITION:
            Log.log("使用条件引擎 [{}]".format(self.metadata))
            NotMoveCondition(self.metadata).waitfor()

        TimeWait.wait(self.time_wait)

    def __str__(self):
        return " @action in position({},{}) ,action type is {} ,will wait for {} sec".format(self.position.X,
                                                                                             self.position.Y,
                                                                                             self.action_enum,
                                                                                             self.time_wait)

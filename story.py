#!/usr/bin/python3
# -*- coding:utf-8-*-


"""
Story
定义一系列事件集合进行处理

"""

from action import ActionEnum, Action
from event import Event
from position import Position
from storycmmand import StoryCommand
from utils.logUtil import Log
from timeUtil import TimeWait


class Story(object):
    def __init__(self, name=""):
        self.name = name
        self.event_group = []
        self.event_loop_group = []

        self.record_loop = False
        self.start_loop = False
        self.count_loop = -1
        self.timewait_loop = 1
        self.loop_total = 0

    def push(self, event):
        if event is not None:
            self.event_group.append(event)

    def start(self, runner, condition=True):
        Log.log("-------------------------------------------")
        Log.log("Start Story [{}]".format(self.name))
        Log.log("-------------------------------------------")
        # 开始执行时间
        # 遇到循环条件的话 进行条件逻辑处理
        if condition:
            if self.event_group is None or self.event_group.__len__() <= 0:
                return
            for e in self.event_group:
                if e is not None:
                    if e.action_group is not None and e.action_group.__len__() > 0:
                        act = e.action_group[0]
                        #  start loop remark
                        if act is not None and act.action_enum == ActionEnum.LOOP:
                            self.record_loop = True
                            # loop(1,2)
                            metadata = str(act.metadata)
                            metadata = metadata.replace(StoryCommand.COMMAND_LOOP, "").replace("(", "").replace(")", "")
                            if metadata is not None:
                                config = metadata.split(",")
                                self.count_loop = int(config[0])
                                self.timewait_loop = int(config[1])

                    # endloop remark
                    if e.action_group is not None and e.action_group.__len__() > 0:
                        act = e.action_group[0]
                        if act is not None and act.action_enum == ActionEnum.END_LOOP:
                            self.start_loop = True

                    if self.record_loop:
                        self.event_loop_group.append(e)

                    # 遇到endloop的时候 执行LOOP
                    # FIXME 随机坐标无法使用
                    if self.start_loop:
                        while True:
                            if self.count_loop != -1:
                                Log.log("执行Loop {} 剩余 ".format(self.count_loop))
                            else:
                                Log.log("-------------------------------------------------------")
                                Log.log("进入永恒模式,目前已执行 #{}# 次".format(self.loop_total))
                                Log.log("-------------------------------------------------------")

                            if self.count_loop <= 0 and self.count_loop != -1:
                                break
                            for e in self.event_loop_group:
                                e.execute(container=self.name)
                            if self.count_loop != -1:
                                self.count_loop -= 1
                            self.loop_total += 1
                            TimeWait.wait(self.timewait_loop)

                    if not self.record_loop:
                        e.execute(container=self.name,runner=runner)

    def _start_loop(self):
        pass

    def __str__(self):
        return "Story->{} event[{}]".format(self.name, self.event_group.__len__())


if __name__ == '__main__':
    s = Story("师门任务")
    s.push(Event(Action(Position(1, 1), ActionEnum.R_CLICK, 3), 1, "hello"))
    s.push(Event(Action(Position(2, 1), ActionEnum.R_CLICK, 1), 1))
    s.push(Event(Action(Position(3, 1), ActionEnum.R_CLICK, 2), 1))
    s.push(Event(Action(Position(4, 1), ActionEnum.R_CLICK, 1), 1))

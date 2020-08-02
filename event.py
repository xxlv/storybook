#!/usr/bin/python3
# -*- coding:utf-8-*-


import time

from action import Action, ActionEnum
from position import Position
from utils.logUtil import Log


class Event:
    """
    Position : Event Location
    Action
    TimeWait
    """
    def push(self, action):
        if action is not None:
            self.action_group.append(action)

    def updatename(self, name):
        self.name = name

    def __init__(self, action=None, timewait=None, name=None):
        self.action = action
        self.timewait = timewait
        if name is None and self.action is not None:
            name = "Event-action({})".format(self.action.action_name)
        self.name = name
        self.action_group = []

    def execute(self, container=None):
        start = time.time()
        Log.log("Execute Event {}".format(self))
        if self.action is not None:
            self.action.run(container)

        for act in self.action_group:
            if act is not None:
                act.run(container)

        Log.log("[{}] 任务结束,总计消耗时间 {}".format(self.name, int(time.time() - start)))

    def __str__(self):
        return "{}".format(self.action)


if __name__ == '__main__':
    Event(Action(Position(1, 1), ActionEnum.R_CLICK, 3), 1).execute()

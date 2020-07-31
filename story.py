#!/usr/bin/python3
# -*- coding:utf-8-*-


"""
Story
定义一系列事件集合进行处理

"""

from action import ActionEnum, Action
from event import Event
from position import Position
from utils.logUtil import Log


class Story(object):
    event_group = []

    def __init__(self, name):
        self.name = name

    def push(self, event):
        if event is not None:
            self.event_group.append(event)

    def start(self, condition=True):
        Log.log("-------------------------------------------")
        Log.log("Start Story [{}]".format(self.name))
        Log.log("-------------------------------------------")
        if condition:
            while True:
                if self.event_group is None or self.event_group.__len__() <= 0:
                    break
                e = self.event_group.pop()
                if e is not None:
                    e.execute(container=self.name)


if __name__ == '__main__':
    s = Story("师门任务")
    s.push(Event(Action(Position(1, 1), ActionEnum.R_CLICK, 3), 1, "Hello"))
    s.push(Event(Action(Position(2, 1), ActionEnum.R_CLICK, 1), 1))
    s.push(Event(Action(Position(3, 1), ActionEnum.R_CLICK, 2), 1))
    s.push(Event(Action(Position(4, 1), ActionEnum.R_CLICK, 1), 1))

    s.start()

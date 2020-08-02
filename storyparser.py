#!/usr/bin/python3
# -*- coding:utf-8-*-

from enum import Enum
from utils.deviceUtil import Device
from utils.timeUtil import TimeWait
from utils.logUtil import Log
from storycmmand import StoryCommand
from story import Story
from event import Event
from action import Action, ActionEnum
from position import Position

import random

"""
解析
"""


class StoryParser(object):
    event_group = []

    def __init__(self, book):
        self.book = book

    def parse(self):
        """
        Return story
        """
        body = self.read_book()
        story_segment = body.split("\n")
        stroy = Story()

        for s in story_segment:
            s = s.strip()
            if s.startswith("#"):
                continue
            if s.startswith(StoryCommand.COMMAND_NAME):
                s = s.replace(StoryCommand.COMMAND_NAME, "").replace("=", "").strip()
                stroy.name = s
            if s.startswith(StoryCommand.COMMAND_ACT):
                # 解析StoryCommand Act
                stroy.push(self._get_event(s))

        print("Build new story {}".format(stroy))
        return stroy

    def _get_event(self, s):
        # @move(1,10)->rclick(2)->wait(0)
        #  这里的EVENT 每次都是相同的
        event = Event()
        s = s[1:]

        commands = s.split(StoryCommand.COMMAND_FLOW)
        for cmd in commands:
            self._parse_and_set_event(cmd, event)
        return event

    def _parse_and_set_event(self, cmd, event):

        """
        解析命令 初始化event的Actions
        """

        EMPTY = ""
        if cmd.startswith(StoryCommand.COMMAND_MOVE):
            cmd = cmd.replace(StoryCommand.COMMAND_MOVE, "").replace(StoryCommand.COMMAND_PARAMS_L, "").replace(
                StoryCommand.COMMAND_PARAMS_R, "").strip()
            cmds = cmd.split(",")
            if (cmds.__len__() < 2):
                return

            pos = (cmds[0], cmds[1])
            time_wait = 0
            if (cmds.__len__() > 3):
                time_wait = cmds[2]

            event.push(Action(self._get_pos(pos), ActionEnum.M_MOVE, time_wait))

        if cmd.startswith(StoryCommand.COMMAND_D_CLICK):
            cmd = cmd.replace(StoryCommand.COMMAND_D_CLICK, "").replace(StoryCommand.COMMAND_PARAMS_L, "").replace(
                StoryCommand.COMMAND_PARAMS_R, "").strip()

            cmds = cmd.split(",")
            if (cmds.__len__() < 2):
                return

            pos = (cmds[0], cmds[1])
            time_wait = 0
            if (cmds.__len__() > 3):
                time_wait = cmds[2]

            event.push(Action(self._get_pos(pos), ActionEnum.L_D_CLICK, time_wait))

        if cmd.startswith(StoryCommand.COMMAND_CLICK_R):
            cmd = cmd.replace(StoryCommand.COMMAND_CLICK_R, EMPTY).replace(StoryCommand.COMMAND_PARAMS_L,
                                                                           EMPTY).replace(
                StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()

            cmds = cmd.split(",")
            if (cmds.__len__() < 2):
                return

            pos = (cmds[0], cmds[1])
            time_wait = 0
            if (cmds.__len__() > 3):
                time_wait = cmds[2]

            event.push(Action(self._get_pos(pos), ActionEnum.R_D_CLICK, time_wait))

        if cmd.startswith(StoryCommand.COMMAND_CLICK_L):
            cmd = cmd.replace(StoryCommand.COMMAND_CLICK_L, EMPTY).replace(StoryCommand.COMMAND_PARAMS_L,
                                                                           EMPTY).replace(
                StoryCommand.COMMAND_PARAMS_R, "").strip()

            cmds = cmd.split(",")
            if (cmds.__len__() < 2):
                return

            pos = (cmds[0], cmds[1])
            time_wait = 0
            if (cmds.__len__() > 3):
                time_wait = cmds[2]

            event.push(Action(self._get_pos(pos), ActionEnum.L_D_CLICK, time_wait))

        if cmd.startswith(StoryCommand.COMMAND_WAIT):
            cmd = cmd.replace(StoryCommand.COMMAND_WAIT, "").replace(StoryCommand.COMMAND_PARAMS_L, EMPTY).replace(
                StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()

            cmds = cmd.split(",")
            if (cmds.__len__() < 1):
                return
            pos = (0, 0)
            time_wait = cmds[0]
            event.push(Action(self._get_pos(pos), ActionEnum.T_SLEEP, time_wait))

        # 处理输入
        if cmd.startswith(StoryCommand.COMMAND_B_TYPE):
            cmd = cmd.replace(StoryCommand.COMMAND_B_TYPE, "").replace(StoryCommand.COMMAND_PARAMS_L, EMPTY).replace(
                StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()
            cmds = cmd.split(",")
            if (cmds.__len__() < 1):
                return
            cmd = cmds[0]
            event.push(Action(Position(0, 0), ActionEnum.K_TYPE, 0).bindmetadata(cmd))

        # 按键
        if cmd.startswith(StoryCommand.COMMAND_B_KEY):
            cmd = cmd.replace(StoryCommand.COMMAND_B_KEY, EMPTY).replace(StoryCommand.COMMAND_PARAMS_L, EMPTY).replace(
                StoryCommand.COMMAND_PARAMS_R, "").strip()

            cmds = cmd.split(",")
            if (cmds.__len__() < 1):
                return
            cmd = cmds[0]
            event.push(Action(Position(0, 0), ActionEnum.K_KEY, 0).bindmetadata(cmd))

        if cmd.startswith(StoryCommand.COMMAND_COMMENT):
            cmd = cmd.replace(StoryCommand.COMMAND_COMMENT, EMPTY).replace(StoryCommand.COMMAND_PARAMS_L,
                                                                           EMPTY).replace(
                StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()
            event.updatename(cmd)

        if cmd.startswith(StoryCommand.COMMAND_CHECK_POINT):
            # command = cmd.replace(StoryCommand.COMMAND_CHECK_POINT, "").replace(StoryCommand.COMMAND_PARAMS_L,
            #                                                                     EMPTY).replace(
            #     StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()
            # 绑定特殊的元数据
            event.push(Action(None, ActionEnum.CONDITION, 0).bindmetadata(cmd))

        # 循环
        if cmd.startswith(StoryCommand.COMMAND_LOOP):
            # command = cmd.replace(StoryCommand.COMMAND_LOOP, "").replace(StoryCommand.COMMAND_PARAMS_L,
            #                                                              EMPTY).replace(
            #     StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()
            event.push(Action(None, ActionEnum.LOOP, 0).bindmetadata(cmd))

        # 结束循环
        if cmd.startswith(StoryCommand.COMMAND_END_LOOP):
            # command = cmd.replace(StoryCommand.COMMAND_END_LOOP, "").replace(StoryCommand.COMMAND_PARAMS_L,
            #                                                                  EMPTY).replace(
            #     StoryCommand.COMMAND_PARAMS_R, EMPTY).strip()
            event.push(Action(None, ActionEnum.END_LOOP, 0).bindmetadata(cmd))

        return event

    def _get_pos(self, p):
        RAND_SPLIT = "~"
        if len(p) < 2:
            return None
        x = p[0]
        y = p[1]
        # (1,2~2,2)
        if type(x) == type("") and x.__contains__(RAND_SPLIT):
            randscope = x.split("~")
            if len(randscope) >= 2:
                x = lambda: self._get_rand(randscope[0], randscope[1])
        #
        if type(y) == type("") and y.__contains__(RAND_SPLIT):
            randscope = y.split("~")
            if len(randscope) >= 2:
                y = lambda: self._get_rand(randscope[0], randscope[1])

        return Position(x, y)

    def read_book(self):
        with open(self.book, "r+", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def _get_rand(min, max):
        min = int(min)
        if min < 0:
            min = 0

        max = int(max)
        r = int(random.random() * max)
        while r > max:
            r = r - 10
        while r < min:
            r += 10
        return r


if __name__ == '__main__':
    StoryParser("{}/{}".format("", "story\\SHIMEN.txt")).parse()

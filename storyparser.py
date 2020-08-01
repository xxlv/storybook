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
            if cmd.startswith(StoryCommand.COMMAND_MOVE):
                cmd = cmd.replace(StoryCommand.COMMAND_MOVE, "").replace(StoryCommand.COMMAND_PARAMS_L, "").replace(
                    StoryCommand.COMMAND_PARAMS_R, "").strip()
                cmds = cmd.split(",")
                if (cmds.__len__() < 2):
                    continue

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
                    continue

                pos = (cmds[0], cmds[1])
                time_wait = 0
                if (cmds.__len__() > 3):
                    time_wait = cmds[2]

                event.push(Action(self._get_pos(pos), ActionEnum.L_D_CLICK, time_wait))

            if cmd.startswith(StoryCommand.COMMAND_CLICK_R):
                cmd = cmd.replace(StoryCommand.COMMAND_CLICK_R, "").replace(StoryCommand.COMMAND_PARAMS_L, "").replace(
                    StoryCommand.COMMAND_PARAMS_R, "").strip()

                cmds = cmd.split(",")
                if (cmds.__len__() < 2):
                    continue

                pos = (cmds[0], cmds[1])
                time_wait = 0
                if (cmds.__len__() > 3):
                    time_wait = cmds[2]

                event.push(Action(self._get_pos(pos), ActionEnum.R_CLICK, time_wait))

            if cmd.startswith(StoryCommand.COMMAND_WAIT):
                cmd = cmd.replace(StoryCommand.COMMAND_WAIT, "").replace(StoryCommand.COMMAND_PARAMS_L, "").replace(
                    StoryCommand.COMMAND_PARAMS_R, "").strip()

                cmds = cmd.split(",")
                if (cmds.__len__() < 1):
                    continue
                pos = (0, 0)
                time_wait = cmds[0]
                event.push(Action(self._get_pos(pos), ActionEnum.T_SLEEP, time_wait))

            # 键盘输入
            if cmd.startswith(StoryCommand.COMMAND_B_KEY_TYPE):
                cmd = cmd.replace(StoryCommand.COMMAND_B_KEY_TYPE, "").replace(StoryCommand.COMMAND_PARAMS_L, "").replace(
                    StoryCommand.COMMAND_PARAMS_R, "").strip()

                cmds = cmd.split(",")
                if (cmds.__len__() < 1):
                    continue
                cmd = cmds[0]
                event.push(Action(Position(0,0), ActionEnum.K_TYPE, 0).bindmetadata(cmd))

            if cmd.startswith(StoryCommand.COMMAND_COMMENT):
                comment = cmd.replace(StoryCommand.COMMAND_COMMENT, "").replace(StoryCommand.COMMAND_PARAMS_L,
                                                                                "").replace(
                    StoryCommand.COMMAND_PARAMS_R, "").strip()
                event.updatename(comment + u"")
        return event

    def _get_pos(self, p):
        return Position(int(p[0]), int(p[1]))

    def read_book(self):
        with open(self.book, "r+", encoding="utf-8") as f:
            return f.read()


if __name__ == '__main__':
    StoryParser("{}/{}".format("", "story\\SHIMEN.txt")).parse()

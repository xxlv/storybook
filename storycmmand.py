#!/usr/bin/python3
# -*- coding:utf-8-*-


"""
StoryRunner

"""

from storyparser import StoryParser


class StoryCommand(object):
    COMMAND_ACT = "@"
    COMMAND_MOVE = "move"
    COMMAND_D_CLICK = "dclick"
    COMMAND_FLOW = "->"
    COMMAND_WAIT = "wait"
    COMMAND_PARAMS_L = "("
    COMMAND_PARAMS_R = ")"
    COMMAND_CHECK_POINT = "$$"
    CHECK_NOT_MOVE = "NOT_MOVE"


if __name__ == '__main__':
    pass

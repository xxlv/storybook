#!/usr/bin/python3
# -*- coding:utf-8-*-


class Condition(object):

    def __init__(self, name):
        self.name = name

    def setcond(self, cond):
        self.cond = cond

    def waitfor(self):
        self.cond()

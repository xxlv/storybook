#!/usr/bin/python3
# -*- coding:utf-8-*-

from enum import Enum
from utils.deviceUtil import Device
from utils.timeUtil import TimeWait
from utils.logUtil import Log

from story import Story


class StoryParser(object):

    def __init__(self, book):
        self.book = book

    def parse(self):
        body = self.read_book()
        print(body)
        return None

    def _get_name(self):
        pass

    def read_book(self):
        with open(self.book, "r+") as f:
            return f.read()

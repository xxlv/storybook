#!/usr/bin/python3
# -*- coding:utf-8-*-


"""
StoryRunner

"""

from storyparser import StoryParser

class StoryRunner(object):
    def __init__(self, name, context):
        self.name = name
        # GUI context
        self.context = context

    def read(self):
        story = StoryParser(self.name).parse()
        if story is not None:
            story.start(self)


if __name__ == '__main__':
    StoryRunner("auto_war.txt").read()

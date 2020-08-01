#!/usr/bin/python3
# -*- coding:utf-8-*-


"""
StoryRunner

"""

from storyparser import StoryParser


class StoryRunner(object):
    BASE_STORY_PATH = "story"

    def __init__(self, name):
        self.name = name

    def read(self):
        story = StoryParser("{}/{}".format(StoryRunner.BASE_STORY_PATH, self.name)).parse()
        if story is not None:
            story.start()


if __name__ == '__main__':
    StoryRunner("SHIMEM.txt").read()

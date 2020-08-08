#!/usr/bin/python3
# -*- coding:utf-8-*-

# The GUI context for current project
# we use this print logs and do some extra things
class GuiContext(object):
    def __init__(self, root, text):
        self.root = root
        self.text = text
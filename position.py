#!/usr/bin/python3
# -*- coding:utf-8-*-


class Position(object):
    """
    X,Y 代表相当于(0,0) 的坐标位置
    """

    def __getattribute__(self, item):
        pos= object.__getattribute__(self,item)
        if isinstance(pos,type(1)) or isinstance(pos,type("")):
            return int(pos)
        else:
            return int(pos())


    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # def get(self):
    #     if isinstance(self.X, type(1)) and isinstance(self.X, type(1)):
    #         return (self.X, self.Y)
    #     else:
    #         return (self.X(), self.Y())

    def __str__(self):
        return "({},{})".format(self.X, self.Y)


if __name__ == '__main__':
    print(Position(10, 10))

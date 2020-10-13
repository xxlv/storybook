#!/usr/bin/python3
# -*- coding:utf-8-*-


# /usr/bin/python3
# -*- coding=utf-8 -*-

import os

#
# import pyautogui
# import pytesseract
# from PIL import Image

SAVE_PATH = "C:\\Users\\12528\\game\\storybook\\data"


class PosUtil(object):
    # 删除文件
    @staticmethod
    def _clean_file(file):
        if os.path.exists(file):
            os.remove(file)
            # print("成功删除文件 {}".format(file))

    @staticmethod
    def _cut_image(xpos, w, h, filename):
        """
        指定窗口位置进行截图
        :param xpos:
        :param w:
        :param h:
        :return:
        """
        # print("当前x的坐标是 {}, w={}, h={},生成文件名为 {}".format(xpos, w, h, filename))
        # if xpos is None or w is None or h is None:
        #     # print("缺少必要的参数")
        #     return
        # # 将当前坐标进行截图
        # img = pyautogui.screenshot(region=[xpos[0], xpos[1], w, h])
        #
        # # 保存文件到指定文件中
        # real_name = "{}\{}".format(SAVE_PATH, filename)
        # img.save(real_name)
        #
        # return real_name
        pass

    @staticmethod
    def _read(image):
        pass
        # 这里接受一个图片的路径 进行识别
        # print("这里接受一个图片的路径 进行识别")
        # print("process file {}".format(image))
        # im = Image.open(image)
        # string = pytesseract.image_to_string(im)
        # return string

    # 检查指定区域是否相同 默认不相同
    @staticmethod
    def check_if_same(x, w, h):
        # 检查当前的文件是与1.png 是否相等
        first = "1.png"
        second = "2.png"
        a = "{}\{}".format(SAVE_PATH, first)

        if os.path.exists(a):
            b = PosUtil._cut_image(x, w, h, second)

            bresult = PosUtil._read(b)

            ret = PosUtil._read(a) == bresult
            PosUtil._clean_file(a)
            os.rename(b, a)
            return ret

        else:
            PosUtil._cut_image(x, w, h, first)
            return False


if __name__ == '__main__':
    x = (50, 94)
    w = 80
    h = 100

    r = PosUtil.check_if_same(x, w, h)

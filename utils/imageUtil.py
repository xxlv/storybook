#!/usr/bin/python3
# -*- coding:utf-8  -*-

# import cv2
from PIL import Image
import os
import time
import pyautogui

cv2 = None

def snapshot_image(xpos, w, h, filename):
    """
    指定窗口位置进行截图
    :param xpos:
    :param w:
    :param h:
    :return:
    """

    print("当前x的坐标是 {}, w={}, h={},生成文件名为 {}".format(xpos, w, h, filename))
    if xpos is None or w is None or h is None:
        print("缺少必要的参数")
        return
    # 将当前坐标进行截图
    img = pyautogui.screenshot(region=[xpos[0], xpos[1], w, h])

    # 保存文件到指定文件中
    img.save(filename)
    return filename


def crop_screenshot(img_file, pos_x, pos_y, width, height, out_file):
    """
    图片裁剪

    :param img_file:  原图片
    :param pos_x: X
    :param pos_y: Y
    :param width: 宽度
    :param height: 高度
    :param out_file: 输出文件
    :return:
    """

    img = Image.open(img_file)
    region = (pos_x, pos_y, pos_x + width, pos_y + height)
    crop_img = img.crop(region)
    crop_img.save(out_file)
    print("exported:", out_file)


def find_pos(screen, template):
    """
    返回指定区域的坐标

    :param screen: 小图
    :param template: 原图
    :return: 返回小图在原图的位置
    """
    image_x, image_y = template.shape[:2]
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.97:
        print("found max_val is {}".format(max_val))
        center = (max_loc[0] + image_y / 2, max_loc[1] + image_x / 2)
        return center
    else:
        return None


def image_mode_2(path):
    filename = os.path.split(path)[-1]
    full_path_list = os.path.split(path)
    image = Image.open(path)
    target = image.convert('L')

    target.save(os.path.join("/".join(full_path_list[0:-1])) + "/{}".format("L-{}".format(filename)))
    # threshold = 200
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    # target2 = target.point(table, "1")
    # target2.save(os.path.join("/".join(full_path_list[0:-1])) + "/{}".format("L2-{}".format(filename)))
    # os.remove(os.path.join("/".join(full_path_list[0:-1])) + "/{}".format("L-{}".format(filename)))


def _on_mouse(event, x, y, flags, param):
    global pts_2d, img
    # EVENT_LBUTTONDOWN 左键点击
    if event == cv2.EVENT_LBUTTONDOWN:
        pts_2d.append([x, y])
        cv2.circle(img, (x, y), 1, (0, 255, 0), -1)


if __name__ == '__main__':
    snapshot_image([0, 0], 1600, 1600, "/Users/lvxiang/PycharmProjects/hack/storybook/data/{}.png".format(time.time()))

if __name__ == '__main__':
    # pts_2d = []
    # path = "data/L-demo.jpg"
    # # image_mode_2(path)
    #
    # img = cv2.imread(path)
    # cv2.namedWindow('image')
    # cv2.setMouseCallback('image', _on_mouse)
    #
    # while 1:
    #     cv2.imshow("image", img)
    #     cv2.moveWindow("image", 100, 100)
    #     k = cv2.waitKey(1)
    #     if k == 27:
    #         cv2.destroyAllWindows()
    #         time.sleep(0.1)
    #         # 保存图片到data
    #         x = pts_2d[0][0]
    #         y = pts_2d[0][1]
    #         w = abs(pts_2d[1][0] - x) + 5
    #         h = abs(pts_2d[1][1] - y) + 5
    #         print(pts_2d)
    #         name = input("请输入裁剪名称...\n")
    #         if name is None or name.__len__() < 2:
    #             print("无效的名字，跳过")
    #             break
    #
    #         crop_screenshot(path, x, y, w, h, "data/{}.jpg".format(name))
    #         break
    #
    # if name is not None:
    #     screen = cv2.imread("data/{}.jpg".format(name))
    #     template = cv2.imread("data/L-demo.jpg")
    #     pos = find_pos(screen, template)
    #     if pos is None:
    #         print("无法验证改图片，请重新裁剪")
    #     else:
    #         print("恭喜🎉裁剪正确 ", pos)
    pass

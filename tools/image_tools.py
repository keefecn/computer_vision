#!/usr/bin/env python3
# encoding: utf-8
"""
@summary:
 打印图像通道信息： RGB/HSV
@since: 2020-5-31
@author: Keefe Wu
@requires: matplotlib
"""

__author__ = 'Keefe Wu'

import matplotlib.pyplot as plt


def get_image(path=''):
    img = plt.imread(path)
    print(type(img))
    if img.any() == None:  # judge image
        print('This file may not be available')
    return img


def base_rw(img):
    pass


def show_pie(img):
    # 饼图
    # plt.rcParams['font.sas-serif']=['SimHei']  # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    labels = 'frogs', 'hogs', 'dogs', 'logs'
    sizes = 15, 20, 45, 10
    colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
    explode = 0, 0.1, 0, 0
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()


def make_gray(img):
    img_r = img[:, :, 0]  # 取单通道-r通道
    plt.imshow(img_r)  # show
    plt.title('raw')
    plt.show()
    plt.imshow(img_r, cmap='Greys_r')  # gray
    plt.title('make_gray')
    plt.show()


def test(img):
    base_rw(img)
    # show_pie(img)
    make_gray(img)


def show_channels(img):
    """ show channel 打印通道 """
    import cv2
    def show_one_channel(channel, title=''):
        # 只打印一个通道 的图片
        plt.plot(channel[200, :])
        plt.title(title)
        plt.show()

    def show_rgb(img):
        """ 打印 RGB通道 """
        import matplotlib.pyplot as plt
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        fruits_all = [img, img[:, :, 0], img[:, :, 1], img[:, :, 2]]
        channels = ["RGB", "red", "green", "blue"]
        for i in range(4):  # 4个分量打印在一张图里，图像效果
            plt.subplot(2, 2, i + 1)  # subplot子图打印， 序号1,2,3,4
            plt.imshow(fruits_all[i], cmap=plt.cm.gray)
            plt.title(channels[i])
        plt.show()

        for fruit in fruits_all:  # 打印每个通道的值：  (行，列，色彩分量/通道数)
            print(fruit.shape)
        for i in range(4):  # 每个分量单独打印
            show_one_channel(fruits_all[i], channels[i])
            pass

    def show_hsl(img):
        """ 打印 HSL 通道 """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        channels = ["HSL", "Hue", "Solution", "Value"]
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            plt.imshow(img[i], cmap=plt.cm.gray)
            plt.title(channels[i])
        plt.show()

    print(img.shape)
    show_rgb(img)
    # show_hsl(img)


def show_click(img):
    """  根据mouse点击 显示坐标上的相应值 """
    import cv2
    def mouse_click(event, x, y, flags, para):
        if event == cv2.EVENT_LBUTTONDOWN:  # 左边鼠标点击
            print('\nPIX:', x, y)
            print("BGR:", img[y, x])
            print("RGB:", rgb[y, x])
            print("GRAY:", gray[y, x])
            print("HSV:", hsv[y, x])

        elif event == cv2.EVENT_RBUTTONDOWN:
            print("HSV(245,236)=[208.5246 0.516949 0.4627451]", hsv[236, 245])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.namedWindow("img")
    cv2.setMouseCallback("img", mouse_click)
    while True:
        cv2.imshow('img', img)
        if cv2.waitKey() == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img = get_image("..//data/test2.png")
    # test(img)
    show_channels(img)
    # show_click(img)

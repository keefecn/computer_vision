# -*- coding: utf-8 -*-
"""
@summary: show how to use cv2
@since: 2017-11-22
@author: Keefe Wu
@requires: opencv-python
@see: http://blog.csdn.net/liqiancao/article/details/55670749
"""
import cv2
import numpy as np


def get_image(path=''):
    """ read image """
    img = cv2.imread(path)  # flags Flag that can take values of cv::ImreadModes
    if not img.any():  # 判断图像是否存在
        print('This file may not be available')
    return img


def base_rw(img):
    cv2.imshow("1", img)

    # zeros 初始化
    empty_image = np.zeros(img.shape, np.uint8)
    # empty_image2 = img.copy()

    # make gray
    empty_image3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("empty_image3", empty_image3)

    cv2.waitKey(0)  # wait for show
    cv2.imwrite('new_image.jpg', img)

    cv2.destroyAllWindows()


def make_gray(img):
    # cv2.IMREAD_UNCHANGED 包含alpha通道（透明度）
    gray1 = cv2.imread("../../data/test2.png", cv2.IMREAD_GRAYSCALE)
    show_image(gray1)

    # 使用颜色转换函数: cv2.cvtColor
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #
    show_image(gray, "cvtColor_image.jpg")


def show_image(img, filename="show_image.jpg"):
    """
    显示图片
    :param img: <class 'numpy.ndarray'>
    :param filename:
    :return:
    """
    print("shape=", img.shape)
    print(img[9:11, 9:12])
    cv2.imshow(filename, img)
    # cv2.waitKey(0)  # wait for show


def test(img):
    base_rw(img)
    make_gray(img)


if __name__ == '__main__':
    img = get_image("../../data/test2.png")
    show_image(img)

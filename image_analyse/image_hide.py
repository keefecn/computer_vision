#!/usr/bin/env python
# encoding: utf-8
"""
@summary: 图像信息隐藏
方法1： 主要是用『修改像素奇偶性后，图片变化不明显』来实现的
从源图中提取文字图像信息，记录这个文字图像信息像素点在图像矩阵中的位置
对载体图片进行预处理，将B通道的像素值全部设置成偶数
把载体图片中，把第一步已经记录的位置的像素B通道设置为奇数
信息解码的过程就是逆过程，只要找出载体图片中B通道是奇数的像素位置，然后统一着色就可以恢复
@since: 2020-5-31
@author: Keefe Wu
@requires: matplotlib
"""

import cv2
import numpy as np


def image_encrypt(source_img_path='../data/image_hide/source.png',
                  carrier_img_path='../data/image_hide/carrier.png', message="Hello World!"):
    """

    :param source_img_path:  源图像，需要将message写入此图片
    :param carrier_img_path: 加载图像
    :param message:
    :return:
    """
    # 写入要隐藏的信息
    source = cv2.imread(source_img_path)
    h, w = source.shape[:2]
    x, y = (180, 250)
    color = [88, 26, 16]  # 文字格式~黑色
    cv2.putText(source, message, (x, y), cv2.QT_FONT_BLACK, 3, color, thickness=5)
    cv2.imwrite('../data/image_hide/source_txt.png', source)

    # 预处理载体图片
    carrier = cv2.imread(carrier_img_path)
    for i in range(h):
        for j in range(w):
            # 把整幅图的B通道全设置为偶数
            if carrier[i, j, 0] % 2 == 1:
                carrier[i, j, 0] -= 1

    # 把隐藏信息的位置设置成奇数
    for i in range(h):
        for j in range(w):
            # 找出有文字的位置
            if list(source[i, j]) == color:
                carrier[i, j, 0] += 1
    cv2.imwrite('../data/image_hide/hide.png', carrier)


def image_decrypt(hide_img_path='../data/image_hide/hide.png'):
    """
    信息恢复
    :param hide_img_path:
    :return:
    """
    img = cv2.imread(hide_img_path)
    h, w = img.shape[:2]
    # 新建一张图用来放解出来的信息
    info = np.zeros((h, w, 3), np.uint8)
    for i in range(h):
        for j in range(w):
            # 发现B通道为奇数则为信息的内容
            if img[i, j, 0] % 2 == 1:
                info[i, j, 0] = 255
                info[i, j, 1] = 255
                info[i, j, 2] = 255
    cv2.imwrite('info.png', info)


if __name__ == '__main__':
    # image_encrypt()
    image_decrypt()

# -*- coding: utf-8 -*-
'''
@summary: show how to use PIL
@since: 2019-7-20
@author: Keefe Wu
@requires: pillow
@see: 
'''

import numpy as np
from PIL import Image


def get_image(path=''):
    img = Image.open(path)
    print(type(img))
    if img == None:  # judge image 
        print ('This file may not be available')     
    return img


def base_rw(img):  
    img.show()  # 显示图像
    img_arr = np.array(img)  # 3维矩阵
    
    # 存储图像
    new_img = Image.fromarray(img_arr)
    # new_img.save('newimage.jpg')  # 如果不转矩阵可直接用'.save'保存

    
def make_gray(img):
    img.convert('L')
    img.show()
    
def img_rotate(img):
    h,w = 900, 900 
    #缩放
    img_resize = img.resize((h,w))
    #旋转
    img_r90 = img.rotate(90) #旋转90度
    img_transpose_tb = img.transpose(Image.FLIP_TOP_BOTTOM)#上下翻转
    img_transpose_lr = img.transpose(Image.FLIP_LEFT_RIGHT)#左右翻转
    img.show()
    
def test(img):  
    base_rw(img)
    # make_gray(img)
    img_rotate(img)
    
if __name__ == '__main__':
    img = get_image("../../data/test2.png")
    test(img)

# -*- coding: utf-8 -*-
'''
@summary: show how to use PIL
@since: 2019-7-20
@author: Keefe Wu
@requires: scikit-image
@see: 
'''
from skimage import io


def get_image(path=''):
    # 可以读取tif格式图片，保存之前要将数据转换成uint8，否则会报错。
    img = io.imread(path)
    print(type(img))
    if img.all() == None:  # judge image 
        print ('This file may not be available')     
    return img


def base_rw(img):  
    io.imshow(img)
    io.show() 
    io.imsave('new_img.tif', img)

    
def make_gray(img):
    pass

    
def test(img):  
    base_rw(img)

    
if __name__ == '__main__':
    img = get_image("../../data/test2.png")
    test(img)

# -*- coding: utf-8 -*-
'''
@summary: show how to use cv2
@since: 2017-11-22
@author: Keefe Wu
@requires: opencv-python
@see: http://blog.csdn.net/liqiancao/article/details/55670749
'''
import cv2  
import numpy as np  


def get_image(path=''):
    img = cv2.imread(path)
    if img == None:               #判断图像是否存在
        print ('This file may not be available')     
    return img


def base_rw(img):  
    cv2.imshow("1", img)  
    
    # 
    emptyImage = np.zeros(img.shape, np.uint8)  
    
    # make gray
    emptyImage2 = img.copy()   
    emptyImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    cv2.imshow("EmptyImage3", emptyImage3)  
    
    cv2.waitKey (0) # wait for show
    cv2.imwrite('new_image.jpg',img)
    
    cv2.destroyAllWindows() 

def make_gray(img):
    gray = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE) #cv2.IMREAD_UNCHANGED 包含alpha通道（透明度）
    #使用颜色.cvtColor
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 转换函数cv2

def test(img):  
    base_rw(img)
    make_gray(img)
    
if __name__ == '__main__':
    img = get_image("../../data/test2.png")
    test(img)
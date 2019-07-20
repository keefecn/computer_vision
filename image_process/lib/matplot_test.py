#!/usr/bin/env python 
# encoding: utf-8 
'''
@summary: show how to use matplotlib.pyplot
@since: 2017-11-22
@author: Keefe Wu
@requires: matplotlib
'''
__author__ = 'Keefe Wu'

import matplotlib.pyplot as plt


def get_image(path=''):
    img = plt.imread(path)
    print(type(img))
    if img.any() == None:  # judge image 
        print ('This file may not be available')     
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
    plt.show()
    plt.imshow(img_r, cmap='Greys_r')  # gray
    plt.show()    

    
def test(img):  
    base_rw(img)
    # show_pie(img)
    make_gray(img)

        
if __name__ == '__main__':
    img = get_image("../../data/test2.png")
    test(img)
    

# coding: utf-8  
"""
@summary: show how to use 
@since: 2017-11-22
@author: Keefe Wu
@requires: cv2
@see: http://blog.csdn.net/topgun_chenlingyun/article/details/10582641
https://blog.csdn.net/qq_36941368/article/details/82998296
  [ x for x in dir(cv2) if 'CV' in x ]
"""

import cv2  
import numpy as np  
  
# 原始图片  cv3 use cv2.IMREAD_COLOR --> cv2.CV_LOAD_IMAGE_COLOR, 
image = cv2.imread('../data/beauty.png', cv2.IMREAD_COLOR)  
cv2.imshow('Original image', image)  

# 截取图片的一部分，即ROI(region of interest)  
# 因为在python cv2中图片以ndarray格式表示，所以直接用ndarray的  
# 分片方式能非常容易的截取ROI，跟python中list的分片用法一样，只不过  
# 这个是在二维数组上分片  
crop = image[0:201, 100:301]  # 分片都是不包含后面一个参数的，所以多1  
cv2.imshow('Crop image', crop)  
cv2.imwrite('../output/beauty_crop.jpg', crop)  

# 处理过的灰度图片  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
cv2.imshow('Gray image', gray)  
cv2.imwrite('../output/beauty_gray.jpg', gray)  
  
# 在图片上画一个框  
imageRect = image.copy()  
p1 = (300, 200)  
p2 = (500, 300)  
color = (0, 0, 255)  # BGR的顺序，这个颜色为红色  
cv2.rectangle(imageRect, p1, p2, color)  
cv2.imshow('Rectangle an image', imageRect)  
cv2.imwrite('../output/beauty_rect.jpg', imageRect)  
  
# 图片缩放  
size = (400, 300)  
imageResize = cv2.resize(image, size)  
# 可以不指定缩放的图片大小，而指定缩放比例，如下，等比缩放到一半大小  
# 即将缩放尺寸设为0,然后再分别设定xy方向上的缩放比例  
# imageResize = cv2.resize(image, (0,0), fx=0.5, fy=0.5)  
cv2.imshow('Resize an image', imageResize)  
cv2.imwrite('../output/beauty_resize.jpg', imageResize)  
  
# 保留单一通道色彩，通道顺序是BGR  
# b = image.copy()  
# b[:,:,1] = 0  
# b[:,:,2] = 0  
# cv2.imshow('Blue image', b)  
# cv2.imwrite('../output/beauty_blue.jpg', b)  
#   
# g = image.copy()  
# g[:,:,0] = 0  
# g[:,:,2] = 0  
# cv2.imshow('Green image', g)  
# cv2.imwrite('../output/beauty_green.jpg', g)  
#   
# r = image.copy()  
# r[:,:,1] = 0  
# r[:,:,0] = 0  
# cv2.imshow('Red image', r)  
# cv2.imwrite('../output/beauty_red.jpg', r)  
  
# 改变对比度和亮度  
# 公式  
# result = ori*alpha + beta  
# ndarray是直接支持乘法和加法操作的，但是要注意  
# 乘加后的结果必须在[0,255]范围内，所以稍做一下处理  
alpha = 2  
beta = -200  
# result1 = image*2 - 200 #直接这么处理会有问题，会不在范围  
p = []  
for i in range(256):  
    p.append(max(min(round(alpha * i + beta), 255), 0))  
parray = np.array(p, np.uint8)  
result = parray[image]  
cv2.imshow('Change contrast and brightness', result)  
cv2.imwrite('../output/beauty_contrast_brightness.jpg', result)  
  
# 显示文字  
# 字体：FONT_HERSHEY_COMPLEX  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_COMPLEX', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_COMPLEX' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_COMPLEX_SMALL  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_COMPLEX_SMALL', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_COMPLEX_SMALL' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_DUPLEX  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_DUPLEX, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_DUPLEX', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_DUPLEX' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_PLAIN  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_PLAIN', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_PLAIN' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_SCRIPT_COMPLEX  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_SCRIPT_COMPLEX', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_SCRIPT_COMPLEX' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_SCRIPT_SIMPLEX  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_SCRIPT_SIMPLEX', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_SCRIPT_SIMPLEX' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_SIMPLEX  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_SIMPLEX', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_SIMPLEX' + '.jpg', imageText)  
  
# 字体：FONT_HERSHEY_TRIPLEX  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_TRIPLEX, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_HERSHEY_TRIPLEX', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_HERSHEY_TRIPLEX' + '.jpg', imageText)  
  
# 字体：FONT_ITALIC  
imageText = image.copy()  
cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_ITALIC, 4, (255, 0 , 0), thickness=4, lineType=8)  
cv2.imshow('Show text FONT_ITALIC', imageText)  
cv2.imwrite('../output/beauty_text_' + 'FONT_ITALIC' + '.jpg', imageText)  
  
# 退出窗口  
k = cv2.waitKey(0)  
if k == ord('s'):  # wait for 's' key to save and exit
    # cv2.imwrite('messigray.png',img)
    pass
cv2.destroyAllWindows()

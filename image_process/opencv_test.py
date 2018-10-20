# -*- coding: utf-8 -*-
import cv2  
import numpy as np  
'''
@summary: show how to use cv2
@since: 2017-11-22
@author: Keefe Wu
@see: http://blog.csdn.net/liqiancao/article/details/55670749
'''
 
img = cv2.imread("../data/test2.png")  
cv2.imshow("1", img)  

# 
emptyImage = np.zeros(img.shape, np.uint8)  

# make gray
emptyImage2 = img.copy()   
emptyImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
cv2.imshow("EmptyImage3", emptyImage3)  

cv2.waitKey (0)  
cv2.destroyAllWindows() 

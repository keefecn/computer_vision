# coding: utf-8 
'''
@summary:  image process
@since: 2019/7/17
@author: Keefe Wu
@requires: libtiff scipy
@see: 
'''
import os
import numpy as np

from scipy import misc
from PIL import Image
from libtiff import TIFF 

# 读入已有图像,数据类型和原图像一致
tif32 = misc.imread('.\test\lena32.tif')  # <class 'numpy.float32'>
tif16 = misc.imread('.\test\lena16.tif')  # <class 'numpy.uint16'>
tif8 = misc.imread('.\test\lena8.tif')  # <class 'numpy.uint8'>
# 产生随机矩阵,数据类型float64
np.random.seed(12345)
flt = np.random.randn(512, 512)  # <class 'numpy.float64'>
# 转换float64矩阵type,为后面作测试
z8 = (flt.astype(np.uint8))  # <class 'numpy.uint8'>
z16 = (flt.astype(np.uint16))  # <class 'numpy.uint16'>
z32 = (flt.astype(np.float32))  # <class 'numpy.float32'> 


def tiff_to_image_array(tiff_image_name, out_folder, out_type): 
    """
    tiff文件解析成图像序列
    :params tiff_image_name：tiff文件名
    :params out_folder：保存图像序列的文件夹
    :params out_type:保存图像的类型，如.jpg、.png、.bmp等
    :return
    """          
    from libtiff import TIFF
    from scipy import misc    
    tif = TIFF.open(tiff_image_name, mode="r")
    idx = 0
    for im in list(tif.iter_images()):
        #
        im_name = out_folder + str(idx) + out_type
        misc.imsave(im_name, im)
        print (im_name, 'successfully saved!!!')
        idx = idx + 1
    return
 

def image_array_to_tiff(image_dir, file_name, image_type, image_num):
    """
          图像序列保存成tiff文件
    :params image_dir：图像序列所在文件夹
    :params file_name：要保存的tiff文件名
    :params image_type:图像序列的类型
    :params image_num:要保存的图像数目    
    :return    
    """
    from libtiff import TIFF
    out_tiff = TIFF.open(file_name, mode='w')
    
    # 这里假定图像名按序号排列
    for i in range(0, image_num):
        image_name = image_dir + str(i) + image_type
        image_array = Image.open(image_name)
        # 缩放成统一尺寸
        img = image_array.resize((480, 480), Image.ANTIALIAS)
        out_tiff.write_image(img, compression=None, write_rgb=True)
        
    out_tiff.close()
    return 


def tiff_to_read(tiff_image_name):  
    # tiff文件解析成图像序列：读取tiff图像
    tif = TIFF.open(tiff_image_name, mode="r")  
    im_stack = list()
    for im in list(tif.iter_images()):  
        im_stack.append(im)
    return  
    # 根据文档,应该是这样实现,但测试中不管是tif.read_image还是tif.iter_images读入的矩阵数值都有问题
  

def write_to_tiff(tiff_image_name, im_array, image_num):
    # 图像序列保存成tiff文件：保存tiff图像   
    with TIFF.open(tiff_image_name, mode='w') as out_tiff: 
        for i in range(0, image_num):  
            im = Image.fromarray(im_array[i])
            # 缩放成统一尺寸  
            im = im.resize((480, 480), Image.ANTIALIAS)  
            out_tiff.write_image(im, compression=None)     
    return   


def tif_to_jpg(inputfile='', outfile=''):
    from PIL import Image
    print('tif_to_jpg: %s, %s' % (inputfile, outfile))
    im = Image.open(inputfile)
    im.save(outfile)    


if __name__ == '__main__':
    tif_to_jpg(inputfile='/Users/jowang/Pictures/wbh5.tiff', outfile='/Users/jowang/Pictures/wbh5.jpg')  
      

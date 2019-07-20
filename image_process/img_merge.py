# coding: utf-8 
'''
@summary:  图片合并成pdf
@since: 2019/7/17
@author: Keefe Wu
@requires: reportlab
@see: 
'''

import os

from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


def image_to_pdf(filepath, newpath):
    """ 将图片转化成pdf，支持jpg/tif/png/... """
    (w, h) = landscape(A4)
    c = canvas.Canvas(newpath, pagesize=landscape(A4))
    c.drawImage(filepath, 0, 0, w, h)
    c.save()


if __name__ == '__main__':
    # filepath = r'E:\ebook\hot\images\industry\2016年服务外包业务结构.png'
    filepath = r'E:\ebook\hot\images\经济学可视化图表\中国经济统计图表\中国人口年龄结构（2010年）.TIF'
    newpath = os.path.join(r'C:\Users\keefe\Pictures\tmp', os.path.basename(filepath) + '.pdf')
    print(newpath)
    image_to_pdf(filepath, newpath)

    print('ok')

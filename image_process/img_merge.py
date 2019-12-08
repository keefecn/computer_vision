# coding: utf-8 
'''
@summary:  图片合并成pdf
@since: 2019/7/17
@author: Keefe Wu
@requires: reportlab PIL img2pdf
@see: 
@note: 
convert_pdf_size: img2pdf < reportlab < PIL 
'''

import os


def image_to_pdf_by_reportlab(filepath, newpath):
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.pdfgen import canvas    
    """ 将图片转化成pdf，支持jpg/tif/png/... """
    (w, h) = landscape(A4)
    c = canvas.Canvas(newpath, pagesize=landscape(A4))
    c.drawImage(filepath, 0, 0, w, h)
    c.save()
    return newpath


def image_to_pdf_by_pillow(filepath, newpath):
    from PIL import Image
    img = Image.open(filepath)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    img.save(newpath, 'pdf', resolution=100.0, save_all=True, append_images=[img])

    
def image_to_pdf(filepath, newpath):
    """ img2pdf 支持多页tif """
    import img2pdf  
    with open(newpath, 'wb') as f:
        f.write(img2pdf.convert(filepath))

    
if __name__ == '__main__':
    # filepath = r'E:\ebook\hot\images\industry\2016年服务外包业务结构.png'
    filepath = r'E:\ebook\hot\images\经济学可视化图表\中国经济统计图表\中国人口年龄结构（2010年）.TIF'
    newpath = os.path.join(r'C:\Users\keefe\Pictures\tmp', os.path.basename(filepath) + '.pdf')
    print(newpath)
    image_to_pdf_by_reportlab(filepath, newpath)
    # image_to_pdf_by_pillow(filepath, newpath)
    # image_to_pdf(filepath, newpath) 

    print('ok')

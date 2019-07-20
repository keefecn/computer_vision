# coding: utf-8 
'''
@summary:  图片合并成pdf
@since: 2019/7/17
@author: Keefe Wu
@requires: PyPDF2 PyMUPDF
@see: https://blog.csdn.net/u013421629/article/details/77703582
'''

import os
import time
from PyPDF2 import PdfFileReader, PdfFileWriter

from image_process import file_extension


def get_filename(filepath, filetypes=['.pdf']):
    """  get_filename
        使用os.walk 或者 os.list，搜索出某目录下的全部指定类型文件
    """
    file_list = []
    for root, _dirs, files in os.walk(filepath):
#         for filespath in files:
#             if file_extension(filespath) in filetypes:
#                 file_list.append(os.path.join(root, filespath))
        file_list = [ os.path.join(root, filespath)  for filespath in files if file_extension(filespath) in filetypes]            
    print('filenums=%d' % len(file_list))
    return file_list


def merge_pdf(filepath, outfilename='.merge.pdf'):
    """ merge_pdf
        合并同一个文件夹下所有PDF文件
    :return: outfile 输出压缩后的pdf全路径
    """
    filepath_2nd = os.path.dirname(filepath)
    filename = os.path.basename(filepath) + outfilename
    outfile = os.path.join(filepath_2nd, filename)

    pdfwriter = PdfFileWriter()
    outputPages = 0
    pdf_files = get_filename(filepath, filetypes=['.pdf'])
    for _file in pdf_files:
        pdreader = PdfFileReader(open(_file, 'rb'))
        if pdreader.isEncrypted == True:  
            pdreader.decrypt("map")  # 如果pdf文件已经加密，必须首先解密才能使用pyPdf
                        
        pageCount = pdreader.getNumPages()  # 获得源pdf文件中页面总数
        outputPages += pageCount
        print(_file, pageCount)
        # 分别将page添加到输出output中
        for iPage in range(0, pageCount):
            pdfwriter.addPage(pdreader.getPage(iPage))
    print("All Pages Number:" + str(outputPages))
    
    with open(outfile, "wb") as f:
        pdfwriter.write(f)
    print('outfile=%s' % outfile)        
    return outfile


def pdf_to_image_by_poppler(pdf_path=''):
    from pdf2image import convert_from_path  # 依赖 poppler
    pages = convert_from_path(pdf_path, 300, "output", fmt="JPEG", output_file="essay", thread_count=1)
    for i in range(0, len(pages)):  
        pages[i].save('image{i+1}.png', 'PNG')  


def pdf_to_image_by_wand(pdf_path=''):
    from wand.image import Image  # 依赖 imagemagick
    image_pdf = Image(filename=pdf_path, resolution=300)
    image_jpeg = image_pdf.convert('jpg')
    # wand已经将PDF中所有的独立页面都转成了独立的二进制图像对象。遍历image_jpeg
    req_image = [Image(image=img).make_blob('jpg') for img in image_jpeg.sequence ]
    out_filepath = os.path.dirname(pdf_path)
    out_file_prefix = os.path.basename(pdf_path)    
    i = 0
    for img in req_image:  # 遍历req_image,保存为图片文件
        i += 1
        imgname = os.path.join(out_filepath, "{}_{}.jpg".format(out_file_prefix, i))
        with open(imgname, 'wb') as ff:
            ff.write(img)


def pdf_to_image_by_pymupdf(pdf_path=''):
    import fitz  # 依赖 PyMUPDF, ok
    import glob
    pdffile = glob.glob(pdf_path)[0]
    doc = fitz.open(pdffile)
    pagecount = doc.pageCount
    out_filepath = os.path.dirname(pdf_path)
    out_file_prefix = os.path.basename(pdf_path)
    for pg in range(0, pagecount):
        page = doc[pg]
        zoom = int(100)
        rotate = int(0)
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        imgname = os.path.join(out_filepath, "{}_{}.png".format(out_file_prefix, pg + 1))
        print(imgname)
        pm.writePNG(imgname)


def pic2pdf_by_pymupdf(img_path):
    import fitz  # 依赖 PyMUPDF, ok
    import glob    
    doc = fitz.open()   
    for img in sorted(glob.glob(img_path)):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档
    if os.path.exists("allimages.pdf"):
        os.remove("allimages.pdf")
    doc.save("allimages.pdf")  # 保存pdf文件
    doc.close()

            
if __name__ == '__main__':
    time1 = time.time()
    file_dir = r'C:\Users\keefe\Pictures\tmp'
    out_file = merge_pdf(file_dir)
    # out_file = r'C:\Users\keefe\Pictures\tmp.merge.pdf'
    # pdf_to_image_by_wand(out_file)
    # pdf_to_image_by_pymupdf(out_file)
    print ('总共耗时：%.4f seconds' % (time.time() - time1))


# coding: utf-8 
"""
@summary:  image process
@since: 2019/7/17
@author: Keefe Wu
@requires: 
@see: 

"""

import os


def file_extension(path): 
    return os.path.splitext(path)[1].lower()
 

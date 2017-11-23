#!/usr/bin/env python 
# encoding: utf-8 
'''
@summary: show how to use matplotlib.pyplot
@since: 2017-11-22
@author: Keefe Wu
'''
__author__ = 'Keefe Wu'

import matplotlib.pyplot as plt

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

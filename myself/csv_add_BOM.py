#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################################################################
#
#
# name:		csv_add_BOM
# author：	slnamurv
# function：将所在目录下所有csv文件转换为带Bom头的csv文件，不改变编码
# version：	1.0.0
# updated:	16/08/23
# env:		python 2.7.12
#
#
#####################################################################

import os
import time
import pandas as pd
from urllib import unquote

# 初始化列表
csvfilenames = []

# 获取当前目录下的csv文件
filenames = os.listdir(os.getcwd())  # os.getcwd()的作用是返回一个表示当前工作目录的字符串
# print filenames

for name in filenames:
    # print name
    if '.csv' in name:
        # print name[:-4]
        csvfilenames.append(name)

# print csvfilenames
# print csvfilenames[0]

# 转换文件
for csv in csvfilenames:
    print csv + u' 转换中'
    start_time = time.clock()
    data = pd.read_csv(csv, )
    data.to_csv(csv, encoding='utf_8_sig')
    end_time = time.clock()
    print csv + u' 转换完毕'
    print u'本次转换耗时 ' + str(end_time - start_time) + u' 秒'

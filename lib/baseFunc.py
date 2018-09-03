#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 9:24
# @Author  : NooneLiu
# @File    : baseFunc.py
# @Desc    :

import time
import os

def genLogFile(mode):
    '''
    :param mode: 文件读写方式，'r','w','a','r+','w+'等。
    :return: 返回文件对象
    '''
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 工程根目录下的report文件夹的绝对路径
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\report\\'
    fullpath = path + 'TestResult' + now + '.html'
    fp = open(fullpath, mode)
    return fp
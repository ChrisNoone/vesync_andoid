#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 9:47
# @Author  : NooneLiu
# @File    : doElement.py
# @Desc    :


def is_element_exist(driver,type,param):
    """
    判断元素是否存在
    :param driver:
    :param type: 元素定位方式
    :param param:
    :return: True or False
    """
    els = []
    if type=='id':
        els = driver.find_elements_by_id(param)
    elif type=='name':
        els = driver.find_elements_by_name(param)
    elif type=='xpath':
        els = driver.find_elements_by_xpath(param)
    else:
        print '不支持%s定位'%type

    if len(els)==0:
        return False
    elif len(els)==1:
        return True
    else:
        print "找到多个相同元素..."
        return False
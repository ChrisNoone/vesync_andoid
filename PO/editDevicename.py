#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 14:32
# @Author  : AnnaFu
# @File    : editDevicename.py
# @Desc    :

from time import time,sleep
from PO import *
from commons import *

class editDevicename_page():

    def __init__(self,driver):
        self.driver = driver

    #  按顺序修改设备列表所有设备的名字，设备名字为：device_1-device_n
    def edit_Devicename(self,):
        driver = self.driver
        # find_elements定位到的是一组元素，返回的是list队列
        els = driver.find_elements_by_id('com.etekcity.vesyncplatform:id/main_device_list_name')
        if len(els) == 0:
            print u'设备列表没有设备，请先添加设备'
        else:
            for i in range(len(els)):
                els[i].click()
                sleep(5)
                driver.find_element_by_xpath("//android.widget.TextView[@text='Schedule']/../../../../../../preceding-sibling::android.view.ViewGroup/android.view.ViewGroup[3]").click()  # 定位设置按钮按钮
                sleep(3)
                driver.find_element_by_name('Device Name').click()  # 定位'Device Name'按钮
                sleep(3)
                driver.find_element_by_xpath("//android.widget.TextView[@text='Historical input']/preceding-sibling::android.view.ViewGroup/preceding-sibling::android.widget.EditText").send_keys('device_%s'%i)  # 定位设备名字输入框
                sleep(3)
                driver.find_element_by_name('Save').click()  # 定位'Save'按钮
                sleep(3)
                driver.find_element_by_xpath("//android.widget.TextView[@text='Device Setting']/../preceding-sibling::android.view.ViewGroup").click()  # 定位'我的'页面的返回按钮
                sleep(3)
                driver.find_element_by_xpath("//android.widget.TextView[@text='Schedule']/../../../../../../preceding-sibling::android.view.ViewGroup/android.view.ViewGroup[1]").click()  # 定位设置页面的返回按钮
                sleep(3)
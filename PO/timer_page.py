#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 18:20
# @Author  : AnnaFu
# @File    : addTimer.py
# @Desc    :

from time import time,sleep
from PO import *
from commons import *

class addTimer_page():

    def __init__(self,driver):
        self.driver = driver

    def add_Timer(self,devicename):
        driver = self.driver
        driver.find_element_by_xpath("//*[@text=%s]"%devicename).click()  # 通过设备名称，进入上设备详情页
        # driver.find_element_by_name("%s"%devicename).click()
        sleep(5)
        driver.find_element_by_name('Timer').click()
        sleep(5)
        flag = doElement.is_element_exist(driver,'name',"Set Timer")  # 用Set Timer判断是否已存在Timer
        if flag:
            addTimer_page.buildTimer(self)  # 没有Timer时，直接新建Timer
            return u'新建Timer成功'
        else:
            driver.find_element_by_xpath("//android.widget.TextView[@text='Timer']/../../../../../following-sibling:: android.view.ViewGroup").click()  # 定位已存在的Timer
            sleep(3)
            driver.find_element_by_name('Delete').click()  # 删除已存在的Timer
            sleep(3)
            addTimer_page.buildTimer(self)  # 新建Timer
            return u'Timer任务已存在，删除后新建Timer'

    #  新建Timer
    def buildTimer(self):
        driver = self.driver
        driver.find_element_by_name('Set Timer').click()  # 定位Set Timer
        sleep(3)
        driver.find_element_by_name('Save').click()  # 定位Save
        sleep(3)

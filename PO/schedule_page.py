#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 14:56
# @Author  : AnnaFu
# @File    : addSchedule_page.py
# @Desc    :

from time import time,sleep
from PO import *

class addSchedule_page():

    def __init__(self,driver):
        self.driver = driver

    #  name是设备的名称，手机的时候为12小时制
    #  Start时间是最小值（AM），End时间是最大值（PM），状态为默认状态：开始时开启设备（On），结束时关闭设备（Off）

    def add_Schedule_12(self,devicename,):  # 设备名称作为参数传入
        driver = self.driver
        sleep(3)
        driver.find_element_by_xpath("//*[@text='%s']"%devicename).click()  # 通过设备名称，进入上设备详情页
        sleep(5)
        driver.find_element_by_name('Create Schedule').click()
        # driver.find_element_by_xpath("//*[@text='Create Schedule']").click()  # 点击创建schedule
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Start']").click()  # 点击Start
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([200.0,860.0],[200.0,1200.0],[720,1280])  # 滑动设置小时一栏，小时滑到最小值：01
        sleep(2)
        # swipeScreen.swipeScreen(self.driver).swipeScreen_Point([200.0,1000.0],[200.0,940.0],[720,1280])  # 滑动设置小时一栏，一次滑动1小时
        # sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,860.0],[350.0,1220.0],[720,1280])  # 滑动设置分钟一栏，小时滑到最小值：00，默认是AM，不需要滑动设置
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,860.0],[350.0,1220.0],[720,1280])
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,860.0],[350.0,1220.0],[720,1280])
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,860.0],[350.0,1220.0],[720,1280])
        sleep(2)
        # swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,1200.0],[350.0,940.0],[720,1280])  # 滑动设置分钟一栏，一次滑动5分钟
        # sleep(2)
        clickOn.clickOn_X_Y(self.driver).clickOn_x_y([680.0,800.0],[720,1280])  # 保存Start时间
        sleep(2)
        driver.find_element_by_xpath("//*[@text='End']").click()  # 点击End
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([200.0,1200.0],[200.0,900.0],[720,1280])  # 滑动设置小时一栏，小时滑到最大值：12
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,1200.0],[350.0,100.0],[720,1280])  # 滑动设置分钟一栏，小时滑到最大值：59
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([350.0,1200.0],[350.0,100.0],[720,1280])
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([500.0,1200.0],[500.0,900.0],[720,1280])  # 滑动选择PM
        sleep(2)
        clickOn.clickOn_X_Y(self.driver).clickOn_x_y([680.0,800.0],[720,1280])  # 保存End时间
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Repeat']").click()  # 点击Repeat
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Every Day']").click()  # 点击Every Day
        sleep(2)
        clickOn.clickOn_X_Y(self.driver).clickOn_x_y([40.0,100.0],[720,1184])  # 点击返回保存按钮，[720,1184]是SONY手机的屏幕尺寸
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Save']").click()  # 点击Save
        sleep(5)

    #  name是设备的名称，手机的时候为24小时制
    #  Start时间是最小值，End时间是最大值，状态为默认状态：开始时开启设备（On），结束时关闭设备（Off）

    def add_Schedule_24(self,devicename,):  # 设备名称作为参数传入
        driver = self.driver
        sleep(3)
        driver.find_element_by_xpath("//*[@text='%s']"%devicename).click()  # 通过设备名称，进入上设备详情页
        sleep(5)
        driver.find_element_by_name('Create Schedule').click()
        # driver.find_element_by_xpath("//*[@text='Create Schedule']").click()  # 点击创建schedule
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Start']").click()  # 点击Start
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([300.0,860.0],[300.0,1200.0],[720,1280])  # 滑动设置小时一栏，小时滑到最小值：00
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([400.0,860.0],[400.0,1220.0],[720,1280])  # 滑动设置分钟一栏，小时滑到最小值：00，默认是AM，不需要滑动设置
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([400.0,860.0],[400.0,1220.0],[720,1280])
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([400.0,860.0],[400.0,1220.0],[720,1280])
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([400.0,860.0],[400.0,1220.0],[720,1280])
        sleep(2)
        clickOn.clickOn_X_Y(self.driver).clickOn_x_y([680.0,800.0],[720,1280])  # 保存Start时间
        sleep(2)
        driver.find_element_by_xpath("//*[@text='End']").click()  # 点击End
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([300.0,1200.0],[300.0,100.0],[720,1280])  # 滑动设置小时一栏，小时滑到最大值：23
        sleep(2)
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([400.0,1200.0],[400.0,100.0],[720,1280])  # 滑动设置分钟一栏，小时滑到最大值：59
        swipeScreen.swipeScreen(self.driver).swipeScreen_Point([400.0,1200.0],[400.0,100.0],[720,1280])
        sleep(2)
        clickOn.clickOn_X_Y(self.driver).clickOn_x_y([680.0,800.0],[720,1280])  # 保存End时间
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Repeat']").click()  # 点击Repeat
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Every Day']").click()  # 点击Every Day
        sleep(2)
        clickOn.clickOn_X_Y(self.driver).clickOn_x_y([40.0,100.0],[720,1184])  # 点击返回保存按钮，[720,1184]是SONY手机的屏幕尺寸
        sleep(2)
        driver.find_element_by_xpath("//*[@text='Save']").click()  # 点击Save
        sleep(5)

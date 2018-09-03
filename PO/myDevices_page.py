#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 11:02
# @Author  : NooneLiu
# @File    : myDevices_page.py
# @Desc    : 设备列表页

from commons import swipeScreen

class myDevices_page():
    '''设备列表页'''
    def __init__(self,driver):
        self.driver = driver

    def get_addDevices(self):
        '''定位右上角添加设备按钮'''
        el = self.driver.find_element_by_id('com.etekcity.vesyncplatform:id/ek_cp_toolbar_right')
        return el

    def get_myDevices(self):
        '''定位下方导航栏My Devices按钮'''
        el = self.driver.find_elements_by_id("com.etekcity.vesyncplatform:id/ll_tap")[0]
        return  el

    def get_Notifications(self):
        '''定位下方导航栏Notifications按钮'''
        el = self.driver.find_elements_by_id("com.etekcity.vesyncplatform:id/ll_tap")[1]
        return el

    def get_Notifications(self):
        '''定位下方导航栏More按钮'''
        el = self.driver.find_elements_by_id("com.etekcity.vesyncplatform:id/ll_tap")[2]
        return el

    def get_OnOff(self,devicename):
        '''通过设备名称定位设备列表中开关按钮'''
        xpath = "//android.widget.TextView[@text='" + devicename + \
                "']/../following-sibling::android.widget.FrameLayout/android.widget.ImageButton"
        if(self.driver.find_element_by_xpath(xpath).is_displayed()):
            el = self.driver.find_element_by_xpath(xpath)
            return el
        else:
            print "未找到按钮."

    def do_refresh(self):
        '''下拉刷新设备列表页面'''
        swipeScreen.swipeScreen(self.driver).swipeScreen_Down()

    def do_intoDevice(self,devicename):
        '''点击进入指定设备详情页'''
        xpath = "//android.widget.TextView[@text='" + devicename + \
                "']/.."
        self.driver.find_element_by_xpath(xpath).click()
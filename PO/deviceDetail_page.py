#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 16:06
# @Author  : NooneLiu
# @File    : deviceDetail_page.py
# @Desc    : 设备详情页

from commons import doElement

class deviceDetail_page():
    '''设备详情页'''
    def __init__(self,driver):
        self.driver = driver

    def get_return(self):
        '''定位左上角返回按钮'''
        xpath = "//*[@class='android.widget.ScrollView']/preceding-sibling::android.view.ViewGroup\
                /android.view.ViewGroup[1]/android.view.ViewGroup"
        el = self.driver.find_element_by_xpath(xpath)
        return el

    def get_configration(self):
        '''定位右上角设备配置按钮'''
        xpath = "//*[@class='android.widget.ScrollView']/preceding-sibling::android.view.ViewGroup\
                /android.view.ViewGroup[3]/android.view.ViewGroup"
        el = self.driver.find_element_by_xpath(xpath)
        return el

    def get_Onoff(self):
        '''定位开关按钮'''
        xpath = "//android.widget.TextView[@text='ACTIVE TIME']/../preceding-sibling::android.view.ViewGroup"
        el = self.driver.find_element_by_xpath(xpath)
        return el

    def get_intoEnergy(self):
        '''定位进入电量按钮'''
        xpath = "//android.widget.TextView[@text='ACTIVE TIME']/following-sibling::android.widget.ImageView"
        el = self.driver.find_element_by_xpath(xpath)
        return el

    def get_Timer(self):
        '''定位Timer按钮'''
        el = self.driver.find_element_by_name('Timer')
        return el

    def get_Schedule(self):
        '''定位Schedule按钮'''
        el = self.driver.find_element_by_name('Schedule')
        return el

    def get_Away(self):
        '''定位Away按钮'''
        el = self.driver.find_element_by_name('Away')
        return el

    def get_CreateSchedule(self):
        '''定位Create Schedule按钮'''
        if doElement.is_element_exist(self.driver,'name','Create Schedule'):
            el = self.driver.find_element_by_name('Create Schedule')
            return el
        else:
            print '元素不存在'
            return None

    def get_SetTimer(self):
        '''定位Set Timer按钮'''
        if doElement.is_element_exist(self.driver,'name','Set Timer'):
            el = self.driver.find_element_by_name('Set Timer')
            return el
        else:
            print '元素不存在'
            return None

    def get_SetAwayMode(self):
        '''定位Set Away Mode按钮'''
        if doElement.is_element_exist(self.driver,'name','Set Away Mode'):
            el = self.driver.find_element_by_name('Set Away Mode')
            return el
        else:
            print '元素不存在'
            return None
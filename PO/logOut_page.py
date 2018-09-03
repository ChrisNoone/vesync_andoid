#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 17:27
# @Author  : AnnaFu
# @File    : logOut_page.py
# @Desc    :

import time

class logOut_page():

    def __init__(self,driver):
        self.driver = driver

    def log_Out(self):
        # 退出登录功能
        driver = self.driver
        driver.find_element_by_name('More').click()  # 点击Mor按钮
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='Link to Alexa']/../preceding-sibling:: android.widget.LinearLayout").click()  # 点击'我的'
        time.sleep(2)
        account = driver.find_element_by_id('com.etekcity.vesyncplatform:id/more_user_info_mail').text
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/more_user_info_logout').click()  # 点击logOut按钮
        time.sleep(2)
        driver.find_element_by_id('android:id/button1').click()  # 点击确认退出登录
        time.sleep(2)
        return account
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 11:53
# @Author  : AnnaFu
# @File    : logIn_page.py
# @Desc    :
# coding=utf-8

import time

class logIn_page():

    def __init__(self,driver):
        self.driver = driver

    def log_In(self,account,password):
        # 登录功能
        driver = self.driver
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/btn_guide_sign_in').click()  # 点击登录按钮
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/sign_in_input_account').send_keys('%s'%account)  # 输入账号
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/sign_in_input_password').send_keys('%s'%password)  # 输入密码
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/sign_in_submit').click()  # 点击登录按钮
        time.sleep(2)

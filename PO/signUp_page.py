#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 11:12
# @Author  : AnnaFu
# @File    : signUp_page.py
# @Desc    :
# coding=utf-8

import time

class signUp_page():

    def __init__(self,driver):
        self.driver = driver

    def sign_Up(self,account,password):
        # 注册功能
        driver = self.driver
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/btn_guide_sign_up').click()  # 点击注册按钮
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/input_user_name').send_keys('%s'%account)  # 输入注册邮箱
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/input_user_password').send_keys('%s'%password)  # 输入密码
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/btn_sub_register').click()  # 点击注册按钮
        time.sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/complete_sign_up_to_login').click()# 点击Continue
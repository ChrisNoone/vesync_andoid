#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 10:21
# @Author  : AnnaFu
# @File    : clickOn.py
# @Desc    :

# 根据屏幕坐标位置点击

from time import sleep, time

# 设定系数
# a = 500.0/720# (500.0,250.0)是要点击的坐标点，小米手机
# b = 250.0/1280# 720*1280 是写用例时使用的手机屏幕大小，小米手机
# a = x/1080# (x,y)是要点击的坐标点,（1080，,180）是X7手机屏幕大小
# b = y/1920# 720*1280 是写用例是使用的手机屏幕大小，X7手机

class clickOn_X_Y():

    def __init__(self,driver):
        self.driver = driver

    # loc是要点击的坐标点,带一位小数，size是写用例时使用手机的屏幕大小
    # 坐标要用浮点数(200.0,850.0)

    def clickOn_x_y(self,loc,size):
        driver = self.driver
        a = loc[0]/size[0]# (x,y)是要点击的坐标点,
        b = loc[1]/size[1]# 720*1280 是写用例是使用的手机屏幕大小
        # 获取当前手机屏幕大小X,Y
        X = driver.get_window_size()['width']
        Y = driver.get_window_size()['height']
        driver.tap([(a*X,b*Y)],50)
        sleep(4)
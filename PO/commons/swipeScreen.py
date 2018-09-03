#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 18:22
# @Author  : AnnaFu
# @File    : swipeScreen.py
# @Desc    :

from time import sleep

class swipeScreen():

    def __init__(self,driver):
        self.driver = driver

    # 屏幕定点滑动，startLoc是起始坐标，endLoc是终点坐标，size是写用例时使用手机的屏幕大小
    # 坐标要用浮点数(200.0,850.0)
    def swipeScreen_Point(self,startLoc,endLoc,size):
        driver = self.driver
        a1 = startLoc[0]/size[0]  # (x1,y1)是要点击的起始坐标点,(x2,y2)是要点击的终点坐标点
        b1 = startLoc[1]/size[1]  # size(720*1280)是写用例是使用的手机屏幕大小
        a2 = endLoc[0]/size[0]
        b2 = endLoc[1]/size[1]
        # 获取当前手机屏幕大小X,Y
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(4)
        x1 = int (x * a1)  #  起始x坐标
        y1 = int (y * b1)  #  起始y坐标
        x2 = int (x * a2)  #  终点x坐标
        y2 = int (y * b2)  #  终点y坐标
        driver.swipe(x1, y1, x2, y2, 1000)
        sleep (2)

    # 屏幕向上滑动
    def swipeScreen_Up(self):
        driver = self.driver
        # 获取当前手机屏幕大小X,Y
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(4)
        x1 = int (x * 0.5)  # x坐标
        y1 = int (y * 0.75)  #  起始y坐标
        y2 = int (y * 0.25)  #  终点y坐标
        driver.swipe(x1, y1, x1, y2, 1000)
        sleep (2)

    # 屏幕向下滑动
    def swipeScreen_Down(self):
        driver = self.driver
        # 获取当前手机屏幕大小X,Y
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(4)
        x1 = int (x * 0.5)  # x坐标
        y1 = int (y * 0.25)  #  起始y坐标
        y2 = int (y * 0.75)  #  终点y坐标
        driver.swipe(x1, y1, x1, y2, 1000)
        print 'zzzzzzzzzz'
        sleep (2)

    # 屏幕向左滑动
    def swipeScreen_Left(self):
        driver = self.driver
        # 获取当前手机屏幕大小X,Y
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(4)
        x1 = int (x * 0.75)  # 起始x坐标
        x2 = int (x * 0.25)  #  终点x坐标
        y1 = int (y * 0.5)  #  y坐标
        driver.swipe(x1, y1, x2, y1, 1000)
        sleep (2)

    # 屏幕向右滑动
    def swipeScreen_Right(self):
        driver = self.driver
        # 获取当前手机屏幕大小X,Y
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(4)
        x1 = int (x * 0.25)  # 起始x坐标
        x2 = int (x * 0.75)  #  终点x坐标
        y1 = int (y * 0.5)  #  y坐标
        driver.swipe(x1, y1, x2, y1, 1000)
        sleep (2)
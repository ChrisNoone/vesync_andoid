#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 15:42
# @Author  : NooneLiu
# @File    : clock_window.py
# @Desc    : 安卓设置时间的窗口

from time import sleep

class clock_window():
    def __init__(self,driver):
        self.driver = driver

    def get_cancel(self):
        el = self.driver.find_element_by_id("android:id/button2")
        return el

    def get_confirm(self):
        el = self.driver.find_element_by_id("android:id/button1")
        return el

    def get_ampm(self,noon="am"):
        """
        传入上午/下午，定位
        :param noon: 上午(am)或者下午(pm)
        """
        if noon=="am":
            el = self.driver.find_element_by_id("android:id/am_label")
        elif noon=="pm":
            el = self.driver.find_element_by_id("android:id/pm_label")
        return el

    def get_hours(self):
        el = self.driver.find_element_by_id("android:id/hours")
        return el

    def get_minutes(self):
        el = self.driver.find_element_by_id("android:id/minutes")
        return el

    def set_hours(self,desc):
        if 1 <= desc <= 12:
            self.get_hours().click()
            self.driver.find_element_by_name(str(desc)).click()
        else:
            print "小时请输入1到12之间整数。"

    def set_minutes(self,desc):
        if 0 <= desc <= 55:
            n = desc % 5
            if n == 0:
                self.get_minutes().click()
                self.driver.find_element_by_name(str(desc)).click()
            else:
                print "分钟请输入5的整数倍。"
        else:
            print "分钟请输入0到55之间整数。"

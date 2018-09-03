#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 10:09
# @Author  : NooneLiu
# @File    : away_page.py
# @Desc    :

class away_page():
    '''离家模式'''
    def __init__(self,driver):
        self.driver = driver

    def get_Cancel(self):
        el = self.driver.find_element_by_name("Cancel")
        return el

    def get_Save(self):
        el = self.driver.find_element_by_name("Save")
        return el

    def get_title(self):
        el = self.driver.find_element_by_name("Away Mode")
        return el

    def get_Onoff(self):
        xpath = "//*[@class='android.widget.ScrollView']/android.view.ViewGroup/\
                android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup"
        el = self.driver.find_element_by_xpath(xpath)
        return el

    def get_Start(self):
        el = self.driver.find_element_by_name("Start")
        return el

    def get_End(self):
        el = self.driver.find_element_by_name("End")
        return el

    def get_Repeat(self):
        el = self.driver.find_element_by_name("Repeat")
        return el

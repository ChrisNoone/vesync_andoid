#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 10:31
# @Author  : NooneLiu
# @File    : test.py
# @Desc    :

from lib import baseFunc
from appium import webdriver
from time import sleep
from PO.deviceDetail_page import deviceDetail_page
from PO.away_page import away_page
from PO.clock_window import clock_window

'''配置参数'''
platformVersion = '6.0.1'
deviceName = '8fa526ef'
appPackage = 'com.etekcity.vesyncplatform'
appActivity = '.presentation.ui.activities.LaunchActivity'

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = platformVersion
desired_caps['deviceName'] = deviceName
desired_caps['appPackage'] = appPackage
desired_caps['appActivity'] = appActivity
# desired_caps['appWaitActivity'] = '.presentation.ui.activities.MainActivity'

'''打开APP'''
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
sleep(5)
# '''打开通知页'''
# driver.find_elements_by_id("com.etekcity.vesyncplatform:id/ll_tap")[1].click()
# sleep(1)
# '''打开More页'''
# driver.find_elements_by_id("com.etekcity.vesyncplatform:id/ll_tap")[2].click()
# sleep(2)
# '''打开我的设备页'''
# driver.find_elements_by_id("com.etekcity.vesyncplatform:id/ll_tap")[0].click()
# sleep(1)
# '''下滑页面刷新'''
# swipeScreen.swipeScreen(driver).swipeScreen_Down()
# sleep(2)
# '''点击设备开/关'''
# xpath = "//android.widget.TextView[@text='" + "5ac5b" + \
#         "']/../following-sibling::android.widget.FrameLayout/android.widget.ImageButton"
# if(driver.find_element_by_xpath(xpath).is_displayed()):
#     print "元素存在..."
#     driver.find_element_by_xpath(xpath).click()
# sleep(2)
'''点击进入设备详情'''
xpath1 = "//android.widget.TextView[@text='" + "5ac5b" + "']/.."
driver.find_element_by_xpath(xpath1).click()
sleep(5)
d = deviceDetail_page(driver)
d.get_Away().click()
sleep(2)
d.get_SetAwayMode().click()
sleep(2)
d = away_page(driver)
d.get_Start().click()
sleep(2)
d = clock_window(driver)
d.set_hours(10)
sleep(1)
d.set_minutes(25)
sleep(2)
d.get_confirm().click()
sleep(2)

driver.quit()

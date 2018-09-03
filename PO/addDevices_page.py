#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 14:38
# @Author  : AnnaFu
# @File    : addDevices_page.py
# @Desc    :

from time import time,sleep

class addDevices_page():

    def __init__(self,driver):
        self.driver = driver

    def add_Devices(self):
        driver = self.driver
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/ek_cp_toolbar_right').click()  # 点击添加按钮
        sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/device_type_name').click()  #  添加的设备类型
        # x_y.test_X_Y(self.driver).test_x_y(500.0,350.0,1080,1920)  # 根据x，y位置，定位要添加的设备类型,1080,1920为手机屏幕的宽和长
        sleep(2)
        driver.find_element_by_name('Mini Smart Outlet').click()  # 点击选择要连接的设备，（设备的名称，可修改设备的名称连接其他设备）
        sleep(2)
        Mode = driver.find_element_by_id('com.etekcity.vesyncplatform:id/add_device_tv_config_type').text
        sleep(3)
        if Mode == 'APN mode >':
            driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_add_device_guide_start').click()  # smart分组，点击Start Setup
            self.smart_group()
            return 'smartconfig group'  # 返回用户当前在smartconfig分组
        else:
            driver.find_element_by_id('com.etekcity.vesyncplatform:id/add_device_tv_config_type').click()  # APN分组，点击smartconfig直接进入smart模式配网
            self.smart_group()
            return 'APN group'  # 返回用户当前在APN模式分组

    def smart_group(self):
        driver = self.driver
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_smart_guide_next').click()  # 点击Next  com.etekcity.vesyncplatform:id/wo_apn_guide_next
        sleep(2)
        WiFi_Name = driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_smart_wifi_name').text
        if WiFi_Name == 'NETGEAR':
            driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_smart_input_wifi_pwd').send_keys('admin123456')  # 输入Wi_Fi密码
        elif WiFi_Name == 'etekcity01':
            driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_smart_input_wifi_pwd').send_keys('05031122')  # 输入Wi_Fi密码
        sleep(2)
        driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_smart_start_config_wifi').click()  # 点击'Join Network'按钮
        sleep(30) # 配网70s失败

        # 需要手动操作使设备进入smartconfig配网模式，然后才能正确配网
        # sleep(70)
        # driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_device_friendly_name').send_keys('beautiful')  # 设备重命名
        # sleep(2)
        # driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_add_device_success').click()  # 点击确定
        # sleep(2)
        # driver.find_element_by_id('com.etekcity.vesyncplatform:id/wo_config_device_success_confirm_done').click()  # 点击确定进入设备列表页面
        # sleep(5)



# coding:utf-8

from appium import webdriver

class initDriver():
    '''initDriver类，初始化APP'''

    def initDriver(self):
        '''initDriver方法，初始化APP'''

        '''配置参数'''
        platformVersion = '6.0'
        '''SONY'''
        # deviceName = 'RQ30051L5F'
        '''XIAOMI'''
        deviceName = '531b4a341f404'
        appPackage = 'com.etekcity.vesyncplatform'
        appActivity = '.presentation.ui.activities.LaunchActivity'

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        # desired_caps['app'] = PATH(r'D:\smartoutlet.apk')
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity

        '''打开APP'''
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

        return self.driver
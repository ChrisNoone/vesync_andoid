#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 18:12
# @Author  : AnnaFu
# @File    : test_lonIn_logOut.py
# @Desc    :

from PO import *
from lib import baseFunc
import time
import unittest
import HTMLTestRunner
import os
import main

class base_case(unittest.TestCase):
    def setUp(self):
        self.driver = initDriver.initDriver().initDriver()
        time.sleep(8)

    def test_case1(self):
        # 注册功能
        account = '111@qq.com'
        password = '123456'
        signUp_page.signUp_page(self.driver).sign_Up(account,password)
        print u'%s账号注册成功'%account,'账号的登录密码为%s'%password

    def test_case2(self):
        # 退出登录
        account = logOut_page.logOut_page(self.driver).log_Out()
        print u'%s账号退出登录成功'%account

    def test_case3(self):
        # 登录功能
        account = '916943599@qq.com'
        password = '123456'
        logIn_page.logIn_page(self.driver).log_In(account,password)
        print u'%s账号登录成功'%account

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #     unittest.main()
    #   不需要手动开启appium服务，用例执行前先打开appium服务，用例执行完后关闭appium服务
    os.system('start startAppiumServer.bat')  # 开启appium服务
    time.sleep(6)
    testunit = unittest.TestSuite()
    testunit.addTest(base_case("test_case1"))
    testunit.addTest(base_case("test_case2"))
    testunit.addTest(base_case("test_case3"))
    fp = baseFunc.genLogFile('w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(testunit)
    fp.close()
    os.system('start stopAppiumServer.bat')  # 关闭appium服务
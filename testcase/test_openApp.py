# coding:utf-8

from PO import *
from lib import *
import time
import unittest
import HTMLTestRunner


class base_case(unittest.TestCase):
    def setUp(self):
        self.driver = initDriver().initDriver()
        time.sleep(5)

    def test_case1(self):
        print 'test_case1'

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    #     unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(base_case("test_case1"))

    fp = baseFunc.genLogFile('w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(testunit)
    fp.close()
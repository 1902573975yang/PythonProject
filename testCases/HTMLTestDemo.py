#coding=utf-8

import HTMLTestRunner
import HTMLTestReport

import os
import sys
import time
import unittest
from selenium import webdriver


class Baidu(unittest.TestCase):
    '''
    Test Report
    '''
    #每个case都会执行该方法
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.baidu.com")
        pass
    # 关闭
    def tearDown(self):
        self.driver.quit()

    def test_case(self):
        print("test_case1")
        pass
    def test_case2(self):
        print("test_case2")
        pass
    def closeBrowser(self):
        print("close")
        pass
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
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.baidu.com")
        pass
    def test_case(self):
        print("test_case1")
        pass
    def test_case2(self):
        print("test_case2")
        pass
    def closeBrowser(self):
        print("close")
        pass

if __name__ == "__main__":
    '''Testing'''
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_case"))
    testunit.addTest(Baidu("test_case2"))
    testunit.addTest(Baidu("closeBrowser"))
    report_path ="D:\\temp\\result.html"
    fp = open(report_path,"wb")
    report = HTMLTestReport.HTMLTestRunner(stream=fp,title="repo",description="this is desc",tester="yang")
    report.run(testunit)
    fp.close()
import unittest
import os
import HTMLTestReport
from testCases.HTMLTestDemo import Baidu

if __name__ == "__main__":
    '''Testing'''
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_case"))
    testunit.addTest(Baidu("test_case2"))
    testunit.addTest(Baidu("closeBrowser"))
    report_path =os.path.abspath(os.path.dirname(__file__)) +"/reports/HTMLTest.html"
    fp = open(report_path,"wb")
    report = HTMLTestReport.HTMLTestRunner(stream=fp,title="repo",description="this is desc",tester="yang")
    report.run(testunit)
    fp.close()
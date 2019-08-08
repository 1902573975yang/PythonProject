#code=utf-8

from BeautifulReport import BeautifulReport
import os
import unittest


if __name__ == '__main__':
    tests = unittest.defaultTestLoader.discover("./testCases",pattern="Beautiful*.py",top_level_dir=None)
    BeautifulReport(tests).report(filename="BeautifulReport",description="Simple Desc", log_path='.//reports/')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/12 15:32
# @Author : whj
import unittest
import os,sys
import time
from Common import sendEmail
from BeautifulReport import BeautifulReport
from test_case.test11_01 import *
path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(path)

# 测试用例目录
test_dir = os.path.join(os.path.dirname(__file__),"test_case")
# 测试报告目录
reportPath = os.path.join(os.path.dirname(__file__),"report")
# print(test_dir)
# print(reportPath)
# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
pattern = 'test_*.py'
now = time.strftime("%Y-%m-%d %H_%M_%S")
reportName = now + '测试报告.html'
description = 'H5自动化测试报告'
if __name__ == '__main__':
    test_suite = unittest .defaultTestLoader.discover(test_dir, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=reportName, description=description, log_path=reportPath)
    # # 发送邮件
    # sendEmail.email(reportPath)
# -*- coding:utf-8 -*- 
"""
@Time    : 2019-09-05 22:12
@Author  : Allen
@FileName: readConfig.py
@IDE     : PyCharm
"""
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
print(BASE_DIR)

# 配置文件
CONFIG_DIR = os.path.join(BASE_DIR, "config", "config.ini")
# 元素配置文件
Element_Config = os.path.join(BASE_DIR, "config", "config.py")
# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR, "test_case")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "log")
# 截图目录
Img_DIR = os.path.join(BASE_DIR, "img")

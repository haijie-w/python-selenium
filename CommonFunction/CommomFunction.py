# -*- coding:utf-8 -*- 
"""
@Time    : 2020-03-12 22:50
@Author  : Allen
@FileName: CommomFunction.py
@IDE     : PyCharm
"""

import sys
from common.commonFuction import UIHandle
from common.commonFuction import WebHandle
from config.config import browser_config
from config.config import local_constant
from config.config import local_config
import time
from time import sleep
from datetime import *
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from xlrd import xldate_as_tuple
from selenium.webdriver.common.keys import Keys

global driver
driver = browser_config['chrome']


# 打开进入微端首页
# class commomFunction():
#     def __init__(self):
#         # 初始化driver参数
#         # 通过device name设置模拟的手机设备
#         # mobile_emulation = {"deviceName": "Galaxy S5"}
#         # option = webdriver.ChromeOptions()
#         # option.add_experimental_option('mobileEmulation', mobile_emulation)
#         # driver = webdriver.Chrome(chrome_options=option)
#         self.uihandle = UIHandle(driver)
#         self.webdriver = WebHandle(driver)
#         self.uihandle.get(local_constant['H5_Test_URL'])
#         self.uihandle.maxiWindow()
#         sleep(2)
#         return driver

def logIn():
    uihandle = UIHandle(driver)
    webhandle = WebHandle(driver)
    uihandle.get(local_constant['H5_Test_URL'])
    # uihandle.maxiWindow()
    sleep(2)
    return driver


def logInModule(driver, page, module):
    # 传入driver对象
    uihandle = UIHandle(driver)
    webhandle = WebHandle(driver)
    webhandle.Click(page, module)
    sleep(2)
    return driver

# -*- coding:utf-8 -*- 
"""
@Time    : 2020-03-12 22:50
@Author  : Allen
@FileName: CommomFunctio1n.py
@IDE     : PyCharm
"""

from common.commonFuction import UIHandle
from common.commonFuction import WebHandle
from config.config import browser_config
from config.config import local_constant
from time import sleep

# 此文件中封装打开浏览器和切换模块操作
global driver
driver = browser_config['chrome']
# 暂时在此处切换测试环境地址
# url = local_constant['H5_uat_URL']
url = local_constant['H5_Test_URL']


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
    uihandle.get(url)
    # uihandle.maxiWindow()
    sleep(1)
    return driver


def changeModule(driver, page, module):
    # 传入driver对象
    uihandle = UIHandle(driver)
    webhandle = WebHandle(driver)
    webhandle.Click(page, module)
    sleep(2)
    return driver

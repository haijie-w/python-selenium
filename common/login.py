# -*- coding: utf-8 -*-
# @Time    : 2017-07-25
# @Vestion :1.0
# @Author  :Zoe Zhou

# 业务功能脚本（用例脚本可调用此处的功能脚本）

import sys
from common.commonFuction import UIHandle
from common.commonFuction import WebHandle
# from common.commonFuction import Assert
from config.config import browser_config, local_config, local_constant
import time

global driver
driver = browser_config['chrome']


# print(driver)
# uihandle = WebHandle(driver1)
# uihandle.get(local_constant['LOGIN_MATRIX_URL'])


# 打开Matrix首页登录
class Login():
    def __init__(self):
        self.driver1 = UIHandle(driver)
        self.driver2 = WebHandle(driver)

    def login(self):
        # 打开浏览器
        # 传入driver对象
        # ast = Assert(driver)
        # 输入url地址
        self.driver1.get(local_constant['LOGIN_MATRIX_URL'])
        self.driver2.Click('平安三春晖登录', '百度首页')
        time.sleep(2)
        # self.driver1.back()
        self.driver1.maxiWindow()
        self.driver1.refresh()
        time.sleep(2)
        # self.driver1.quit()
        return self.driver1


a = Login()
a.login()

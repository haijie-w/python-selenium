# -*- coding:utf-8 -*- 
"""
@Time    : 2020-03-12 22:40
@Author  : Allen
@FileName: CommonRe1cycle.py
@IDE     : PyCharm
"""
# 噢啦回收业务功能脚本（用例脚本可调用此处的功能脚本）

import importlib, sys
importlib.reload(sys)
from common.commonFuction import *
from CommonFunction.CommomFunction import *
from config.config import local_constant
from config.config import local_config
from config.config import basic_config
from CommonFunction.login import Login
from common.globalvar import GlobalMap
# from CommonFunction.CommonPersonal import *
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from time import sleep
import time
import random

global bean22
bean22 = GlobalMap()
# 点击进入回收模块
def recycleModule(driver):
    try:
        webhandle = WebHandle(driver)
        a = Login(driver)
        a.login(driver)
        # clickOola(driver)
        # UIHandle.back()
        changeModule(driver, '个人页面', '环保回收页')
        sleep(1)
        webhandle.Click('环保回收', '选择发起回收地址')
        webhandle.Click('个人页面', '广州')
        sleep(1)
        webhandle.Click('环保回收', '衣帽鞋包')
        # sleep(1)
        print(r"进入环保回收页")
    except Exception as e:
        print(r"进入环保回收页失败", e)
        # sleep(1)

if __name__ == "__main__":
    recycleModule(driver)

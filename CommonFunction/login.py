#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/17 16:51
# @Author : whj

# 此处为封装好的用户登录脚本

import sys
from common.commonFuction import *
from CommonFunction.CommomFunction import *
from common.globalvar import GlobalMap
from config.config import browser_config
from config.config import local_constant
from config.config import local_config
from config.config import basic_config
from config.config import all_phone_nums
from selenium.webdriver.common.by import By
from time import sleep
import random
# from CommonFunction.CommonPersonal import *
from datetime import *

global driver
global userID
# global bean

# 登录模块
class Login():

    def __init__(cls,driver):
        logIn()
        cls.driver = driver
        changeModule(driver, '个人页面', '个人模块')
        # sleep(1)
        print(r"进入个人模块")

    def login(cls,driver):
        try:
            cls.driver = driver
            webhandle = WebHandle(driver)
            webhandle.Click('个人页面', '登录按钮')
            # print(r"成功进入注册页面")
            # phone = random.choice(basic_config.get('phone'))
            # 随机取到一个180,189和158开头的手机号码
            phone = random.choice(all_phone_nums)
            webhandle.Input('个人页面', '输入手机号', phone)
            # print(r"输入手机号成功")
            webhandle.Click('个人页面', '发送验证码')
            # print(r"成功发送验证码")
            sleep(2)
            webhandle.Click('个人页面', '数字1')
            webhandle.Click('个人页面', '数字2')
            webhandle.Click('个人页面', '数字3')
            webhandle.Click('个人页面', '数字4')
            webhandle.Click('个人页面', '数字5')
            webhandle.Click('个人页面', '数字6')
            # print(r"成功输入验证码")
            sleep(1)
            webhandle.Click('个人页面', '引导图图层')
            # print(r"关闭个人页面引导图图层")
            bean0 = webhandle.getElementText('个人页面', '用户噢啦豆')
            print(r'登录成功，用户的噢啦豆为' + ":" + bean0)
            bean1 = int(bean0)
            GlobalMap.set_map('bean', bean1)
            sleep(1)
        except Exception as e:
            print(r"登录失败", e)

if __name__ == "__main__":
    a = Login(driver)
    a.login(driver)
    # userSetting(driver)
    # clickAddress(driver)
    # addAddress(driver, '晓杰')

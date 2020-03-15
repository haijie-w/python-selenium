# -*- coding:utf-8 -*- 
"""
@Time    : 2020-03-12 22:39
@Author  : Allen
@FileName: CommonPersonal.py
@IDE     : PyCharm
"""

# 业务功能脚本（用例脚本可调用此处的功能脚本）

import sys
from common.commonFuction import *
from CommonFunction.CommomFunction import *
from config.config import browser_config
from config.config import local_constant
from config.config import local_config
from config.config import basic_config
from selenium.webdriver.common.by import By
from time import sleep
import random
from datetime import *

global driver
global userID


# 点击进入个人模块
def loginModule1(driver):
    try:
        # webhandle = WebHandle(driver)
        # # personal = local_config['个人模块']
        # webhandle.Click('个人页面','个人模块')
        logIn()
        logInModule(driver, '个人页面', '个人模块')
        sleep(1)
        print(r"进入个人模块")
    except Exception as e:
        print(r"进入个人模块失败", e)
        # sleep(1)


# 点击进入到登录/注册页面
def loginPage(driver):
    try:
        webhandle = WebHandle(driver)
        # login_page = element_config['login_page']
        # self.driver1.login_page(login_page)
        webhandle.Click('个人页面', '登录按钮')
        sleep(1)
        print(r"成功进入注册页面")
        # phoneText = driver.find_element(By.XPATH, "//*[@id='telephone']").text
        # print(phoneText)
    except Exception as e:
        print(r"进入登录/注册页面失败", e)


# 在登录页面输入手机号码
def phoneInput(driver):
    try:
        webhandle = WebHandle(driver)
        # 从配置中随机获取一个手机号
        # inputNumber = basic_config['inputNumber']
        phone = random.choice(basic_config.get('phone'))
        # webhandle.Click('个人页面','输入手机号')
        webhandle.Input('个人页面', '输入手机号', phone)
        print(r"输入手机号成功")
    except Exception as e:
        print(r"输入手机号失败", e)


# 点击发送验证码
def sendMessageCode(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '发送验证码')
        print(r"成功发送验证码")
    except Exception as e:
        print(r"发送验证码失败", e)
    sleep(3)


# 输入6位数验证码
def inputMessageCode(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '数字1')
        webhandle.Click('个人页面', '数字2')
        webhandle.Click('个人页面', '数字3')
        webhandle.Click('个人页面', '数字4')
        webhandle.Click('个人页面', '数字5')
        webhandle.Click('个人页面', '数字6')
        print(r"成功输入验证码")
    except Exception as e:
        print(r"验证码输入失败", e)
    sleep(1)


# 关闭引导图图层（点击噢啦豆图标）
def clickOola(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '引导图图层')
        print(r"关闭个人页面引导图图层")
        bean = webhandle.getElementText('个人页面', '用户噢啦豆')
        print(r'用户的噢啦豆为' + ":" + bean)
    except Exception as e:
        print(r"关闭个人页面引导图层失败", e)
    sleep(1)


# 点击用户头像进入个人设置页面
def userSetting(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '用户头像')
        print(r"进入用户设置页面")
        sleep(0.5)
        userID = webhandle.getElementText('个人页面', '用户ID')
        print(r'用户的噢啦豆为' + ":" + userID)
        sleep(0.5)
        UIHandle.back()
    except Exception as e:
        print(r"进入用户设置页面失败", e)
    sleep(1)


if __name__ == "__main__":
    loginModule1(driver)
    loginPage(driver)
    phoneInput(driver)
    sendMessageCode(driver)
    inputMessageCode(driver)
    clickOola(driver)
    userSetting(driver)

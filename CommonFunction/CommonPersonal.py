# -*- coding:utf-8 -*-
"""
@Time    : 2020-03-12 22:39
@Author  : Allen
@FileName: CommonPersonal.py
@IDE     : PyCharm
"""

# 个人中心业务功能脚本（用例脚本可调用此处的功能脚本）

import importlib, sys
importlib.reload(sys)
from common.commonFuction import *
from CommonFunction.CommomFunction import *
from CommonFunction.login import *
from config.config import browser_config
from config.config import local_constant
from config.config import local_config
from config.config import basic_config
from common.dataBase import *
from selenium.webdriver.common.by import By
from time import sleep
import random


global driver
global userID

#
# # 点击进入个人模块
# def loginModule(driver):
#     try:
#         # webhandle = WebHandle(driver)
#         # # personal = local_config['个人模块']
#         # webhandle.Click('个人页面','个人模块')
#         logIn()
#         changeModule(driver, '个人页面', '个人模块')
#         # sleep(1)
#         print(r"进入个人模块")
#     except Exception as e:
#         print(r"进入个人模块失败", e)
#         # sleep(1)
#
#
# # 点击进入到登录/注册页面
# def loginPage(driver):
#     try:
#         webhandle = WebHandle(driver)
#         # login_page = element_config['login_page']
#         # self.driver1.login_page(login_page)
#         webhandle.Click('个人页面', '登录按钮')
#         # sleep(1)
#         print(r"成功进入注册页面")
#         # phoneText = driver.find_element(By.XPATH, "//*[@id='telephone']").text
#         # print(phoneText)
#     except Exception as e:
#         print(r"进入登录/注册页面失败", e)
#
#
# # 在登录页面输入手机号码
# def phoneInput(driver):
#     try:
#         webhandle = WebHandle(driver)
#         # 从配置中随机获取一个手机号
#         # inputNumber = basic_config['inputNumber']
#         phone = random.choice(basic_config.get('phone'))
#         # webhandle.Click('个人页面','输入手机号')
#         webhandle.Input('个人页面', '输入手机号', phone)
#         print(r"输入手机号成功")
#     except Exception as e:
#         print(r"输入手机号失败", e)
#
#
# # 点击发送验证码
# def sendMessageCode(driver):
#     try:
#         webhandle = WebHandle(driver)
#         webhandle.Click('个人页面', '发送验证码')
#         print(r"成功发送验证码")
#     except Exception as e:
#         print(r"发送验证码失败", e)
#     sleep(2)
#
#
# # 输入6位数验证码
# def inputMessageCode(driver):
#     try:
#         webhandle = WebHandle(driver)
#         webhandle.Click('个人页面', '数字1')
#         webhandle.Click('个人页面', '数字2')
#         webhandle.Click('个人页面', '数字3')
#         webhandle.Click('个人页面', '数字4')
#         webhandle.Click('个人页面', '数字5')
#         webhandle.Click('个人页面', '数字6')
#         print(r"成功输入验证码")
#         sleep(1)
#     except Exception as e:
#         print(r"验证码输入失败", e)

# 关闭引导图图层（点击噢啦豆图标）
def clickOola(driver):
    try:
        webhandle = WebHandle(driver)
        # webhandle.Click('个人页面', '引导图图层')
        # print(r"关闭个人页面引导图图层")
        bean = webhandle.getElementText('个人页面', '用户噢啦豆')
        # print(r'用户的噢啦豆为' + ":" + bean)
        # print(type(bean))
        sleep(1)
        if int(bean) < 20:
            webhandle.Click('个人页面', '用户头像')
            print(r"进入用户设置页面")
            sleep(1)
            userID = webhandle.getElementText('个人页面', '用户ID')
            # print(type(userID))
            print('用户的ID为' + ":" + userID)
            sleep(1)
            x = DB()
            userID1 = int(userID)
            y = "update star_user SET credit=credit+10 WHERE id = " + userID
            y1 = "select credit from star_user WHERE id = " + userID
            x.delete(y)
            credit1 = x.select_oneInt(y1)
            print(credit1)
            print("用户增加后的噢啦豆数量为" + ":" + str(credit1))
        else:
            print(r"用户当前的噢啦豆够用了")
    except Exception as e:
        print(r"关闭个人页面引导图层失败", e)


# 点击用户头像进入个人设置页面
def userSetting(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '用户头像')
        print(r"进入用户设置页面")
        sleep(1)
        userID = webhandle.getElementText('个人页面', '用户ID')
        print(r'用户的ID为' + ":" + userID)
        sleep(1)
        # UIHandle.back()
    except Exception as e:
        print(r"进入用户设置页面失败", e)

# 点击进入我的地址页面
def clickAddress(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '我的地址')
        print(r"进入我的地址页面")
        sleep(0.5)
    except Exception as e:
        print(r"进入我的地址页面失败", e)
    sleep(1)

# 新增我的地址并设置为默认地址（广州市）
def addAddress(driver,name):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '添加地址')
        print(r"进入添加地址页面")
        sleep(0.5)
        webhandle.Input('个人页面', '联系人',name)
        print(r"联系人信息已输入")
        webhandle.Click('个人页面', '地址')
        sleep(1)
        webhandle.Click('个人页面', '地址选择框')
        # sleep(1)
        webhandle.Click('个人页面', '广州')
        # sleep(1)
        webhandle.Click('个人页面', '搜索城市')
        sleep(1)
        webhandle.Input('个人页面', '搜索城市', '中信广场')
        sleep(1)
        webhandle.Click('个人页面', '第一个结果')
        sleep(0.5)
        webhandle.Input('个人页面', '详细地址','1001房')
        webhandle.Click('个人页面', '设置默认地址')
        sleep(0.5)
        webhandle.Click('个人页面', '完成添加地址')
        sleep(1)
        UIHandle.back()
        print(r'返回到个人页面')
        UIHandle.back()
        print(r'返回到个人中心页面')
    except Exception as e:
        print(r"添加地址失败", e)
    sleep(1)

# 进入回收订单页面
def recycleList(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '回收订单')
        print(r"进入回收订单页面")
        sleep(2)
        UIHandle.back()
        sleep(1)
    except Exception as e:
        print(r"进入回收订单页面失败", e)

# 进入爱心记录页面
def loveRecord(driver):
    try:
        webhandle = WebHandle(driver)
        UIHandle.refresh()
        webhandle.Click('个人页面', '爱心记录')
        print(r"进入爱心记录页面")
        sleep(1)
        UIHandle.back()
        sleep(1)
    except Exception as e:
        print(r"进入爱心记录失败", e)

# 进入任务中心页面
def task(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '任务中心')
        print(r"进入任务中心页面")
        sleep(0.5)
        UIHandle.back()
        sleep(2)
    except Exception as e:
        print(r"进入任务中心失败", e)

# 进入噢啦日签页面
def dailySignature(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '噢啦日签')
        print(r"进入噢啦日签页面")
        sleep(1)
        UIHandle.back()
        sleep(2)
    except Exception as e:
        print(r"进入噢啦日签失败", e)

# 进入消息中心页面
def message(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '消息中心')
        print(r"进入消息中心页面")
        sleep(1)
        UIHandle.back()
        sleep(2)
    except Exception as e:
        print(r"进入消息中心失败", e)

# 进入联系客服页面
def customerService(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '联系客服')
        print(r"进入联系客服页面")
        sleep(1)
        UIHandle.back()
        sleep(2)
    except Exception as e:
        print(r"进入联系客服失败", e)

# 进入关于噢啦页面
def aboutOola(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('个人页面', '关于噢啦')
        print(r"进入关于噢啦页面")
        sleep(1)
        UIHandle.back()
        sleep(2)
    except Exception as e:
        print(r"进入关于噢啦失败", e)


if __name__ == "__main__":
    # loginModule(driver)
    # loginPage(driver)
    # phoneInput(driver)
    # sendMessageCode(driver)
    # inputMessageCode(driver)
    a = Login(driver)
    a.login(driver)
    clickOola(driver)
    # userSetting(driver)
    # clickAddress(driver)
    # addAddress(driver)
    # addNewAddress(driver,'whj')
    # recycleList(driver)
    # loveRecord(driver)
    # task(driver)
    # dailySignature(driver)
    # message(driver)
    # # customerService(driver)
    # aboutOola(driver)

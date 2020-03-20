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
from CommonFunction.login import Login
from common.globalvar import GlobalMap
from CommonFunction.CommonPersonal import userSetting,clickAddress,addAddress
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
        userSetting(driver)
        clickAddress(driver)
        addAddress(driver,'test')
        # clickOola(driver)
        changeModule(driver, '个人页面', '环保回收页')
        # sleep(1)
        webhandle.Click('环保回收', '选择发起回收地址')
        sleep(2)
        # UIHandle.back()
        webhandle.Click('环保回收', '广州')
        # webhandle.Click('环保回收', '衣帽鞋包')
        # sleep(1)
        print(r"进入环保回收页")
    except Exception as e:
        print(r"进入环保回收页失败", e)

def recycleCategory(driver,categoryNum,weight=None):
    if weight != None:
        weight = weight
    else:
        weight = 5
    webhandle = WebHandle(driver)
    if categoryNum == 1:
        try:
            webhandle.Click('环保回收','第一个回收品类')
        except Exception as e:
            print(r"进入第一个回收品类失败失败", e)
    elif categoryNum == 2:
        try:
            webhandle.Click('环保回收','第二个回收品类')
        except Exception as e:
            print(r"进入第二个回收品类失败失败", e)
    elif categoryNum == 3:
        try:
            webhandle.Click('环保回收','第三个回收品类')
        except Exception as e:
            print(r"进入第三个回收品类失败失败", e)
    elif categoryNum ==4:
        try:
            webhandle.Click('环保回收','第四个回收品类')
        except Exception as e:
            print(r"进入第四个回收品类失败失败", e)
    else:
        print("你输入回收品类数字有误")
    webhandle.clearText('环保回收','下单时输入回收重量')
    webhandle.Input('环保回收','下单时输入回收重量',weight)
    sleep(1)
    prediction = webhandle.getElementText('环保回收','下单时的预计噢啦豆数量')
    prediction1 = webhandle.getText("//div[@class='bottom-area flex-row ']/div[1]/p")
    print(prediction1,prediction)
    webhandle.Click('环保回收', '确定回收品类数量')
    # webhandle.Click('环保回收','选择上门取件地址')
    webhandle.Click('环保回收', '选择上门取件时间')
    sleep(1)
    try:
        webhandle.Click('环保回收', '确定上门取件时间')
        print('选择上门时间成功')
    except Exception as e:
        print(e)
    webhandle.Click('环保回收', '确定预约')
    # try:
    #     webhandle.Click('环保回收','确定预约')
    #     print('选择上门时间成功')
    # except Exception as e:
    #      print(e)
    # recycleSuccess = webhandle.getElementText('环保回收','预约成功')
    # print(recycleSuccess)
    # webhandle.Click('环保回收','分享成就')
    # 海报截图

if __name__ == "__main__":
    recycleModule(driver)
    recycleCategory(driver,1,6)

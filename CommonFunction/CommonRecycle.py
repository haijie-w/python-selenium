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
from CommonFunction.CommonPersonal import userSetting,addAddress,clickOola,recycleList
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from time import sleep
import time
import random

global bean22
bean22 = GlobalMap()
# 点击进入回收模块，选择回收地区
def recycleModule(driver):
    try:
        webhandle = WebHandle(driver)
        # a = Login(driver)
        # a.login(driver)
        # # clickOola(driver)
        # userSetting(driver)
        # addAddress(driver,'test')
        # clickOola(driver)
        changeModule(driver, '个人页面', '环保回收页')
        # sleep(1)
        webhandle.Click('环保回收', '选择发起回收地址')
        sleep(1)
        # UIHandle.back()
        webhandle.Click('环保回收', '广州')
        print(r"成功选择回收地址")
    except Exception as e:
        print(r"选择回收地址失败", e)

# 选择回收品类（数字1,2,3,4代表回收品类的顺序），下单数量（默认为5并支持修改），下单回收成功后截图下单成功页
def recycleCategory(driver,categoryNum,weight=None):
    # 回收数量不输入时，默认数量为5
    if weight != None:
        weight = weight
    else:
        weight = 5
    webhandle = WebHandle(driver)
    # 判断输入的回收品类顺序
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
    try:
        webhandle.clearText('环保回收','下单时输入回收重量')
        sleep(0.5)
        webhandle.Input('环保回收','下单时输入回收重量',weight)
        # sleep(1)
    except Exception as e:
            print(r"输入下单回收重量失败", e)
    # 获取并打印下单时显示的预计噢啦豆数量
    prediction = webhandle.getElementText('环保回收','下单时的预计噢啦豆数量')
    prediction1 = webhandle.getText("//div[@class='bottom-area flex-row ']/div[1]/p")
    print(prediction1,prediction)
    # 进入确认下单页面
    try:
        webhandle.Click('环保回收', '确定回收品类数量')
    except Exception as e:
            print(r"进入确认下单页面失败", e)
    # 选择预约下单地址和时间
    try:
        # webhandle.Click('环保回收','选择上门取件地址')
        webhandle.Click('环保回收', '选择上门取件时间')
        sleep(1)
        webhandle.Click('环保回收', '确定上门取件时间')
        # print('选择上门时间成功')
    except Exception as e:
        print(e)
    # 滚动屏幕到页面底部，确认预约回收信息
    try:
        webhandle.script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        webhandle.Click('环保回收', '确定预约')
        print('预约成功')
        sleep(3)
    except Exception as e:
        print(e)

# 查看是否预约成功
def orderSuccess(driver):
    # webhandle = WebHandle(driver)
    try:
        a= Assert.assertTextExist('环保回收','预约成功','预约成功')
        if a ==True:
            print('预约回收成功')
        else:
            print('预约回收失败')
    except Exception as e:
        print('没找到元素',e)

# 预约成功页分享海报
def orderSuccessShare(driver):
    webhandle = WebHandle(driver)
    uihandle = UIHandle(driver)
    try:
        webhandle.Click('环保回收','分享成就')
        sleep(2)
        # 海报截图
        # uihandle.get_screent_img('预约回收成功页分享')
        UIHandle.back()
        sleep(1)
    except Exception as e:
        print('分享成就按钮失败',e)

# 预约成功页分享海报
def moreProject(driver):
    webhandle = WebHandle(driver)
    uihandle = UIHandle(driver)
    try:
        webhandle.Click('环保回收','更多项目')
        sleep(2)
        # 跳转到爱心项目
        title = uihandle.get_page_title()
        print('订单详情页跳转到爱心项目首页',title)
        sleep(1)
    except Exception as e:
        print('更多项目跳转失败',e)

# 判断页面是否显示有可以支持的爱心项目
def supportProjict(driver):
    webhandle = WebHandle(driver)
    if Assert.assertTextExist('环保回收','支持项目','支持项目') == True:
        try:
            supportProjictName = webhandle.getElementText('环保回收','支持项目名称')
            print('准备支持的项目是:' + '[' + supportProjictName + ']')
            webhandle.Click('环保回收','支持项目')
            sleep(1)
            webhandle.Click('环保回收','确认捐赠')
            # 打印捐赠成功后的信息
            support1 = webhandle.getText("//*[@class='right flex-col']/p")
            support2 = webhandle.getText("//*[@class='right flex-col']/div")
            print(support1,support2)
        except Exception as e:
            print('支持项目失败',e)
    else:
        print('该渠道下没有可支持的项目')

# 点击查看订单页面
def orderPage(driver):
    webhandle = WebHandle(driver)
    try:
        webhandle.Click('环保回收','查看订单')
        sleep(1)
        orderStatus = webhandle.getElementText('环保回收','订单状态')
        print('当前的订单状态为：',orderStatus)
        orderID = webhandle.getElementText('环保回收','订单编号')
        print('订单编号为：',orderID)
        # UIHandle.get_screent_img('回收成功后的订单详情页面')
        GlobalMap.set_map('orderNo', orderID)
    except Exception as e:
        print('查看订单失败',e)

# 订单页面取消订单
def cancleOrder(driver):
    webhandle = WebHandle(driver)
    try:
        webhandle.Click('环保回收','取消订单')
        sleep(1)
        webhandle.Click('环保回收','取消原因1')
        webhandle.script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        webhandle.Click('环保回收','确定取消')
    except Exception as e:
        print('查看订单失败',e)

# 点击页面中的悬浮按钮，回到首页
def backHome(driver):
    sleep(2)
    webhandle = WebHandle(driver)
    try:
        webhandle.Click('环保回收','回到首页')
    except Exception as e:
        print('回到回收首页失败',e)









if __name__ == "__main__":
    recycleModule(driver)
    recycleCategory(driver,1,6)
    # orderSuccess(driver)
    # orderSuccessShare(driver)
    supportProjict(driver)
    orderPage(driver)
    backHome(driver)
    changeModule(driver,'个人页面', '个人模块')
    recycleList(driver)

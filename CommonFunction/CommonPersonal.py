# -*- coding:utf-8 -*-
"""
@Time    : 2020-03-12 22:39
@Author  : Allen
@FileName: Common1Personal.py
@IDE     : PyCharm
"""

# 个人中心业务功能脚本（用例脚本可调用此处的功能脚本）

import importlib
import sys

importlib.reload(sys)
from CommonFunction.login import *
from common.dataBase import *
from common.globalvar import GlobalMap
from time import sleep


global driver
global userID


# 关闭个人页面-用户登录后的引导图图层（点击噢啦豆图标）
def clickOola(driver):
    try:
        webhandle = WebHandle(driver)
        # 获取用户登录后的噢啦豆数量
        bean = GlobalMap.get('bean')
        sleep(1)
        # 判断用户噢啦豆是否充足，不够设置的数量，则为用户充值
        if int(bean) < 20:
            webhandle.Click('个人页面', '用户头像')
            print(r"进入用户设置页面")
            sleep(1)
            userID = webhandle.getElementText('个人页面', '用户ID')
            print('用户的ID为' + ":" + userID)
            sleep(1)
            # 保存获取到的用户ID信息
            GlobalMap.set_map('userid',userID)
            # 建立数据库连接
            x = DB()
            # userID1 = int(userID)
            # 为用户充值10个噢啦豆
            y = "update star_user SET credit=credit+10 WHERE id = " + userID
            y1 = "select credit from star_user WHERE id = " + userID
            x.delete(y)
            credit1 = x.select_oneInt(y1)
            # 更新修改后的用户噢啦豆信息
            GlobalMap.set_map('bean', credit1)
            # print(GlobalMap.get('bean'))
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
def addAddress(driver,name):
    webhandle = WebHandle(driver)
    try:
        webhandle.Click('个人页面', '我的地址')
        # print(r"进入我的地址页面")
        sleep(2)
    except Exception as e:
        print(r"进入我的地址页面失败", e)
    # 判断地址页面是否不存在地址信息，若不存在则新建地址，若存在则打印当前地址信息
    bool1 = Assert.assertXPathExistByXPath('个人页面', '无地址信息')
    if bool1 == False:
        address1 = webhandle.getText("//*[@class='address-item']/div/div[1]/div/div[2]")
        print('已有地址信息',address1)
    else:
        webhandle.Click('个人页面', '添加地址')
        print(r"进入添加地址页面")
        sleep(0.5)
        webhandle.Input('个人页面', '联系人', name)
        print(r"联系人信息已输入")
        webhandle.Click('个人页面', '地址')
        sleep(1)
        webhandle.Click('个人页面', '地址选择框')
        webhandle.Click('个人页面', '广州')
        webhandle.Click('个人页面', '搜索城市')
        sleep(1)
        webhandle.Input('个人页面', '搜索城市', '中信广场')
        sleep(2)
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
    a = Login(driver)
    a.login(driver)
    clickOola(driver)
    # userSetting(driver)
    addAddress(driver,'whj')
    # recycleList(driver)
    # loveRecord(driver)
    # task(driver)
    # dailySignature(driver)
    # message(driver)
    # # customerService(driver)
    # aboutOola(driver)

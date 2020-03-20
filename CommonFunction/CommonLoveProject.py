# -*- coding:utf-8 -*- 
"""
@Time    : 2020-03-12 22:41
@Author  : Allen
@FileName: CommonLovePr1oject.py
@IDE     : PyCharm
"""

# 噢啦爱心业务功能脚本（用例脚本可调用此处的功能脚本）

import importlib, sys
importlib.reload(sys)
from common.commonFuction import *
from CommonFunction.CommomFunction import *
from CommonFunction.CommonPersonal import clickOola
from CommonFunction.login import Login
from common.globalvar import GlobalMap
# from CommonFunction.CommonPersonal import *
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By
from time import sleep
import time
import random

# 点击进入个人模块
def loveModule(driver):
    try:
        # webhandle = WebHandle(driver)
        a = Login(driver)
        a.login(driver)
        clickOola(driver)
        UIHandle.back()
        changeModule(driver, '个人页面', '噢啦爱心首页')
        # Ec.title_contains("噢啦爱心")
        # webhandle.Click('噢啦爱心', '爱心项目')
        print(r"进入爱心首页")
    except Exception as e:
        print(r"进入爱心首页失败", e)

# 点击进入热门活动
# def hotActivity(driver):
#     try:
#         webhandle = WebHandle(driver)
#         webhandle.Click('噢啦爱心', '热门活动')
#         webhandle.Click('噢啦爱心', '第二个热门活动')
#         # print(r"点击第二个热门活动")
#         # sleep(1)
#         title = UIHandle.get_page_title()
#         UIHandle.get_screent_img('热门活动')
#         print("第一个热门活动的标题是" + ":" + title)
#         UIHandle.back()
#         sleep(1)
#         UIHandle.back()
#         print(r"返回到爱心首页")
#     except Exception as e:
#         print(r"进入热门活动失败", e)
#         # sleep(1)

# 点击进入爱心项目
def loveProject(driver):
    try:
        webhandle = WebHandle(driver)
        webhandle.Click('噢啦爱心', '爱心项目')
        # print(r"进入爱心项目")
        sleep(1)
        # UIHandle.refresh()
        webhandle.Click('噢啦爱心', '第一个爱心项目')
        # print(r"点击第一个爱心项目")
        sleep(2)
        title = UIHandle.get_page_title()
        print("第一个爱心项目的标题是" , ":" ,title)
        sleep(1)
    except Exception as e:
        print(r"进入爱心项目失败", e)
        # sleep(1)

# 点击支持爱心项目
def supportProject(driver,num):
    try:
        webhandle = WebHandle(driver)
        UIHandle.refresh()
        webhandle.Click('噢啦爱心', '支持项目')
        # print(r"点击支持爱心项目")
        sleep(1)
        # webhandle.Click('噢啦爱心', '第一个爱心项目')
        # print(r"点击第一个爱心项目")
        sleep(1)
        beanProject = webhandle.getElementText('噢啦爱心', '当前噢啦豆数量')
        print(r"当前噢啦豆的数量为" + ":" + beanProject)
        webhandle.clearText('噢啦爱心', '支持噢啦豆')
        webhandle.Input('噢啦爱心', '支持噢啦豆', num)
        # sleep(1)
        beanLove = GlobalMap.get('bean')
        # print(beanLove)
        # 对比用户现有噢啦豆与捐献的噢啦豆数量
        if beanLove < num:
            webhandle.Click('噢啦爱心', '支持项目1')
            # toast = webhandle.getText("//div[@class='mint-toast-text']")
            # print(r"支持爱心项目失败", toast)
            print("你的噢啦豆不够捐赠")
            # picName = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            UIHandle.get_screent_img()
        else:
            webhandle.Click('噢啦爱心', '支持项目1')
            # result1 = webhandle.getText("//div[@class='popup project']/div[@class='info']/h3")
            # result2 = webhandle.getText("//div[@class='popup project']/div[@class='info']/p")
            # print(r"支持项目成功", result1, result2)
            webhandle.Click('噢啦爱心', '查看证书')
            sleep(1)
            UIHandle.get_screent_img('爱心证书')
        sleep(1)

    except Exception as e:
        print(r"支持爱心项目失败", e)
        # sleep(1)

# 点击进行以废代捐
# def supportProject(driver):
#     try:
#         webhandle = WebHandle(driver)
#         webhandle.Click('噢啦爱心', '以废代捐')
#         # print(r"点击以废代捐")
#         sleep(1)
#         webhandle.Click('噢啦爱心', '第一个爱心项目')
#         # print(r"点击第一个爱心项目")
#         sleep(1)
#         title = UIHandle.get_page_title()
#         print("第一个爱心项目的标题是" + ":" + title)
#         sleep(1)
#     except Exception as e:
#         print(r"进入爱心项目失败", e)
#         # sleep(1)

if __name__ == "__main__":
    loveModule(driver)
    # hotActivity(driver)
    loveProject(driver)
    supportProject(driver, 2)
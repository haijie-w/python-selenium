# -*- coding: utf-8 -*-
# @Time    : 2019-09-15
# @Vestion :1.0
# @Author  :Allen

# 业务功能脚本（用例脚本可调用此处的功能脚本）

import time
import random

from common.commonFuction import UIHandle
from common.commonFuction import WebHandle
from common.commonFuction import Assert
from config.readConfig import ReadConfig
from common.dataBase import DB
from config.config import browser_config

global driver
driver = browser_config['chrome']

# driver.implicitly_wait(10)


# 噢啦H5用户登录
def login():
    # 打开浏览器
    # 传入driver对象
    # ast = Assert(driver)
    uihandle = UIHandle(driver)
    webhandle = WebHandle(driver)
    driver3 = Assert(driver)
    ReadConfig1 = ReadConfig()
    db = DB()
    # 输入url地址
    uihandle.get(ReadConfig1.get_http("login_testUrl"))
    # 关闭广告页
    webhandle.Click('噢啦h5页面', '广告页')
    # 关闭定位提示
    webhandle.Click('噢啦h5页面', '手动定位按钮')
    # 点击进入个人模块
    page = webhandle.byXPath('噢啦h5页面', '个人模块')
    webhandle.script(page)
    time.sleep(2)
    # 点击进入登录/注册页面
    webhandle.clickElement('平安三春晖登录', '登录页面')
    # 读取配置文件中的任一手机号并输入
    phone = random.choice(eval(ReadConfig1.get_http('phone')))
    print(phone)
    # self.driver2.Click('平安三春晖登录', '输入手机号码')
    webhandle.Input('平安三春晖登录', '输入手机号码', phone)
    # 点击发送验证码
    webhandle.Click('平安三春晖登录', '点击发送验证码')
    uihandle.maxiWindow()
    # 输入6位验证码（code)
    numList = ReadConfig1.get_http('code')
    numList1 = list(numList)
    # print(self.numList1)
    for num in numList1:
        webhandle.Click('平安三春晖登录', '键盘数字' + str(num))
    # 关闭引导图图层（点击噢啦豆图标）
    webhandle.Click('平安三春晖登录', '引导图图层')
    # 查询用户的昵称和豆数是否正确
    credit = db.select_one("SELECT (credit + gold_coin)AS '用户剩余豆数' FROM star_user where phone = '%s' " % (phone))
    creditDb = eval(credit)[0]
    # print(type(self.creditDb))
    # 获取登录页面的用户噢啦豆数量
    credit1 = webhandle.getElementText('噢啦h5页面', '用户噢啦豆')
    creditPage = int(credit1)
    # print(type(self.creditPage))
    # 判断页面噢啦豆数量是否与数据库中一致
    driver3.assertInfoEquals(creditDb, creditPage)
    # self.driver1.refresh()
    # self.driver1.quit()
    return driver

    # 打开子模块


def logInModule(page, module):
    uihandle = UIHandle(driver)
    webhandle = WebHandle(driver)
    time.sleep(2)
    webhandle.Click(page, module)
    time.sleep(2)
    # return driver


driver = login()
logInModule('噢啦h5页面', '噢啦爱心')
logInModule('噢啦h5页面', '环保回收')


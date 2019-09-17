# -*- coding: utf-8 -*-
# @Time    : 2019-09-15
# @Vestion :1.0
# @Author  :Allen

# 业务功能脚本（用例脚本可调用此处的功能脚本）

import sys
from common.commonFuction import UIHandle
from common.commonFuction import WebHandle
from common.commonFuction import Assert
from config.readConfig import ReadConfig
from selenium import webdriver
from common.dataBase import DB
from config.config import browser_config, local_config, local_constant
import time
import random

global driver
driver = browser_config['chrome']
# driver.implicitly_wait(10)


# 打开Matrix首页登录
class Login():
    def __init__(self):
        self.driver1 = UIHandle(driver)
        self.driver2 = WebHandle(driver)
        self.driver3 = Assert(driver)
        self.ReadConfig = ReadConfig()
        self.DB = DB()

    def login(self):
        # 打开浏览器
        # 传入driver对象
        # ast = Assert(driver)
        # 输入url地址
        self.driver1.get(self.ReadConfig.get_http("login_testUrl"))
        # 关闭广告页
        self.driver2.Click('噢啦h5页面', '广告页')
        # 关闭定位提示
        self.driver2.Click('噢啦h5页面', '手动定位按钮')
        # 点击进入个人模块
        page = self.driver2.byXPath('噢啦h5页面', '个人模块')
        self.driver2.script(page)
        time.sleep(2)
        # 点击进入登录/注册页面
        self.driver2.clickElement('平安三春晖登录', '登录页面')
        # 读取配置文件中的任一手机号并输入
        self.phone = random.choice(eval(self.ReadConfig.get_http('phone')))
        print(self.phone)
        # self.driver2.Click('平安三春晖登录', '输入手机号码')
        self.driver2.Input('平安三春晖登录', '输入手机号码', self.phone)
        # 点击发送验证码
        self.driver2.Click('平安三春晖登录', '点击发送验证码')
        self.driver1.maxiWindow()
        # 输入6位验证码（code)
        self.numList = self.ReadConfig.get_http('code')
        self.numList1 = list(self.numList)
        # print(self.numList1)
        for num in self.numList1:
            self.driver2.Click('平安三春晖登录', '键盘数字' + str(num))
        # 关闭引导图图层（点击噢啦豆图标）
        self.driver2.Click('平安三春晖登录', '引导图图层')
        # 查询用户的昵称和豆数是否正确
        self.credit = self.DB.select_one("SELECT (credit + gold_coin)AS '用户剩余豆数' FROM star_user where phone = '%s' "%(self.phone))
        self.creditDb = eval(self.credit)[0]
        print(type(self.creditDb))
        # 获取登录页面的用户噢啦豆数量
        self.credit1 = self.driver2.getElementText('噢啦h5页面', '用户噢啦豆')
        self.creditPage = int(self.credit1)
        print(type(self.creditPage))
        # 判断页面噢啦豆数量是否与数据库中一致
        self.driver3.assertInfoEquals(self.creditDb, self.creditPage)
        # self.driver1.refresh()
        # self.driver1.quit()
        return self.driver1


a = Login()
a.login()

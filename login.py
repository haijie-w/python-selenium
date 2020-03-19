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
class Login():
    def __init__(self):
        self.uihandle = UIHandle(driver)
        self.webhandle = WebHandle(driver)
        self.driver3 = Assert(driver)
        self.ReadConfig = ReadConfig()
        self.DB = DB()

    def login(self):
        # 打开浏览器
        # 传入driver对象
        # ast = Assert(driver)
        # 输入url地址
        self.uihandle.get(self.ReadConfig.get_http("login_testUrl"))
        # 关闭广告页
        self.webhandle.Click('噢啦h5页面', '广告页')
        # 关闭定位提示
        self.webhandle.Click('噢啦h5页面', '手动定位按钮')
        # 点击进入个人模块
        page = self.webhandle.byXPath('噢啦h5页面', '个人模块')
        self.webhandle.script(page)
        time.sleep(2)
        # 点击进入登录/注册页面
        self.webhandle.clickElement('平安三春晖登录', '登录页面')
        # 读取配置文件中的任一手机号并输入
        self.phone = random.choice(eval(self.ReadConfig.get_http('phone')))
        print(self.phone)
        # self.driver2.Click('平安三春晖登录', '输入手机号码')
        self.webhandle.Input('平安三春晖登录', '输入手机号码', self.phone)
        # 点击发送验证码
        self.webhandle.Click('平安三春晖登录', '点击发送验证码')
        self.uihandle.maxiWindow()
        # 输入6位验证码（code)
        self.numList = self.ReadConfig.get_http('code')
        self.numList1 = list(self.numList)
        # print(self.numList1)
        for num in self.numList1:
            self.webhandle.Click('平安三春晖登录', '键盘数字' + str(num))
        # 关闭引导图图层（点击噢啦豆图标）
        self.webhandle.Click('平安三春晖登录', '引导图图层')
        # 查询用户的昵称和豆数是否正确
        self.credit = self.DB.select_one("SELECT (credit + gold_coin)AS '用户剩余豆数' FROM star_user where phone = '%s' "%(self.phone))
        self.creditDb = eval(self.credit)[0]
        print(type(self.creditDb))
        # 获取登录页面的用户噢啦豆数量
        self.credit1 = self.webhandle.getElementText('噢啦h5页面', '用户噢啦豆')
        self.creditPage = int(self.credit1)
        print(type(self.creditPage))
        # 判断页面噢啦豆数量是否与数据库中一致
        self.driver3.assertInfoEquals(self.creditDb, self.creditPage)
        # self.driver1.refresh()
        # self.driver1.quit()
        return self.driver

    # 打开子模块
    def logInModule(self, driver, page, module):
        time.sleep(2)
        self.webhandle.Click(page, module)
        time.sleep(2)
        return driver


a = Login()
a.login()

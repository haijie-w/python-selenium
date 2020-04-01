# -*- coding:utf-8 -*-
from common.login_h5 import login_go
from config.config_h5 import *
from selenium.webdriver.common.by import By
import time
import os
import sys
from time import sleep
import random
from selenium import webdriver
from dateutil.parser import parse


class login():
    path = os.path.join(os.path.dirname(__file__), 'test11_01.py')
    sys.path.append(path)

    # 初始化函数
    def __init__(self):
        self.driver1 = login_go()
        self.driver = self.driver1.driver
        self.url = 'https://oola-m-tt.oola.cn/h5/#/recycle?channel=136_1'
        # self.driver = self.driver
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间：", self.starttime)
        self.driver.get(self.url)

    # # 广告页面弹窗处理
    # def adClose(self):
    # 	try:
    # 		loadAD = element_config["loadAD"]
    # 		self.driver1.loadAD_close(loadAD)
    # 		print(r"关闭首页加载广告")
    # 	except Exception as e:
    # 		print("failed", e)

    # 点击切换到个人模块
    def loginModule(self):
        try:
            personal = element_config['personal']
            self.driver1.personal_change(personal)
            print(r"进入个人模块")
        except Exception as e:
            print(r"进入个人模块失败", e)
        sleep(1)

    # 点击进入到登录/注册页面
    def loginPage(self):
        try:
            login_page = element_config['login_page']
            self.driver1.login_page(login_page)
            print(r"成功进入注册页面")
            phoneText = self.driver.find_element(By.XPATH, "//*[@id='telephone']").text
            print(phoneText)
        except Exception as e:
            print(r"进入登录/注册页面失败", e)

    # 在登录页面输入手机号码
    def phoneInput(self):
        try:
            # 从配置中随机获取一个手机号
            inputNumber = element_config['inputNumber']
            number = random.choice(basic_config.get('phone'))
            self.driver1.phone_input(inputNumber, number)
            print(r"输入手机号成功")
        except Exception as e:
            print(r"输入手机号失败", e)

    # 点击发送验证码
    def sendMessageCode(self):
        try:
            self.driver1.sendCode(element_config.get('sendCode'))
            print(r"成功发送验证码")
        except Exception as e:
            print(r"发送验证码失败", e)
        sleep(2)

    # 输入6位数验证码
    def inputMessageCode(self):
        try:
            self.driver1.inputCode(element_config.get('num3'))
            self.driver1.inputCode(element_config.get('num2'))
            self.driver1.inputCode(element_config.get('num6'))
            self.driver1.inputCode(element_config.get('num6'))
            self.driver1.inputCode(element_config.get('num1'))
            self.driver1.inputCode(element_config.get('num8'))
            print(r"成功输入验证码")
        except Exception as e:
            print(r"验证码输入失败", e)
        sleep(1)

    # 关闭引导图图层（点击噢啦豆图标）
    def clickOola(self):
        self.driver.find_element(By.XPATH, "//*[@id='guide-layer']/div/img").click()

    # 判断登录是否成功
    def panduanLogin(self):
        try:
            name = self.driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[1]/div[1]/div[1]/p")
            name1 = name.text
            print(name1)
            if str(name1).strip() != '':
                print(r"%s登录成功" % name1)
            else:
                print(r"登录失败")
        except Exception as e:
            print(r"登录失败%s" % e)


if __name__ == "__main__":
    login()

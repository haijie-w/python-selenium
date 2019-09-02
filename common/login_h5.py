# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config_h5 import *
import os,time

# 登录类封装
class login_go():
	def __init__(self):
		# 初始化driver参数
		# 通过device name设置模拟的手机设备
		mobile_emulation = {"deviceName": "Galaxy S5"}
		option = webdriver.ChromeOptions()
		option.add_experimental_option('mobileEmulation', mobile_emulation)
		driver = webdriver.Chrome(chrome_options=option)
		self.driver = driver
	# 广告页面弹窗处理
	def loadAD_close(self,element):
		ad = self.driver.find_element(By.XPATH,element)
		ad.click()
	# 点击切换到个人模块
	def personal_change(self,element):
		personal = self.driver.find_element(By.XPATH,element)
		personal.click()

	# 点击进入到登录/注册页面
	def login_page(self,element):
		login_page1 = self.driver.find_element(By.XPATH,element)
		# login_page1.click()
		# self.driver.execute_script("arguments[0].click();",login_page1)
		# 定位到元素后点击元素
		webdriver.ActionChains(self.driver).move_to_element(login_page1).click(login_page1).perform()

	# 在登录页面输入手机号码
	def phone_input(self,element,phoneNumber):
		phone = self.driver.find_element(By.XPATH,element)
		phone.click()
		phone.send_keys(phoneNumber)

	# 点击发送验证码
	def sendCode(self,element):
		generateOTP= self.driver.find_element(By.XPATH,element)
		generateOTP.click()

	# 输入6位数验证码
	def inputCode(self,element):
		num = self.driver.find_element(By.XPATH,element)
		num.click()
if __name__ == "__main__":
	login1 = login_go()
	personal = element_config['personal']
	print(personal)
	login1.personal_change(personal)

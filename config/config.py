# -*- coding:utf-8 -*- 
# Author:Allen
from selenium import webdriver

# 1.浏览器种类维护在此处
# 通过device name设置模拟的手机设备
mobile_emulation = {"deviceName": "Galaxy S5"}
option = webdriver.ChromeOptions()
option.add_experimental_option('mobileEmulation', mobile_emulation)
# driver = webdriver.Chrome(chrome_options=option)

browser_config = {
    'ie': webdriver.Ie,
    'chrome': webdriver.Chrome(chrome_options=option),
    'firefox': webdriver.Firefox
}

local_constant = {
    'LOGIN_MATRIX_URL': 'http://www.baidu.com' # 正式环境
}
# 定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
local_config = {

    '平安三春晖登录': {
        '广告加载页': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[1]/div[2]/div/img"],
        '个人模块': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/a[3]"],
        '登录页面': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[2]"],
	    '输入手机号码': ['xpath', "//input[@id='telephone']"],
	    '点击发送验证码': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div[2]"],
	    '键盘数字1': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]"],
	    '键盘数字2': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]"],
	    '键盘数字3': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[3]"],
	    '键盘数字4': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[1]"],
	    '键盘数字5': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]"],
	    '键盘数字6': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[3]"],
	    '键盘数字7': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[1]"],
	    '键盘数字8': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[2]"],
	    '键盘数字9': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[3]"],
	    '键盘数字0': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[4]/div[2]"],
	    '键盘数字删除': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[4]/div[3]"],
		'百度首页':['xpath',"//*[@id='index-kw']"],
    },
}

# -*- coding:utf-8 -*- 
# Author:Allen
from selenium import webdriver

# 1.浏览器种类维护在此处
# 通过device name设置模拟的手机设备
mobile_emulation = {"deviceName": "Galaxy S5"}
option = webdriver.ChromeOptions()
option.add_experimental_option('mobileEmulation', mobile_emulation)
# driver = webdriver.Chrome(chrome_options=option)

browser_config = {'ie': webdriver.Ie, 'chrome': webdriver.Chrome(chrome_options=option), 'firefox': webdriver.Firefox}

local_constant = {
    # 正式环境
    'H5_Test_URL': 'https://oola-m-tt.oola.cn/h5/#/new-love-project'
}

# 1.基本的配置元素
basic_config = {'url': 'https://oola-m-tt.oola.cn/h5/#/recycle?channel=136_1',
                'phone': [18011723755, 18011723722, 18011722753, 18028567802, 13424083222], 'code': '326618'}

# 平安三春晖定位元素
pingan_config = {'平安三春晖登录': {
    '广告加载页': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[1]/div[2]/div/img"],
    # '个人模块': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/a[3]"],
    '个人模块': ['xpath', "//*[@id='app']/div[2]/div[1]/div[6]/div[2]/a[3]/div[2]/div"],
    '登录页面': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[2]"],
    '输入手机号码': ['xpath', "//input[@id='telephone']"],
    '点击发送验证码': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div[2]"],
    '引导图图层': ['xpath', "//*[@id='guide-layer']/div/img"],
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
},
}

# H5页面定位信息维护在此处，维护结构由外到内为：页面名称--页面下元素名称--元素的定位方式+参数
local_config = {

    '个人页面': {
        # '个人模块': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/a[3]/div[2]"],
        '噢啦爱心首页': ['xpath', "//div[@class='tabbar-icon-1']"],
        '环保回收页': ['xpath', "//div[@class='tabbar-icon-2']"],
        '个人模块': ['xpath', "//div[@class='tabbar-icon-3']"],
        '登录按钮': ['xpath', "//div[@class='notLogin-info']"],
        '广告页': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[1]/div[2]/div/img"],
        '手动定位按钮': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[3]/div[3]/div[2]/div/div/img"],
        '用户昵称': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div[1]/p"],
        # '用户噢啦豆': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[2]/span"],
        '用户噢啦豆': ['xpath', "//div[@class='bean-num']/span"],
        '输入手机号': ['xpath', "//input[@id='telephone']"],
        '发送验证码': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div[2]"],
        '数字1': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]"],
        '数字2': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]"],
        '数字3': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[3]"],
        '数字4': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[1]"],
        '数字5': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]"],
        '数字6': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[3]"],
        '数字7': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[1]"],
        '数字8': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[2]"],
        '数字9': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[3]"],
        '数字0': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[4]/div[2]"],
        '删除': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[4]/div[3]"],
        '引导图图层': ['xpath', "//*[@id='guide-layer']/div/img"],
        '用户头像': ['xpath', "//div[@class='basic-info']/img"],
        # '用户噢啦豆':['xpath', "//div[@class='notLogin-info']/img"],
        # '用户ID':['xpath', "//ul[@class='info-list']/li[4]/span[2]"],
        '用户ID': ['xpath', "//*[@id='app']/div[2]/div[1]/ul/li[4]/span[2]"],
        '回收订单': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[3]/h1"],
        '爱心记录': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[4]/h1"],
        '任务中心': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[5]/h1"],
        '噢啦日签': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[6]/h1"],
        '消息中心': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[7]/h1"],
        '联系客服': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[8]/h1"],

    }
}

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
    'H5_Test_URL': 'https://oola-m-tt.oola.cn/h5/#/new-love-project',
    # uat环境
    'H5_uat_URL': 'https://uat.oola.cn/h5/#/new-love-project',
}

# 1.基本的配置元素
basic_config = {'url': 'https://oola-m-tt.oola.cn/h5/#/recycle?channel=136_1',
                'phone': [18011723750, 18011723722,18562659835, 18011722533, 18022569802, 13421083222], 'code': '326618'}

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
        '数字1': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[1]/div[1]"],
        '数字2': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[1]/div[2]"],
        '数字3': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[1]/div[3]"],
        '数字4': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[2]/div[1]"],
        '数字5': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[2]/div[2]"],
        '数字6': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[2]/div[3]"],
        '数字7': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[3]/div[1]"],
        '数字8': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[3]/div[2]"],
        '数字9': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[3]/div[3]"],
        '数字0': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[4]/div[2]"],
        '删除': ['xpath', "//div[@class='verify-code bgi-com']/div[1]/div[3]/div[4]/div[3]"],
        '引导图图层': ['xpath', "//*[@id='guide-layer']/div/img"],
        '用户头像': ['xpath', "//div[@class='basic-info']/img"],
        '我的地址': ['xpath', "//ul[@class='info-list']/li[3]"],
        '添加地址': ['xpath', "//*[@class='add-addr']/div"],
        '联系人': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div[1]/div/input"],
        '地址': ['xpath', "//div[@class='extra-item']/input"],
        '地址选择框': ['xpath', "//div[@class='search-box']/div"],
        '广州': ['xpath', "//div[@class='hot-city-list']/div[3]"],
        # '搜索城市': ['xpath', "//div[@class='search-box']/input"],
        '搜索城市':['xpath',"//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div[1]/input"],
        '第一个结果': ['xpath', "//div[@class='address-list']/div[1]/div[1]"],
        '详细地址': ['xpath', "//*[@id='app']/div[2]/div[1]/div[1]/div/div[5]/div/input"],
        '设置默认地址': ['xpath', "//div[@class='oCheckbox-wrapper']/div[1]"],
        '完成添加地址': ['xpath', "//div[@class='bottom-btn']"],
        # '用户噢啦豆':['xpath', "//div[@class='notLogin-info']/img"],
        # '用户ID':['xpath', "//ul[@class='info-list']/li[4]/span[2]"],
        '用户ID': ['xpath', "//*[@id='app']/div[2]/div[1]/ul/li[4]/span[2]"],
        # '回收订单': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[3]/h1"],
        # '爱心记录': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[4]/h1"],
        # '任务中心': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[5]/h1"],
        # '噢啦日签': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[6]/h1"],
        # '消息中心': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[7]/h1"],
        # '联系客服': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/div[8]/h1"],
        '回收订单': ['xpath', "//div[@class='inner-content']/div[3]/h1"],
        '爱心记录': ['xpath', "//div[@class='inner-content']/div[4]/h1"],
        '任务中心': ['xpath', "//div[@class='inner-content']/div[5]/h1"],
        '噢啦日签': ['xpath', "//div[@class='inner-content']/div[6]/h1"],
        '消息中心': ['xpath', "//div[@class='inner-content']/div[7]/h1"],
        '联系客服': ['xpath', "//div[@class='inner-content']/div[8]/h1"],
        '机构合作咨询': ['xpath', "//div[@class='inner-content']/div[9]/h1"],
        '关于噢啦': ['xpath', "//div[@class='inner-content']/div[10]/h1"]

    },


    '噢啦爱心': {
        '热门活动': ['xpath', "//div[@class='item-area']/div[1]/div[1]/img"],
        '爱心项目': ['xpath', "//div[@class='item-area']/div[1]/div[2]/img"],
        '爱心商城': ['xpath', "//div[@class='item-area']/div[1]/div[3]/img"],
        '环保资讯': ['xpath', "//div[@class='item-area']/div[1]/div[4]/img"],
        '首页banner(1)': ['xpath', "//div[@class='oola-autoHeightBanner banner-area']/div[1]/div[1]/div[1]/div[1]/img"],
        '第一个热门活动': ['xpath', "//div[@class='list']/div[1]/img"],
        '第二个热门活动': ['xpath', "//div[@class='list']/div[2]/img"],
        '更多热门公益项目': ['xpath', "//div[@class='hot-welfare-area']/div[1]/div[2]/img"],
        # '第一个爱心项目': ['xpath', "//div[@class='page-loadmore-wrapper']/ul/li[1]/img"],
        '第一个爱心项目': ['xpath', "//*[@id='app']/div[2]/div[1]/div[2]/ul/li[1]/img"],
        '以废代捐': ['xpath', "//div[@class='project-detail']/div[7]/div[1]/span"],
        '支持项目': ['xpath', "//div[@class='project-detail']/div[7]/div[2]"],
        '项目详情页引导图': ['xpath', "//div[@class='guide-layer']/div[2]/img"],
        '当前噢啦豆数量': ['xpath', "//div[@class='popup']/div[1]/p/span[1]"],
        '支持噢啦豆': ['xpath', "//div[@class='popup']/div[1]/div/label/input"],
        '支持项目1': ['xpath', "//div[@class='immediate-recovery immediate-recovery-prohibit']/span"],



    },

    '环保回收': {
        '选择发起回收地址': ['xpath', "//div[@class='position flex-line addr']/img"],
        '广州': ['xpath', "//div[@class='content is-prepend']/li[3]/div"],
        '衣帽鞋包': ['xpath', "//div[@class='recycle-list']/div[1]/div[1]/img"],
        '手机数码': ['xpath', "//div[@class='recycle-list']/div[1]/div[2]/img"],
        '闲置家电': ['xpath', "//div[@class='recycle-list']/div[1]/div[3]/img"],
        '家用电器': ['xpath', "//div[@class='recycle-list']/div[1]/div[4]/img"],
        '衣帽鞋包的开通区域': ['xpath', "//div[@class='open-area']/div[2]/div[1]/img"],
        '手机数码的开通区域': ['xpath', "//div[@class='open-area']/div[2]/div[2]/img"],
        '闲置家电的开通区域': ['xpath', "//div[@class='open-area']/div[2]/div[3]/img"],
        '家用电器的开通区域': ['xpath', "//div[@class='open-area']/div[2]/div[4]/img"],
        '下单时减少回收重量': ['xpath', "//div[@class='choose-count flex-row']/div[2]/div[1]/img[1]"],
        '下单时增加回收重量': ['xpath', "//div[@class='choose-count flex-row']/div[2]/div[1]/img[2]"],
        '下单时输入回收重量': ['xpath', "//div[@class='choose-count flex-row']/div[2]/div[1]/input"],
        '下单时的预计噢啦豆数量': ['xpath', "//div[@class='bottom-area flex-row ']/div[1]/div[1]"],
        '确定回收品类数量': ['xpath', "//div[@class='bottom-area flex-row ']/div[2]"],
        '选择上门取件地址': ['xpath', "//div[@class='address part-item']/div[2]/div[1]"],
        '选择上门取件时间': ['xpath', "//div[@class='time part-item']/div[2]/div[1]"],






    }
}

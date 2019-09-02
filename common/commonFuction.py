#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/13 16:42
# @Author : whj

# 封装部分维护在此
from datetime import *
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from config.config import local_config
from log.logger import *
from getRootPath import root_dir


# 断言判断类
# class Assert():
#     logger = Logger()
#
#     @classmethod
#     def __init__(cls, driver):
#         cls.driver = driver
#
#     # 判断xpath是否存在，若存在返回True，否则返回False
#     @classmethod
#     def assertXPathExistByXPath(cls, page, element):
#         try:
#             WebHandle.byXPath(page, element)
#             cls.logger.mylogger('Element is exist!')
#             return True
#         except Exception as e:
#             cls.logger.mylogger('Element does not exist!',e)
#             # raise Exception
#             return False
#
#     # 判断id是否存在，若存在返回True，否则返回False
#     # 不存在return False,在调用该函数的地方raise Exception，因为要刷新页面逻辑难处理
#     @classmethod
#     def assertElementExistByID(cls, page, element):
#         try:
#             WebHandle.byId(page, element)
#             cls.logger.mylogger(element + ' is exist!')
#             return True
#         except Exception:
#             cls.logger.mylogger(element + ' does not exist!', -1)
#             # raise Exception
#             return False
#
#     # 判断页面上是否存在某个特定的文字，若存在返回True，否则返回False
#     @classmethod
#     def assertTextExist(cls, page, element, str):
#         ele = WebHandle.getElementText(page, element)
#         if str == ele:
#             cls.logger.mylogger(str + 'is exist!')
#             return True
#         else:
#             cls.logger.mylogger(str + ' does not exist!', -1)
#             html = Logger.creatHtml(picpath, pics)
#             Logger.mylogger(html)
#             raise Exception
#
#     # 字符串信息比较，返回比较结果正确与否
#     @classmethod
#     def assertInfoEquals(cls, str1, str2):
#         if str1 == str2:
#             cls.logger.mylogger("Info is matching")
#             return True
#         else:
#             cls.logger.mylogger("Info is mismatching", -1)
#             html = Logger.creatHtml(picpath, pics)
#             Logger.mylogger(html)
#             raise Exception
#
#     # 字符串信息比较不一致，不一致则返回true
#     @classmethod
#     def assertInfoNotEquals(cls, str1, str2):
#         if str1 == str2:
#             cls.logger.mylogger(str1 + " is equal to " + str2, -1)
#             html = Logger.creatHtml(picpath, pics)
#             Logger.mylogger(html)
#             raise Exception  # return False
#         else:
#             cls.logger.mylogger(str1 + " is not equal to " + str2)
#             return True
#
#     # 判断整个页面上是否存在某个特定的文字，若存在返回True，否则返回False
#     @classmethod
#     def assertPageTextExist(cls, path):
#         try:
#             ele = cls.driver.find_element_by_xpath(path)
#             cls.logger.mylogger(path + 'is exist!')
#             return True
#         except Exception as e:
#             cls.logger.mylogger(path + ' does not exist!', -1)
#             html = Logger.creatHtml(picpath, pics)
#             Logger.mylogger(html)
#             raise Exception

# 网页操作类
class WebHandle():
    logger = Log()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    #   # 输入地址
    # @classmethod
    # def get(cls, url):
    #     # cls.logger.loginfo(url)
    #     cls.driver.get(url)

    # send_keys方法
    @classmethod
    def Input(cls, page, element, msg):
        el = cls.element(page, element)
        el.send_keys(msg)

    # click方法
    @classmethod
    def Click(cls, page, element):
        el = cls.element(page, element)
        el.click()

    # 一直等待某个元素消失，默认超时10秒
    # def elementIsNotVisible(cls, page, element):
    #     try:
    #         el = WebDriverWait(UIHandle.driver, 10).until_not(
    #             EC.presence_of_element_located(local_config[page][element]))
    #         cls.logger.mylogger(page + element + 'is not display')
    #         return True
    #     except TimeoutException:
    #         cls.logger.mylogger(page + element + 'is displayed', -1)
    #         return False

    # elements对象(还未完成。。。)
    def elements(cls, page, element):
        # 加入日志
        # cls.logger.loginfo(page)
        # 加入隐性等待
        WebDriverWait(cls.driver, 10)
        els = cls.driver.find_elements(*local_config[page][element])
        # 注意返回的是list
        return els

    # element对象（还可加入try，截图等。。。）
    @classmethod
    def element(cls, page, element):
        # 加入日志
        # cls.logger.mylogger(page)
        # 加入隐性等待
        # 此处便可以传入config_o1中的dict定位参数
        el = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(local_config[page][element]))
        # 加入日志
        cls.logger.info(page + " " + element + 'OK')
        return el

    # 多种定位方式
    @classmethod
    def byId(cls, page, element):
        return cls.driver.find_element_by_id(local_config[page][element][1])

    @classmethod
    def byCssSelector(cls, page, element):
        return cls.driver.find_element_by_css_selector(local_config[page][element][1])

    @classmethod
    def byLinkText(cls, page, element):
        return cls.driver.find_element_by_link_text(local_config[page][element][1])

    @classmethod
    def byLinkTextByStr(cls, str):
        return cls.driver.find_element_by_link_text(str)

    @classmethod
    def byXPath(cls, page, element):
        return cls.driver.find_element_by_xpath(local_config[page][element][1])

    @classmethod
    def byTagName(cls, page, element):
        return cls.driver.find_element_by_tag_name(local_config[page][element][1])

    # 定位下拉框
    @classmethod
    def SelectText(cls, v1):
        select = Select(cls.driver.find_element_by_tag_name('select'))
        select.select_by_visible_text(v1)

    # 获取页面上的数据
    @classmethod
    def getText(cls, path):
        return cls.driver.find_element_by_xpath(path).text

    # 返回element的text值
    @classmethod
    def getElementText(cls, page, element):
        return cls.byXPath(page, element).text

    # 清除元素的内容
    # Zoe @2017-08-14
    @classmethod
    def clearText(cls, page, element):
        el = cls.element(page, element)
        el.clear()

    # 处理删除确认弹窗
    # Allen @2017-09-03 Creat
    @classmethod
    def alter1(cls):
        aa = cls.driver.switch_to_alter
        time.sleep(1)
        aa.accept()

    # 鼠标悬停方法
    # page, element是悬停元素的路径
    @classmethod
    def moveToElement(cls, page, element):
        path = local_config[page][element][1]
        e = cls.driver.find_element_by_xpath(path)
        ActionChains(cls.driver).move_to_element(e).perform()

    # 鼠标右击方法，page和element定位到要右击的元素路径
    @classmethod
    def rightClick(cls, page, element):
        path = local_config[page][element][1]
        e = cls.driver.find_element_by_xpath(path)
        ActionChains(cls.driver).context_click(e).perform()

# 用户界面操作类
class UIHandle():
    Logger = Log()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver
        cls.logger = Log()

    # 输入地址
    @classmethod
    def get(cls, url):
        # cls.logger.loginfo(url)
        cls.driver.get(url)

    # 浏览器前进操作
    @classmethod
    def forward(cls):
        cls.driver.forward()
        cls.Logger.info("Click forward on current page.")

        # 浏览器前进操作

    @classmethod
    def back(cls):
        cls.driver.back()
        cls.Logger.info("Click back on current page.")

    # 浏览器最大化
    @classmethod
    def maxiWindow(cls):
        cls.driver.maximize_window()
        cls.Logger.info(r"浏览器最大化")

        # 刷新页面

    @classmethod
    def refresh(cls):
        cls.driver.refresh()
        cls.Logger.info(r"刷新页面")

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # 截图
    @classmethod
    def getScreenshots(cls, filename):
        file_path = os.path.join(root_dir, "img")  # 设置截图保存路径
        # cls.scrollUpScreen()
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 获取当前系统时间
        img_name = file_path + rq + '.png'  # 设置截图名称格式
        try:
            cls.driver.get_screenshot_as_file(img_name)
        except NameError as e:
            cls.getScreenshots()
            # cls.scrollDownScreen()

    @classmethod
    def get_screenshot_as_file(cls, filename):
        cls.driver.get_screenshot_as_file(filename)

        # if __name__ == '__main__':
        #     driver=browser_config['chrome']()
        #     a = UIHandle(driver)
        #     a.get('http://www.baidu.com')
        #     b = WebHandle(driver)
        #     c = Assert(driver)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/13 16:42
# @Author : whj

# 封装部分维护在此
from datetime import *
import os
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from config.config import local_config
from common.logger import Log
from common import readPath


# 断言判断类
class Assert():
    logger = Log()

    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 判断xpath是否存在，若存在返回True，否则返回False
    @classmethod
    def assertXPathExistByXPath(cls, page, element):
        try:
            WebHandle.byXPath(page, element)
            cls.logger.info('Element is exist!')
            return True
        except Exception as e:
            cls.logger.error(e)
            # raise Exception
            return False

    # 判断id是否存在，若存在返回True，否则返回False
    # 不存在return False,在调用该函数的地方raise Exception，因为要刷新页面逻辑难处理
    @classmethod
    def assertElementExistByID(cls, page, element):
        try:
            WebHandle.byId(page, element)
            cls.logger.info(element + ' is exist!')
            return True
        except Exception as e:
            cls.logger.error(e)
            # raise Exception
            return False

    # 判断页面上是否存在某个特定的文字，若存在返回True，否则返回False
    @classmethod
    def assertTextExist(cls, page, element, str):
        ele = WebHandle.getElementText(page, element)
        if str == ele:
            cls.logger.info(str + 'is exist!')
            return True
        else:
            cls.logger.error(str + ' does not exist!')
            raise Exception

    # 判断页面上是否存在某个特定的文字，进行模糊匹配，若存在返回True，否则返回False
    @classmethod
    def assertTextExist1(cls, page, element, str):
        ele = WebHandle.getElementText(page, element)
        if str in ele:
            cls.logger.info(str + 'is exist!')
            return True
        else:
            cls.logger.error(str + ' does not exist!')
            raise Exception

    # 字符串信息比较，返回比较结果正确与否
    @classmethod
    def assertInfoEquals(cls, str1, str2):
        if str1 == str2:
            cls.logger.info("Info is matching")
            return True
        else:
            cls.logger.error("Info is mismatching")
            raise Exception

    # 字符串信息比较不一致，不一致则返回true
    @classmethod
    def assertInfoNotEquals(cls, str1, str2):
        if str1 == str2:
            cls.logger.info(str1 + " is equal to " + str2)
            raise Exception  # return False
        else:
            cls.logger.error(str1 + " is not equal to " + str2)
            return True

    # 判断整个页面上是否存在某个特定的文字，若存在返回True，否则返回False
    @classmethod
    def assertPageTextExist(cls, path):
        try:
            ele = cls.driver.find_element_by_xpath(path)
            cls.logger.info(path + 'is exist!')
            return True
        except Exception as e:
            cls.logger.error(e)
            raise Exception


# 网页操作类
class WebHandle():
    logger = Log()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    # 输入地址
    @classmethod
    def get(cls, url):
        cls.logger.info(r'打开页面:%s' % url)
        cls.driver.get(url)

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

    # 定位到元素后点击元素
    @classmethod
    def clickElement(cls, page, element):
        e1 = cls.element(page, element)
        ActionChains(cls.driver).move_to_element(e1).click(e1).perform()

    # 一直等待某个元素消失，默认超时10秒
    @classmethod
    def elementIsNotVisible(cls, page, element):
        try:
            # e2 = WebDriverWait(cls.driver, 10).until()
            el = WebDriverWait(cls.driver, 10).until_not(EC.presence_of_element_located(local_config[page][element]))
            cls.logger.info(page + "-" + element + 'is not display')
            return True
        except TimeoutException:
            cls.logger.info(page + element + 'is displayed')
            return False

    # elements对象(还未完成。。。)
    @classmethod
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
        try:
            # 加入隐性等待
            # 此处便可以传入config文件中的dict定位参数
            el = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(local_config[page][element]))
            # 加入日志
            cls.logger.info(page + "-" + element + " " + 'is display')
            return el
        except TimeoutException:
            cls.logger.info(page + "-" + element + " " + 'is not display')

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

    # 另外一种方法选择下拉框,根据option的位置选择内容
    @classmethod
    def selectByIdNo(cls, page, element, num):
        cls.byId(page, element).find_elements_by_tag_name("option")[num].click()

    # 另外一种方法选择下拉框,根据option的位置选择内容

    @classmethod
    def selectByxpathNo(cls, page, element, num):
        cls.byXPath(page, element).find_elements_by_tag_name("option")[num].click()

    def switch_iframe(cls, id_index_locator):
        '''切换iframe'''
        if isinstance(id_index_locator, int):
            cls.driver.switch_to.frame(id_index_locator)
        elif isinstance(id_index_locator, str):
            cls.driver.switch_to.frame(id_index_locator)

    # 获取页面上的数据
    @classmethod
    def getText(cls, path):
        return cls.driver.find_element_by_xpath(path).text

    # 获取页面元素的属性
    @classmethod
    def get_attribute(cls, page, element, name):
        return cls.byXPath(page, element).get_attribute(name)

    # 返回element的text值
    @classmethod
    def getElementText(cls, page, element):
        return cls.byXPath(page, element).text

    # 清除元素的内容
    @classmethod
    def clearText(cls, page, element):
        el = cls.element(page, element)
        el.clear()

    # 警告框处理
    @classmethod
    def alter1(cls):
        try:
            return cls.driver.switch_to_alter().accept()
        except Exception as msg:
            cls.logger.info(msg)

    # 处理JavaScript脚本方法
    @classmethod
    def script(cls, src):
        return cls.driver.execute_script(src)

    # a = "arguments[0].click();",

    # 界面框滚动到顶部
    @classmethod
    def js_scroll_top(cls):
        js = "window.scrollTo(0,0)"
        return cls.script(js)

    # 界面框滚动到顶部
    @classmethod
    def js_scroll_end(cls, x=0):
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        return cls.script(js)

    # 内部框滚动到指定位置
    @classmethod
    def js_scroll_end_id(cls, value, x):
        js = "document.getElementById('%s').scrollTop=%d" % (value, x)
        return cls.script(js)

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

    # 浏览器后退操作
    @classmethod
    def back(cls):
        cls.driver.back()
        cls.Logger.info("Click back on current page.")

    # 浏览器最大化
    @classmethod
    def maxiWindow(cls):
        cls.driver.maximize_window()
        cls.Logger.info(r"浏览器最大化")

    # 获取当前页面的url
    @classmethod
    def get_current_page_url(cls):
        return cls.driver.current_url

    # 获取当前页面的title
    @classmethod
    def get_page_title(cls):
        return cls.driver.title

    # 刷新页面
    @classmethod
    def refresh(cls):
        cls.driver.refresh()
        cls.Logger.info(r"刷新页面")

    # 关闭浏览器驱动
    @classmethod
    def quit(cls):
        cls.driver.quit()

    # 关闭浏览器子窗口驱动
    @classmethod
    def quitNewWindow(cls):
        # 获取当前所有窗口句柄（窗口A、B）
        handles = cls.driver.window_handles
        # 对窗口进行遍历
        for newhandle in handles:
            # 关闭新打开的窗口
            if newhandle != handles[0]:
                cls.driver.switch_to_window(newhandle)
                cls.driver.close()
        # 返回主窗口
        cls.driver.switch_to_window(handles[0])

    # 截图
    @classmethod
    def get_screent_img(cls, imgName=None):
        # 设置截图保存路径
        file_path = readPath.Img_DIR
        # cls.scrollUpScreen()
        if imgName != None:
            imgName = imgName
        else:
            imgName = "页面截图"
        nowdate = datetime.now().strftime('%Y%m%d')  # 当日日期
        screenshot_today_dir = os.path.join(file_path, nowdate)  # 当前日期文件夹
        if not os.path.exists(screenshot_today_dir):
            os.mkdir(screenshot_today_dir)  # 不存在则创建
        nowtime = datetime.now().strftime('%H%M%S%f')  # 时间戳
        filename = nowtime + imgName + ".png"  # 拼接文件名 时间戳+文件名+.png
        filepath = os.path.join(screenshot_today_dir, filename)
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  #获取当前系统时间
        # 设置截图名称格式
        # img_name = file_path + '\\' + imgName + '.png'
        try:
            cls.driver.get_screenshot_as_file(filepath)
        # cls.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"D:\untitled\loginH5\img"), img_name))
        except NameError as e:
            cls.logger.info(r'截图失败', e)  # cls.scrollDownScreen()

    @classmethod
    def get_screenshot_as_file(cls, filename):
        cls.driver.get_screenshot_as_file(filename)

# if __name__ == '__main__':
#     driver=browser_config['chrome']()
#     a = UIHandle(driver)
#     a.get('http://www.baidu.com')
#     b = WebHandle(driver)

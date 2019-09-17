# -*- coding: utf-8 -*-
# @Time    : 2017-08-10
# @Vestion :1.0
# @Author  :Zoe Zhou

import unittest

from common.login import Login
from common.commonFuction import *


# 产品管理01--用户创建一个新产品
class Case_01(unittest.TestCase):
    def setUp(self):  # 执行测试用例之前做的事
        picpath = []
        pics = []
        driver = Login()
        driver.logInModule(driver, 'Matrix首页', '产品管理')

    def test1(self):
        # 创建产品
        # createProduct(driver, u'测试产品',u'测试产品机构')
        # 判断产品创建完成后的字段是否正确
        Assert.assertPageTextExist('//*[contains(text(),"测试产品")]')
        Assert.assertTextExist('产品管理页', '验证产品种类', u'股票,其他,期货,外汇')
        Assert.assertTextExist('产品管理页', '验证所属机构', u'测试产品机构')
        Assert.assertTextExist('产品管理页', '验证总净资产', '400,000.00')
        Assert.assertTextExist('产品管理页', '验证累计收益率', '0.00%')
        Assert.assertPageTextExist('//*[contains(text(),"没有数据")]')

        # def tearDown(self):#执行测试用例后续操作
        # 删除产品
        # detailProduct(driver)
        # deletePro(driver)


if __name__ == "__main__":
    unittest.main()

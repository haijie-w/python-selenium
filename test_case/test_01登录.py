# -*- coding:utf-8 -*-
from common.login_h5 import login_go
from config.config_h5 import *
from selenium.webdriver.common.by import By
import unittest
from BeautifulReport import BeautifulReport
from test_case.test11_01 import *
from dateutil.parser import parse

class loginH5(unittest.TestCase):
	# 屏幕截图
	def get_screent_img(self,img_name):
		try:
			self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"D:\untitled\loginH5\img"), img_name))
		except Exception as e:
			print("截图失败", e)
	# 初始化函数
	@classmethod
	def setUpClass(cls):
		# driver 实例化
		cls.login1_h5 = login()
		cls.driver = cls.login1_h5.driver
		cls.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		# 用例开始执行时间
		print("开始测试时间：", cls.starttime)

	@BeautifulReport.add_test_img('测试报告')
	# 登录函数
	def test_loginInH5(self):
		# 定义用例的描述信息
		self.caseName = 'H5页面登录（平安三春晖）'
		self.__dict__['_testMethodDoc'] = self.caseName
		# 广告页面弹窗处理
		# self.login1_h5.adClose()
		# 点击切换到个人模块
		self.login1_h5.loginModule()
		# 点击进入到登录/注册页面
		self.login1_h5.loginPage()
		time.sleep(1)
		phoneText = self.driver.find_element(By.XPATH, "//*[@id='telephone']").text
		print(phoneText)
		# self.assertEqual(phoneText,r'请输入手机号码')
		# 在登录页面输入手机号码
		self.login1_h5.phoneInput()
		# 点击发送验证码
		self.login1_h5.sendMessageCode()
		codeText = self.driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div[1]/div[1]/div/p/text()[1]").text
		self.assertEqual(codeText, r'已发送6位验证码至')
		# 输入6位数验证码
		self.login1_h5.inputMessageCode()
		# 关闭引导图图层（点击噢啦豆图标）
		self.login1_h5.clickOola()
		# 保存登录后的截图
		now = int(time.time())
		name = str(now) + '登录成功'
		self.get_screent_img(name)
		# 判断登录是否成功
		self.login1_h5.panduanLogin()

	# 结束函数
	@classmethod
	def tearDownClass(cls):
		# cls.driver.quit()
		cls.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		print("测试结束时间：", cls.endtime)
		totaltime = (cls.endtime - cls.starttime).total_seconds()
		print("总时长：", totaltime, "秒")

if __name__ == "__main__":
	# login1 = loginH5()
	# login1.test01()
	unittest.main(verbosity=2)


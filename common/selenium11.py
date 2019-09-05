# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
import time
#通过device name设置模拟的手机设备
mobile_emulation = {"deviceName":"Galaxy S5"}
option = webdriver.ChromeOptions()
option.add_experimental_option('mobileEmulation',mobile_emulation)
driver = webdriver.Chrome(chrome_options=option)
# browser = webdriver.Chrome()
driver.get('https://oola-m-tt.oola.cn/h5/#/recycle?channel=136_1')
print("打开h5页面")
print(driver.title)
# 广告页面弹窗处理
suspondWindow = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[1]/div[1]/div[2]/div/img")
suspondWindow.click()
print("searchKey: Suspond Page1 had been closed.")
time.sleep(1)
#点击切换到个人模块
personal = driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[1]/div[2]/a[3]")
personal.click()
time.sleep(1)
print(r"进入个人模块")
#点击进入到登录/注册页面
login_page = driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[1]/div[1]/div[2]")
# login_page = driver.find_element(By.XPATH,"//*[@class='notLogin-info']/p")
login_page.click()
time.sleep(2)
print(r"成功进入注册页面")
#在登录页面输入手机号码
login = driver.find_element(By.XPATH,"//input[@id='telephone']")
login.click()
login.send_keys('18011723755')
print("输入手机号成功")
#点击发送验证码
generateOTP = driver.find_element(By.XPATH,"//*[@id='app']/div[2]/div[1]/div[1]/div/div[2]")
generateOTP.click()
print("发送验证码成功")
time.sleep(2)
#输入6位数验证码
num_list = {"num1":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]",
"num2":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]",
"num3":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[3]",
"num4":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[1]",
"num5":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]",
"num6":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[3]",
"num7":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[1]",
"num8":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[2]",
"num9":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[3]/div[3]",
"num0":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[4]/div[2]",
"DEL":"//*[@id='app']/div[2]/div[1]/div[1]/div/div/div/div[3]/div[4]/div[3]",}
#第三方测试登录验证码为：326618
driver.find_element(By.XPATH,num_list.get("num3")).click()
driver.find_element(By.XPATH,num_list.get("num2")).click()
driver.find_element(By.XPATH,num_list.get("num6")).click()
driver.find_element(By.XPATH,num_list.get("num6")).click()
driver.find_element(By.XPATH,num_list.get("num1")).click()
driver.find_element(By.XPATH,num_list.get("num8")).click()
time.sleep(0.5)
print(driver.title)
time.sleep(3)
driver.quit()




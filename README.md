#Python+selenium UI自动化测试

这是一个基于Python+selenium+unittest+HTMLTestRunner实现的web自动化框架

###安装与启动

安装Python3版本，确保加入环境变量，pip命令可用

需要把BeautifulReport文件夹放到python的lib文件site-packages下面

##从Github项目下载源码
git clone https://github.com/haijie-w/python-selenium.git

##进入项目目录后执行以下命令：
pip install -r requirements.txt

##目录结构
1. commom 公共方法模块

1.1 commonFuction.py 封装页面元素定位和操作方法

1.2 logger.py 日志方法

1.3 newReport.py 获取最新日志，报告或截图文件

1.4 readPath.py 获取每个目录的路径

1.5 sendEmail.py 发送包含附件的邮件

2. config 配置文件

2.1 config.ini 邮件发送和测试地址相关的配置信息

2.2 config.py 浏览器driver和页面元素定位地址的配置文件

2.3 readConfig.py 读取config.ini配置文件中的内容

3. img 截图文件夹

4. log 日志文件夹

5. report 测试报告文件夹

6. test_case 测试用例文件夹

7. run.py 执行自动化测试用例

# -*- coding:utf-8 -*-
"""
@Time    : 2019-09-01 14:03
@Author  : Allen
@FileName: sendEmail.py
@IDE     : PyCharm
"""
import smtplib
from config.readConfig import *
from common import readPath
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common.newReport import new_report
from email.mime.text import MIMEText
from email.header import Header

class SendEmail:
    def __init__(self):
        # 读取配置文件中的用户信息
        self.url = ReadConfig()
        # 设置服务器
        self.mail_host = self.url.getConfig("Email_config","HOST_SERVER")
        # 用户名
        self.mail_user = self.url.getConfig("Email_config","user")
        # 口令(qq邮箱非密码)
        self.mail_pass = self.url.getConfig("Email_config","password")
        # 发送邮件账号
        self.sender = self.url.getConfig("Email_config","FROM")
        # 接收邮箱，可设置为你的QQ邮箱或者其他邮箱
        self.receivers = self.url.getConfig("Email_config","TO")
        # 邮件标题
        self.subject = self.url.getConfig("Email_config","SUBJECT")
    def send_email(self):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receivers
        message['Subject'] = Header(self.subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText('这是邮件的正文,请注意查收', 'plain', 'utf-8'))

        # 构造附件1（附件为HTML格式的网页）
        file1 = new_report(readPath.TEST_REPORT,-1)
        att1 = MIMEText(open(file1,'rb').read(),'base64','utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename = file1'
        message.attach(att1)

        # 构造附件2（附件为txt格式的log文件）
        file2 = new_report(readPath.LOG_DIR,-3)
        att2 = MIMEText(open(file2,'rb').read(),'base64','utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename = file2'
        message.attach(att2)

        # 构造附件3（附件为png格式的图片）
        file3 = new_report(readPath.Img_DIR,-1)
        att3 = MIMEText(open(file3,'rb').read(),'base64','utf-8')
        att3["Content-Type"] = 'application/octet-stream'
        att3["Content-Disposition"] = 'attachment; filename = file3'
        message.attach(att3)

        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print("邮件发送成功")

        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)


notice = SendEmail()
notice.send_email()
# coding=utf-8 
"""
@Time    : 2019/09/01  下午 15:36
@Author  : Allen
@FileName: sendEmail.py
@IDE     : PyCharm
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = '921519025@qq.com'
password = "whjzll0702"
sender = username
receivers = ','.join(['791098673@qq.com'])


def email(report):
    # 设置请求头信息
    msg = MIMEMultipart()
    msg['Subject'] = 'Web测试报告'  # 邮件名
    msg['From'] = sender
    msg['To'] = receivers

    jpgpart = MIMEApplication(open(report, 'rb').read())
    jpgpart.add_header('Content-Disposition', 'attachment', filename='Web测试报告.html')
    msg.attach(jpgpart)

    # 发送邮件
    client = smtplib.SMTP()
    client.connect('smtp.qq.com')
    client.login(username, password)
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print("邮件发送成功，请查看")

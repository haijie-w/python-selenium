# coding=utf-8 
"""
@Time    : 2019/09/01  下午 15:36
@Author  : Allen
@FileName: sendEmail.py
@IDE     : PyCharm
"""

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import smtplib
import configparser
from common import readPath
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from report.newReport import new_report

username = '921519025@qq.com'
password = "whjzll0702"
sender = username
receivers = ','.join(['791098673@qq.com'])


def send_email(file_new):
    """
    定义发送邮件
    :param file_new:
    :return: 成功：打印发送邮箱成功；失败：返回失败信息
    """
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    # 发送附件
    con = configparser.ConfigParser()
    con.read(readPath.CONFIG_DIR,encoding='utf-8')
    report = new_report(readPath.TEST_REPORT)
    sendfile = open(report,'rb').read()

    # --------- 读取config.ini配置文件 ---------------
    HOST = con.get("Email_config","HOST_SERVER")
    SENDER = con.get("Email_config","FROM")
    RECEIVER = con.get("Email_config","TO")
    USER = con.get("Email_config","user")
    PWD = con.get("Email_config","password")
    SUBJECT = con.get("Email_config","SUBJECT")

    att = MIMEText(sendfile,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))

    msg = MIMEMultipart('related')
    msg.attach(att)
    msgtext = MIMEText(mail_body,'html','utf-8')
    msg.attach(msgtext)
    msg['Subject'] = SUBJECT
    msg['from'] = SENDER
    msg['to'] = RECEIVER

    try:
        server = smtplib.SMTP()
        server.connect(HOST)
        server.starttls()
        server.login(USER,PWD)
        server.sendmail(SENDER,RECEIVER,msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as  e:
        print("失败: " + str(e))

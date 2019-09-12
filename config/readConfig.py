# -*- coding:utf-8 -*-
"""
@Time    : 2019-09-01 14:03
@Author  : Allen
@FileName: readConfig.py
@IDE     : PyCharm
"""
import configparser
import os
from common import readPath

# 配置文件的路径
config_path = readPath.CONFIG_DIR
# flag = "local_constant"


class ReadConfig:
    def __init__(self):
        # 创建configparser对象实例
        self.cf = configparser.ConfigParser()
        # 一启动就读取配置文件
        self.cf.read(config_path, encoding='gbk')

    def get_email(self, name):
        value = self.cf.get("Email_config", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_http(self, name):
        value = self.cf.get("local_constant", name)
        return value


if __name__ == "__main__":
    url = ReadConfig()
    print(url.get_http('login_testUrl'))

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
        self.cf = configparser.ConfigParser()      # 创建configparser对象实例
        self.cf.read(config_path,encoding='gbk') # 一启动就读取配置文件
    def getConfig(self,flag,name):
        value = self.cf.get(flag,name)
        return value

if __name__ == "__main__":
    url = ReadConfig()
    print(url.getConfig("local_constant","phone"))

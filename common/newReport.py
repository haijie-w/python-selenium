# -*- coding:utf-8 -*- 
"""
@Time    : 2019-09-05 22:47
@Author  : Allen
@FileName: newReport.py
@IDE     : PyCharm
""" 
import  os
from common import readPath


def new_report(testReport):
    """
    生成最新的测试报告文件,包括HTML文件，TXT文件和PNG截图
    :param testReport:
    :return:返回文件
    """
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn: os.path.getmtime(testReport + "\\" + fn))
    file_new = os.path.join(testReport,lists[-1])
    # print(file_new)
    return file_new

# new_report(readPath.LOG_DIR)
# print(readPath.LOG_DIR)
# -*- coding:utf-8 -*- 
"""
@Time    : 2019-09-05 22:47
@Author  : Allen
@FileName: newReport.py
@IDE     : PyCharm
""" 
import  os

def new_report(testReport):
    """
    生成最新的测试报告文件
    :param testReport:
    :return:返回文件
    """
    lists = os.listdir(testReport)
    lists.sort(key=lambda fn: os.path.getmtime(testReport + "\\" + fn))
    file_new = os.path.join(testReport,lists[-1])
    return file_new
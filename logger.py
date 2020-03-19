#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 19:08
# @Author : whj

import logging
import time
import os
from common import readPath

log_path = readPath.LOG_DIR
# 日志存放文件夹，如不存在，则自动创建一个log目录
if not os.path.exists(readPath.LOG_DIR): os.mkdir(readPath.LOG_DIR)


class Log():
    """
    日志记录类
    """

    def __init__(self):

        # 文件的命名
        self.logName = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))

        # 初始化log
        self.logger = logging.getLogger()
        # 设置level
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    # 截图方法
    # def screenShot(self):
    #     dirname = os.path.join(root_dir, "img")
    #     now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    #     pic = now + ".png"
    #     path = dirname + "/" + pic
    #     im.save(path)
    #     Logger.mylogger("截图为：" + pic)
    #     pics.append(pic)

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地，默认是a参数
        fh = logging.FileHandler(self.logName, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    log = Log()
    log.info("---测试开始----")
    log.info("操作步骤1,2,3")
    log.warning("----测试结束----")


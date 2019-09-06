#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 19:08
# @Author : whj

import logging
import time
import os
from getRootPath import root_dir
<<<<<<< HEAD
log_path = os.path.join(root_dir, "log")

=======

log_path = os.path.join(root_dir, "log")


>>>>>>> 19bd2ada04e443ddcac660f54ddae6e4f6cb1c3a
class Log():
    @classmethod
    def __init__(cls):

        # 文件的命名
        cls.logName = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))

<<<<<<< HEAD
        #初始化log
        cls.logger = logging.getLogger()
        #设置level
=======
        # 初始化log
        cls.logger = logging.getLogger()
        # 设置level
>>>>>>> 19bd2ada04e443ddcac660f54ddae6e4f6cb1c3a
        cls.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        cls.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    # 截图方法
    # @classmethod
    # def screenShot(cls):
    #     dirname = os.path.join(root_dir, "img")
    #     now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    #     pic = now + ".png"
    #     path = dirname + "/" + pic
    #     im.save(path)
    #     Logger.mylogger("截图为：" + pic)
    #     pics.append(pic)

    @classmethod
    def __console(cls, level, message):
        # 创建一个FileHandler，用于写到本地，默认是a参数
        fh = logging.FileHandler(cls.logName, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(cls.formatter)
        cls.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(cls.formatter)
        cls.logger.addHandler(ch)

        if level == 'info':
            cls.logger.info(message)
        elif level == 'debug':
            cls.logger.debug(message)
        elif level == 'warning':
            cls.logger.warning(message)
        elif level == 'error':
            cls.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        cls.logger.removeHandler(ch)
        cls.logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()
<<<<<<< HEAD
    @classmethod
    def debug(cls, message):
        cls.__console('debug', message)
    @classmethod
    def info(cls, message):
        cls.__console('info', message)
    @classmethod
    def warning(cls, message):
        cls.__console('warning', message)
=======

    @classmethod
    def debug(cls, message):
        cls.__console('debug', message)

    @classmethod
    def info(cls, message):
        cls.__console('info', message)

    @classmethod
    def warning(cls, message):
        cls.__console('warning', message)

>>>>>>> 19bd2ada04e443ddcac660f54ddae6e4f6cb1c3a
    @classmethod
    def error(cls, message):
        cls.__console('error', message)


if __name__ == "__main__":
    log = Log()
    log.info("---测试开始----")
    log.info("操作步骤1,2,3")
<<<<<<< HEAD
    log.warning("----测试结束----")
=======
    log.warning("----测试结束----")
>>>>>>> 19bd2ada04e443ddcac660f54ddae6e4f6cb1c3a

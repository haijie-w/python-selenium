#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/19 13:08
# @Author : whj
import json
from common.logger import *


class GlobalMap():
    # 拼装成字典构造全局变量  借鉴map  包含变量的增删改查
    global map
    map = {}

    # def __init__(self):
    # self.log = Log()

    @staticmethod
    def set_map(key, value):
        if (isinstance(value, dict)):
            value = json.dumps(value)
        map[key] = value

    @staticmethod
    def set(**keys):
        try:
            for key_, value_ in keys.items():
                map[key_] = str(value_)  # self.log.debug(key_+":"+str(value_))
        except BaseException as msg:
            # self.log.error(msg)
            raise msg

    @staticmethod
    def del_map(self, key):
        try:
            del self.map[key]
            return self.map
        except KeyError:
            # self.log.error("key:'" + str(key) + "'  不存在")
            print("hhhhhh")

    @staticmethod
    def get(*args):
        try:
            dic = {}
            for key in args:
                if len(args) == 1:
                    dic = map[key]  # log.debug(key+":"+str(dic))
                elif len(args) == 1 and args[0] == 'all':
                    dic = map
                else:
                    dic[key] = map[key]
            return dic
        except KeyError:
            # self.log.warning("key:'" + str(key) + "'  不存在")
            return 'Null'


def test():
    a = GlobalMap()
    a.set_map(1, 2)
    # x = a.set()
    # print(x)
    a.set_map(1, 3)
    b = a.get(1)

    print(b)


if __name__ == "__main__":
    test()

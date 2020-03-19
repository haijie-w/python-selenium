#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/19 13:08
# @Author : whj
import json
from common.logger import *

class GlobalMap():
    # 拼装成字典构造全局变量  借鉴map  包含变量的增删改查
    map = {}
    # def __init__(self):
        # self.log = Log()

    def set_map(self, key, value):
        if(isinstance(value,dict)):
            value = json.dumps(value)
        self.map[key] = value

    def set(self, **keys):
        try:
            for key_, value_ in keys.items():
                self.map[key_] = str(value_)
                # self.log.debug(key_+":"+str(value_))
        except BaseException as msg:
            # self.log.error(msg)
            raise msg

    def del_map(self, key):
        try:
            del self.map[key]
            return self.map
        except KeyError:
            # self.log.error("key:'" + str(key) + "'  不存在")
            print("hhhhhh")

    def get(self,*args):
        try:
            dic = {}
            for key in args:
                if len(args)==1:
                    dic = self.map[key]
                    # log.debug(key+":"+str(dic))
                elif len(args)==1 and args[0]=='all':
                    dic = self.map
                else:
                    dic[key]=self.map[key]
            return dic
        except KeyError:
            # self.log.warning("key:'" + str(key) + "'  不存在")
            return 'Null'

def test():
    a = GlobalMap()
    a.set_map(1,2)
    b = a.get(1)
    print(b)

if __name__ == "__main__":
    test()
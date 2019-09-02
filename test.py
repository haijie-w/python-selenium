#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/13 15:17
# @Author : whj
import os,sys
import time
import random
from dateutil.parser import parse
now = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print(now + '登录成功')
print(now)
print(str(now) + '登录成功')
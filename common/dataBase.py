#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/9/12 15:49
# @Author : whj
# coning = utf-8

import pymysql
import config.readConfig as conf
from common import logger
import json

host = conf.ReadConfig().get_db('host')
user = conf.ReadConfig().get_db('username')
password = conf.ReadConfig().get_db('password')
port = conf.ReadConfig().get_db('port')
db = conf.ReadConfig().get_db('database')
log = logger.Log()


class DB():
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=str(host), user=user, port=int(port), password=password, database=db,
                                        charset='utf8')
        except Exception as e:
            log.error("数据库连接错误：出错是:%s" % e)

    # 查询第一个数据
    def select_one(self, sql):
        cusor = self.conn.cursor()
        cusor.execute(sql)
        result = cusor.fetchone()
        return json.dumps(result)

    # 查询所有数据
    def select_all(self, sql):
        cusor = self.conn.cursor()
        cusor.execute(sql)
        result = cusor.fetchall()
        return json.dumps(result)

    # 删除数据,修改，插入
    def delete(self, sql):
        cusor = self.conn.cursor()
        try:
            log.info('执行sql语句')
            cusor.execute(sql)
            self.conn.commit()
        except Exception as e:
            log.error("执行sql错误回滚：出错原因是：%s" % e)
            self.conn.rollback()

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    x = DB()
    z1 = "SELECT registration_ip FROM star_user LIMIT 20;"

    y1 = x.select_all(z1)
    print(y1)

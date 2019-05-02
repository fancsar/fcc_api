# -*- coding: utf-8 -*-
# @Time   : 2019/4/2120:58
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :do_mysql.py
import pymysql
from API_03.common.do_config import config


class DoMysql:
    '''
    完成与Mysql数据库的一个交互
    '''

    # 初始化连接数据库
    def __init__(self):
        host = config.get_str('db', 'host')
        user = config.get_str('db', 'user')
        password = config.get_str('db', 'password')
        port = config.get_int('db', 'port')
        # print(host)
        # print(user)
        # print(password)
        # print(port)
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        # 新建查询（游标）
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 建立字典游标
        # self.cursor=self.mysql.cursor()

    def fetch_one(self, sql):
        # 执行sql
        self.cursor.execute(sql)
        #执行SQL后进行提交
        self.mysql.commit()
        # 查询结果
        return self.cursor.fetchone()

    def fetch_all(self, sql):
        # 执行sql
        self.cursor.execute(sql)
        # 查询结果，类型为元组类型
        return self.cursor.fetchall()

    def close(self):
        # 关闭查询
        self.cursor.close()
        # 关闭SQL
        self.mysql.close()


if __name__ == '__main__':
    mysql = DoMysql()
    result = mysql.fetch_one('SELECT max(MobilePhone) FROM future.member')
    print(result[0])
    mysql.close()

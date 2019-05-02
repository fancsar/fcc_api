# -*- coding: utf-8 -*-
# @Time   : 2019/4/2221:04
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :test_add.py
import unittest

from ddt import ddt, data

from API_03.common.do_Excel import DoExcel
from API_03.common.do_HTTPrequ import HTTPrequest
from API_03.common.do_contants import case_files
from API_03.common.do_mysql import DoMysql
from API_03.common.do_config import config
from API_03.common.context import replace
from API_03.common.do_logging import GetLogger
loggor=GetLogger(__name__)
@ddt
class AddTest(unittest.TestCase):
    # 写到类属性中
    doexcel = DoExcel(case_files, 'Add')
    cases = doexcel.get_case()

    # 转换为类方法，即不用创建对象
    @classmethod  # 用classmethod 装饰类，运行类时启动一次,用一个http请求保存session
    def setUpClass(cls):
        loggor.info('准备测试前置')
        # 创建http请求对象session
        cls.http_request = HTTPrequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_add(self, case):
        loggor.info('开始测试:{}'.format(case.title))
        case.data = replace(case.data)
        #print(case.data)
        sql = 'select count(*) as num from future.loan where memberid = 1204'
        before = self.mysql.fetch_one(sql)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(actual_code, str(case.excepted))
            self.doexcel.write_case(case.case_id + 1, resp.text, 'PASS')
            if resp.json()['msg'] == '加标成功':
                after = self.mysql.fetch_one(sql)
                self.assertEqual(before['num'] + 1, after['num'])

        except AssertionError as e:
            self.doexcel.write_case(case.case_id + 1, resp.text, 'FAIL')
            loggor.info('测试出错:{}'.format(e))
            raise e
        loggor.info('测试结束:{}'.format(case.title))
    @classmethod  # 修饰为类方法时方法后加Class、
    def tearDownClass(cls):
        loggor.info('测试后置处理')
        # 关闭session
        cls.http_request.close()
        cls.mysql.close()

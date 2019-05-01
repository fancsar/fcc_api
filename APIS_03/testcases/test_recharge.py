# -*- coding: utf-8 -*-
# @Time   : 2019/4/2111:37
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :test_bidloan.py
import unittest
from ddt import ddt, data
from API_03.common.do_Excel import DoExcel
from API_03.common.do_HTTPrequ import HTTPrequest
from API_03.common.do_contants import case_files
from API_03.common.do_mysql import DoMysql
from API_03.common.do_logging import GetLogger

loggor = GetLogger(__name__)


@ddt
class RechargeTest(unittest.TestCase):
    doexcel = DoExcel(case_files, 'recharge')
    cases = doexcel.get_case()

    @classmethod
    def setUpClass(cls):
        loggor.info('准备测试前置')
        # 创建http请求对象session
        cls.http_request = HTTPrequest()
        # 创建数据库的连接
        cls.mysql = DoMysql()

    @data(*cases)
    def test_recharge(self, case):
        loggor.info('开始测试:{}'.format(case.title))
        # 在请求前查询金额
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            # 保存leaveamount之前的值
            before_v = member['leaveamount']
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(actual_code, str(case.excepted))
            self.doexcel.write_case(case.case_id + 1, resp.text, 'PASS')
            # 在请求后查询金额
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member['leaveamount'])
                after_v = member['leaveamount']
                # 要充值的钱为：
                amount = int(eval(case.data)['amount'])
                # 对充值前后的数值进行校验
                self.assertEqual(after_v, before_v + amount)
        except AssertionError as e:
            self.doexcel.write_case(case.case_id + 1, resp.text, 'FAIL')
            loggor.info('测试出错:{}'.format(e))
            raise e
        loggor.info('测试结束:{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        loggor.info('测试后置处理')
        # 关闭session
        cls.http_request.close()
        # 关闭SQL
        cls.mysql.close()

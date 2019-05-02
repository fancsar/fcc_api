# -*- coding: utf-8 -*-
# @Time   : 2019/4/2111:37
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :test_bidloan.py
from ddt import ddt, data
import unittest
from API_03.common.do_Excel import DoExcel
from API_03.common.do_HTTPrequ import HTTPrequest
from API_03.common.do_contants import case_files
from API_03.common.context import replace
from API_03.common.do_mysql import DoMysql
from API_03.common.context import Context
from API_03.common.do_logging import GetLogger
loggor=GetLogger(__name__)
@ddt
class BidloanTest(unittest.TestCase):
    # 写到类属性中
    doexcel = DoExcel(case_files, 'bidLoan')
    cases = doexcel.get_case()

    # 转换为类方法，即不用创建对象
    @classmethod  # 用classmethod 装饰类，运行类时启动一次,用一个http请求保存session
    def setUpClass(cls):
        loggor.info('准备测试前置')
        # 创建http请求对象session
        cls.http_request = HTTPrequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_bidloan(self, case):
        loggor.info('开始测试:{}'.format(case.title))
        case.data = replace(case.data)
        #loggor.debug('参数替换后的data:{}'.format(case.data))
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            # 充值前leaveamount的值
            before_v = member['leaveamount']
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(actual_code, str(case.excepted))
            self.doexcel.write_case(case.case_id + 1, resp.text, 'PASS')
            if resp.json()['msg'] == '加标成功':
                sql = 'select max(id) as max from future.loan where memberid = 1204'
                loan_id = self.mysql.fetch_one(sql)['max']
                print(loan_id)
                setattr(Context, 'loan_id', str(loan_id))
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member['leaveamount'])
                # 充值后leaveamount的值
                after_v = member['leaveamount']
                amount = int(eval(case.data)['amount'])
                self.assertEqual(before_v - amount, after_v)
        except AssertionError as e:
            self.doexcel.write_case(case.case_id + 1, resp.text, 'FAIL')
            loggor.info('测试报错:{}'.format(e))
            raise e
        loggor.info('测试结束:{}'.format(case.title))
    @classmethod  # 修饰为类方法时方法后加Class、
    def tearDownClass(cls):
        loggor.info('测试后置处理')
        # 关闭session
        cls.http_request.close()
        cls.mysql.close()

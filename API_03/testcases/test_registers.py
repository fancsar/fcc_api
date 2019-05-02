# -*- coding: utf-8 -*-
# @Time   : 2019/4/2122:34
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :test_registers.py
import unittest
from API_03.common.do_HTTPrequ import HTTPrequest
from API_03.common.do_Excel import DoExcel
from API_03.common.do_contants import case_files
from API_03.common.do_mysql import DoMysql
from ddt import ddt, data, unpack
from API_03.common.do_logging import GetLogger

loggor=GetLogger(__name__)
'''
参数化：在充值，投资，新增项目，审核时的前提为登录状态，所以将登录用户给参数化
新增项目时，会在loan表中生成一条数据，而接口参数时，可以将memberid与审核接口中的loanid参数化

'''


@ddt
class RegistersTest(unittest.TestCase):
    # 写到类属性中
    doexcel = DoExcel(case_files, 'register')
    cases = doexcel.get_case()

    # 转换为类方法，即不用创建对象
    @classmethod  # 用classmethod 装饰类，运行类时启动一次,用一个http请求保存session
    def setUpClass(cls):
        loggor.info('准备测试前置')
        # 创建http请求对象session
        cls.http_request = HTTPrequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_register(self, case):
        loggor.debug('开始测试:{}'.format(case.title))
        # 字符串的查找与替换,   查询数据库操作
        if case.data.find('register_mobile') > -1:
            sql = 'SELECT MobilePhone FROM future.member where MobilePhone=13821774377'
            # 查询手机号码，返回结果为字典
            max_phone = self.mysql.fetch_one(sql)
            max_phone = int(max_phone['MobilePhone']) + 1
            # 运用replace 对参数进行替换
            case.data = case.data.replace('register_mobile', str(max_phone))
            print(case.data)
            sql = 'SELECT count(*) as num FROM future.member'
            # 请求前的注册总数
            before = self.mysql.fetch_one(sql)
            print(before)
        resp = self.http_request.request(case.method, case.url, case.data)
        # actual_code = resp.json()['code']
        try:
            self.assertEqual(resp.text, case.excepted)
            self.doexcel.write_case(case.case_id + 1, resp.text, 'PASS')
            if resp.json()['msg'] == '注册成功':
                # 查询请求后注册总数
                after = self.mysql.fetch_one(sql)
                # 对注册总数进行校验
                self.assertEqual(before['num'] + 1, after['num'])
        except AssertionError as e:
            self.doexcel.write_case(case.case_id + 1, resp.text, 'FAIL')
            loggor.error('测试报错:{}'.format(e))
            raise e
        loggor.info('测试结束:{}'.format(case.title))
    @classmethod  # 修饰为类方法时方法后加Class、
    def tearDownClass(cls):
        loggor.info('测试后置处理')
        # 关闭session
        cls.http_request.close()
        cls.mysql.close()

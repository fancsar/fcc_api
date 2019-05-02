# -*- coding: utf-8 -*-
#@Time   : 2019/4/29 17:29
#@Author :xdf_FCC
#@Email  :670992243@qq.com
#@File   :run.py
import sys
sys.path.append('./')
print(sys.path)


import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from APIS_03.testcases import test_login,test_registers
from APIS_03.common.do_contants import report_dir
from APIS_03.common.do_contants import case_dir
#方法一：
# suite=unittest.TestSuite()
# loader=unittest.TestLoader()
# test1=loader.loadTestsFromModule(test_login)
# suite.addTest(test1)
#方法二：
#若多个模块都要进行输出报告时：参数解释：start_dir模块文件名路径, 正则表达式:pattern='test*.py', top_level_dir=None
discover=unittest.defaultTestLoader.discover(case_dir,'test*.py')

#stream指定输出文件
with open(report_dir+'/report.html','wb') as file:
    runner=HTMLTestRunner(stream=file,title='XDF_FCC',description='登陆接口',tester='樊成成')
    runner.run(discover)
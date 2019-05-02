# -*- coding: utf-8 -*-
#@Time   : 2019/4/1415:34
#@Author :lemon_FCC
#@Email  :670992243@qq.com
#@File   :contants.py 
#动态获取路径

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#bas_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#print(base_dir)
#print(bas_dir)
#case_file = os.path.join(base_dir,'API_test','http_case.xlsx')
case_file = os.path.join(base_dir,'data','cases.xlsx')
case_files = os.path.join(base_dir,'data','casess.xlsx')
#print(case_file)

global_file = os.path.join(base_dir,'config','global.ini')
#print(global_file)

online_file = os.path.join(base_dir,'config','online.cfg')
#print(online_file)

test_file = os.path.join(base_dir,'config','test.cfg')
#print(test_file)

# case_file = os.path.join(base_dir,'data','cases.xlsx')
# print(case_file)

fh_dir=os.path.join(base_dir,'log')

report_dir=os.path.join(base_dir,'reports')

case_dir=os.path.join(base_dir,'testcases')
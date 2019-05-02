# -*- coding: utf-8 -*-
# @Time   : 2019/4/2422:52
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :context.py
import configparser
import re
from API_03.common.do_config import config
'''
出现问题时，锁定出错那一行，
进行dubug调试
'''

class Context:
    loan_id = None


def replace(data):
    # 正则表达式
    zz = '#(.*?)#'
    # re.search(zz,data) 匹配到值时返回Match object ，若没有匹配到，则返回None
    while re.search(zz, data):
        # 找到第一个参数时返回的值cs
        cs = re.search(zz, data)
        # 找到正则匹配的值
        g = cs.group(1)
        # 通过配置文件查找配置文件中对应参数的值
        try:
            #在配置文件中取值
            value = config.get_str('member', g)
        except configparser.NoOptionError as e:
            #若配置文件中未取到值，在Context类中找参数
            if hasattr(Context, g):
                value = getattr(Context, g)
            else:
                print('没有找到参数信息')
                raise e
        print(value)
        # sub函数对参数化的值进行替换
        data = re.sub(zz, value, data, count=1)
    # 返回替换后的data值
    return data

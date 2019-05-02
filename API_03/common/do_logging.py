# -*- coding: utf-8 -*-
# @Time   : 2019/4/29 11:51
# @Author :xdf_FCC
# @Email  :670992243@qq.com
# @File   :do_logging.py
'''

'''
import logging
from API_03.common.do_contants import fh_dir
from API_03.common.do_config import config

#
# class GetLogger:
#     def __init__(self, name):
#
#         # 设置自己的日志收集器
#         self.my_log = logging.getLogger(name)
#
#     def get_loggor(self, level, msg):
#         self.my_log.setLevel('DEBUG')
#         # 设置日志的输出格式
#         fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s:  %(lineno)d"
#         # fmt="%(levelno)s-%(asctime)s-%(message)s"
#         myfmt = logging.Formatter(fmt)
#         # 将日志输出到控制台中
#         kh = logging.StreamHandler()
#         # 读取配置文件中等级
#         kh_level = config.get_str('level', 'lv_1')
#         kh.setLevel(kh_level)
#         kh.setFormatter(myfmt)
#         # 输出到文件中，考虑到资源的有效利用，输出级别为info
#         fh = logging.FileHandler(fh_dir + '\case.log',encoding='UTF-8',mode='a')
#         fh_level = config.get_str('level', 'lv_2')
#         fh.setLevel(fh_level)
#         fh.setFormatter(myfmt)
#         # 日志收集器与输出渠道进行对接
#         self.my_log.addHandler(kh)
#         self.my_log.addHandler(fh)
#
#         if level == 'DEBUG':
#             self.my_log.debug(msg)
#         elif level == 'INFO':
#             self.my_log.info(msg)
#         elif level == 'WARNING':
#             self.my_log.warning(msg)
#         elif level == 'ERROR':
#             self.my_log.error(msg)
#         else:
#             self.my_log.critical(msg)
#         self.my_log.removeHandler(kh)
#         self.my_log.removeHandler(fh)
#
#     def debug(self, msg):
#         return self.get_loggor('DEBUG', msg)
#
#     def info(self, msg):
#         return self.get_loggor('INFO', msg)
#
#     def warning(self, msg):
#         return self.get_loggor('WARNING', msg)
#
#     def error(self, msg):
#         return self.get_loggor('ERROR', msg)
#
#     def critical(self, msg):
#         return self.get_loggor('CRITICAL', msg)

#
#
# my_log = GetLogger(__name__)
# my_log.info('输出测试info')
# my_log.debug('输出测试debug')
# my_log.error('输出测试error')
# my_log.warning('输出测试warning')


def GetLogger(name):
    my_log = logging.getLogger(name)
    my_log.setLevel('DEBUG')
    # 设置日志的输出格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s:  %(lineno)d"
    # fmt="%(levelno)s-%(asctime)s-%(message)s"
    myfmt = logging.Formatter(fmt)
    # 将日志输出到控制台中
    kh = logging.StreamHandler()
    # 读取配置文件中等级
    kh_level = config.get_str('level', 'lv_1')
    kh.setLevel(kh_level)
    kh.setFormatter(myfmt)
    # 输出到文件中，考虑到资源的有效利用，输出级别为info
    fh = logging.FileHandler(fh_dir + '\case.log', encoding='UTF-8')
    fh_level = config.get_str('level', 'lv_2')
    fh.setLevel(fh_level)
    fh.setFormatter(myfmt)
    # 日志收集器与输出渠道进行对接
    my_log.addHandler(kh)
    my_log.addHandler(fh)
    return my_log

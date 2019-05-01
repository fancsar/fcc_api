# -*- coding: utf-8 -*-
#@Time   : 2019/4/2110:13
#@Author :lemon_FCC
#@Email  :670992243@qq.com
#@File   :do_config.py
#需要安装configparse 模块   pip install configparser
import configparser
from API_03.common.do_contants import global_file,online_file,test_file
class ReadConfig:
    '''
    完成配置文件的读取
    '''
    def __init__(self,encoding='UTF-8'):
        self.cf = configparser.ConfigParser()
        # 先加载global
        self.cf.read(global_file, encoding)
        switch = self.cf.getboolean('switch', 'on')
        if switch:
            # 开关打开时，使用online 线上环境
            self.cf.read(online_file, encoding)
        else:
            # 开关关闭时，使用test 测试环境
            self.cf.read(test_file, encoding)
    def get_str(self,section,option):
        #获取某一个section下面，某一个option具体的值,所有结果都是字符串
        return self.cf.get(section,option)
    def get_int(self,section,option):
        # 获取int类型的数据
        return self.cf.getint(section,option)
    def get_float(self,section,option):
        # 获取float类型的数据
        return self.cf.getfloat(section,option)
    def get_boolean(self,section,option):
        # 获取布尔类型的数据
        return self.cf.getboolean(section, option)
    def get_section(self):
        # 获取conf配置文件下所有section
        return self.cf.sections()
    def get_option(self,section):
        # 获取section下面所有的option(选项)
        return self.cf.options(section)
    def get_eval(self,section,option):
        # 获取字典、元组、列表等数据
        return eval(self.cf.get(section,option))

#实例化配置对象，调用时直接调用对象
config = ReadConfig()
if __name__ == '__main__':
    a=config.get_section()
    print(a)
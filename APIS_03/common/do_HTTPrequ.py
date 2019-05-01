# -*- coding: utf-8 -*-
# @Time   : 2019/4/1314:03
# @Author :lemon_FCC
# @Email  :670992243@qq.com
# @File   :do_HTTPrequ.py
import requests
from API_03.common.do_config import config
from API_03.common.do_logging import GetLogger

loggor = GetLogger(__name__)


class HTTPrequest:  # 使用session 不用cookies
    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()
        url = config.get_str('api', 'pro_url') + url  # 与配置文件结合，拼接路径
        # print(url)
        loggor.debug('请求的url:{}'.format(url))
        loggor.debug('请求的data:{}'.format(data))
        if type(data) == str:
            data = eval(data)  # 将传的字典数据还原
        if method == 'GET':
            resp = self.session.request(method='get', url=url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method='post', url=url, json=json)
            else:
                resp = self.session.request(method='post', url=url, data=data)
        else:
            loggor.error('UN support this method')
            # print('UN support this method')
        # print('请求响应文本',resp.text)
        loggor.debug('请求响应文本:{}'.format(resp.text))
        return resp

    def close(self):  # 关闭session
        self.session.close()

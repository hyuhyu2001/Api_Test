#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
配置文件
"""

import requests
import json as j
from public import Config

class MyHTTP(object):
    def __init__(self):
        self.url = Config.url()

    def get_url(self,endpoint):
        url = '/'.join([self.url,endpoint])
        return url

    def get(self, url, **params):
        '''封装HTTP GET请求方法'''
        try:
            response = requests.get(url, params=params, timeout=3)
            text = j.loads(response.text)  # 由unicode转换为dict格式 也可以用response.json()直接生成dict格式
            return text
        except Exception as e:
            print('get错误：%s' % e)
            return {}

    def post(self,url,**DataAll):
        headers = DataAll.get('headers')
        data = DataAll.get('data')
        json = DataAll.get('json')
        files = DataAll.get('files')
        try:
            response = requests.post(url=url,headers=headers,data=data,json=json,files=files,timeout=3)
            text = j.loads(response.text)
            return text
        except Exception as e:
            print('post错误：%s' % e)
            return {}


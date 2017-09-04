#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
配置文件
"""

import sys
import requests
import json as j
sys.path.append('./public')
from public import Config
from public import read_excel

class MyHTTP(object):
    def __init__(self):
        self.url = Config.url()

    def get_url(self,endpoint):
        url = '/'.join([self.url,endpoint])
        return url

    def get(self, url,*args, **DataAll):
        '''封装HTTP GET请求方法'''
        headers = DataAll.get('headers')
        params = DataAll.get('params')
        #把从excel中获取的值存入对应的字段
        if len(args)>0:
            read_excel.save_data(args,params=params)
        try:
            response = requests.get(url,headers=headers,params=params, timeout=3)
            text = j.loads(response.text)  # 由unicode转换为dict格式 也可以用response.json()直接生成dict格式
            return text
        except Exception as e:
            print('get错误：%s' % e)
            return {}

    def post(self,url,*args,**DataAll):
        params = DataAll.get('params')
        headers = DataAll.get('headers')
        data = DataAll.get('data')
        json = DataAll.get('json')
        files = DataAll.get('files')
        if len(args)>0:
            json=read_excel.save_data(args,params=params,data=data,json=json,files=files)
        try:
            response = requests.post(url=url,params=params,headers=headers,data=data,json=json,files=files,timeout=3)
            text = j.loads(response.text)
            return text
        except Exception as e:
            print('post错误：%s' % e)
            return {}

    def delete(self, url,*args,**DataAll):
        '''封装HTTP delete请求方法'''
        headers = DataAll.get('headers')
        params = DataAll.get('params')
        if len(args)>0:
            read_excel.save_data(args,params=params)
        try:
            response = requests.delete(url,headers=headers,params=params, timeout=3)
            text = j.loads(response.text)  # 由unicode转换为dict格式 也可以用response.json()直接生成dict格式
            return text
        except Exception as e:
            print('get错误：%s' % e)
            return {}
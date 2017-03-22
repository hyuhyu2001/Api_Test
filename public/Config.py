#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
配置文件

从ini文件里读取信息
import configparser
config = configparser.ConfigParser()
# 从配置文件中读取数据库服务器IP、域名，端口
config.read(config_file, encoding='utf-8')
self.host = config[db]['host']
self.port = config[db]['port']
self.user = config[db]['user']
self.passwd = config[db]['passwd']
self.db_name = config[db]['db']
self.charset = config[db]['charset']
"""


def url():
    Environment = 'test'
    if Environment == 'test':  #测试环境
        url = 'http://apitest.00bang.net:8081'
    elif Environment == 'pre':  #预发布环境
        url = 'https://apipre.00bang.net'
    elif Environment == 'release':  #正式环境
        url = 'https://api.00bang.net'
    return url





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
        # url = 'http://apitest.00bang.net:8081'
        url = 'http://apitest2.00bang.net'
        # url = 'http://apidev.00bang.net/'
    elif Environment == 'pre':  #预发布环境
        url = 'https://apipre.00bang.net'
    elif Environment == 'release':  #正式环境
        url = 'https://api.00bang.net'
    return url

#测试环境数据库连接串
sql_conn_dict = {
    'host': '114.215.107.77',
    'user':'cloudyoung',
    'passwd':'cy@5408',
    'port':5408,
    'db':'llb_ucenter_test',
    'charset':'utf8'
}
'''
#正式环境数据库连接串
sql_conn_dict = {
    'host': 'wappdb008.mysql.rds.aliyuncs.com',
    'user':'llb_db',
    'passwd':'lLb_PwDa',
    'port':3306,
    'db':'llb_ucenter',
    'charset':'utf8'
}
'''



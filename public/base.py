#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
"""
import requests
import base64
import hashlib
from public import HttpService
from public import SqlService
from public import read_excel
import json


def test_account_getRegisterSmsCode(mobile):
    '''获取短信验证码'''
    url = HttpService.MyHTTP().get_url('account/getRegisterSmsCode')
    params = {'mobile': mobile}
    r = requests.get(url, params=params)
    sql = 'SELECT captcha FROM llb_message_test.captcha WHERE mobile=mobile ORDER BY captcha_time DESC LIMIT 1' #llb_message_test
    DB = SqlService.MyDB()
    result = DB.execute_select_one(sql)
    DB.close()
    return result


def userlogin(mobile,password):
    '''登陆账号并获取token'''
    url = HttpService.MyHTTP().get_url('account/userLogin')
    params = {'mobile': mobile, 'password':password}
    DataAll = { 'params': params}
    text = HttpService.MyHTTP().get(url, **DataAll)
    token = text.get(u'data').get(u'token')
    return token

def userLogout(token):
    '''用户注销'''
    url = HttpService.MyHTTP().get_url('/account/userLogout')

    headers= {'token': token}
    DataAll = {'headers':headers}
    text = HttpService.MyHTTP().post(url,**DataAll)

    result = text.get(u'result')
    return result

def bs64(s):
    #base64加密
    bstr=base64.b64encode(s.encode(encoding='utf-8'))
    dstr=bstr.decode()
    return dstr

def md5(s):
    m = hashlib.md5()
    m.update(s.encode(encoding="utf-8"))
    return m.hexdigest()

def get_response(url,RequestMethod,*args,**DataAll):
    RequestMethod = RequestMethod.lower()
    if RequestMethod == 'get':
        text = HttpService.MyHTTP().get(url,*args ,**DataAll)
    elif RequestMethod == 'post':
        text = HttpService.MyHTTP().post(url,*args, **DataAll)
    elif RequestMethod == 'delete':
        text = HttpService.MyHTTP().delete(url,*args,**DataAll)
    return text

def get_url(EndPoint):
    url = HttpService.MyHTTP().get_url(EndPoint)
    return url

def get_data(testfile,sheetname):
    datainfo = read_excel.XLDataInfo( r'D:\python_pycharmWorkspace\python36\Api_Test\test_data\%s'%testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data
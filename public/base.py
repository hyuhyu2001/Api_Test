#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:
"""
import requests
from public import HttpService
from public import SqlService
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

    text = HttpService.MyHTTP().get(url, **params)
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

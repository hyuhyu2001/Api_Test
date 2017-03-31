#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
接口分类：个人中心HTTP接口
接口名称：用户登录
接口类型：http
请求地址：rootUrl/account/userLogin
请求方式：POST GET
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService

class TestAccountLogin(unittest.TestCase):
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('account/userLogin')

    def test_account_Login(self):
        '''校验状态是否登陆成功'''
        params = { 'mobile': '15210110149','password': '123456'}
        text = HttpService.MyHTTP().get(self.url, **params)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_account_Login_mobile(self):
        '''校验手机号为空'''
        params = { 'mobile': '','password': '123456'}
        text = HttpService.MyHTTP().get(self.url, **params)

        errorMessage = text.get(u'errorMessage')
        self.assertEqual(errorMessage,u'手机号不能为空!') #需要加U

    def test_account_Login_password_01(self):
        '''校验密码为空'''
        params = {'mobile': '15210110149','password': ''}
        text = HttpService.MyHTTP().get(self.url, **params)

        errorMessage = text.get(u'errorMessage')
        self.assertEqual(errorMessage,u'密码不能为空!')

    def test_account_Login_password_02(self):
        '''校验密码错误'''
        params = {'mobile': '15210110149','password': '12dasd3'}
        text = HttpService.MyHTTP().get(self.url, **params)

        errorMessage = text.get(u'errorMessage')
        self.assertEqual(errorMessage,u'密码错误!')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()

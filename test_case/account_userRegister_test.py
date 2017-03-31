#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
接口分类：个人中心HTTP接口
接口名称：用户注册
接口类型：http
请求地址：rootUrl/account/userRegister
请求方式：POST GET
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import SqlService
from public import base


class TestAccountUserRegister(unittest.TestCase):
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('account/userRegister')

    def test_account_UserRegister_mobile(self):
        '''手机号不能为空'''
        mobile = ''
        smsCode = base.test_account_getRegisterSmsCode(mobile)

        data = {'mobile': mobile, 'password': '123456', 'smsCode': smsCode, 'nickname': '9875475昵称', 'carTypeId': '1','cityId': '18', 'sex': '1', 'birthdayStr': '1989-11-01', 'photo': 'T1oaDTBQLT1RCvBVdK.png'}
        DataAll = {'data':data}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        errorMessage = text.get(u'errorMessage')
        self.assertEqual(errorMessage, u'手机号不能为空!')

    def test_account_UserRegister(self):
        '''正常注册'''
        mobile = '15819875475'
        smsCode = base.test_account_getRegisterSmsCode(mobile)

        data = {'mobile':mobile, 'password': '123456', 'smsCode':smsCode, 'nickname': '9875475昵称', 'carTypeId': '1', 'cityId': '18','sex':'1','birthdayStr':'1989-11-01','photo':'T1oaDTBQLT1RCvBVdK.png'}
        DataAll = {'data':data}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)


    def tearDown(self):
        sql = "DELETE FROM llb_ucenter_test.user WHERE mobile = '15819875475'"
        DB = SqlService.MyDB()
        DB.execute_delete(sql)
        DB.close()

if __name__ == "__main__":
    unittest.main()

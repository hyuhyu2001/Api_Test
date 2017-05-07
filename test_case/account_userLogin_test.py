#!/usr/bin/env python
"""
@author:     jinzj
@desc:
接口分类：个人中心HTTP接口
接口名称：用户登录
接口类型：http
请求地址：rootUrl/account/userLogin
请求方式：POST GET
增加数据驱动框架ddt
"""

import unittest
import sys
from ddt import ddt,data,unpack
sys.path.append('./public')
from public import base

testcasefile = 'account_userLogin_test_data.xlsx'
AllData = base.get_data(testcasefile, 'AllData')
TestDatainfo = base.get_data(testcasefile, 'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
RequestData = AllData[1][3]
TestData = tuple(TestDatainfo[1:])

@ddt
class AccountUserLogin(unittest.TestCase):
    '''登陆测试'''
    def setUp(self):
        self.url = base.get_url(EndPoint)

    @data(*TestData)
    @unpack
    def test_account_Login(self,mobile,password,expectedresult):
        DataAll = eval(RequestData)
        text = base.get_response(self.url,RequestMethod,**DataAll)

        if expectedresult.lower() == 'true':
            result = text.get('result')
            self.assertEqual(result,True)
        else:
            errorMessage = text.get(u'errorMessage')
            self.assertEqual(errorMessage, expectedresult)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()


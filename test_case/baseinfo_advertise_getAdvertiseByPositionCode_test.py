#!/usr/bin/env python
"""
@author:     jinzj
@desc:
接口分类：广告
接口名称：获取广告位编码对应的广告列表
请求方式：GET
"""

import unittest
import sys
from ddt import ddt,data,unpack
sys.path.append('./public')
from public import base

testcasefile = 'baseinfo_advertise_getAdvertiseByPositionCode_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestDatainfo = base.get_data(testcasefile,'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
RequestData = AllData[1][3]
TestData = tuple(TestDatainfo[1:])

@ddt
class BaseinfoAdvertiseGetAdvertiseByPositionCode(unittest.TestCase):
    '''获取广告位编码对应的广告列表'''
    def setUp(self):
        self.url = base.get_url(EndPoint)
        self.token = base.userlogin('15210110149','123456')

    @data(*TestData)
    @unpack
    def test_baseinfo_advertise_getAdvertiseByPositionCode(self,token,positionCode,expectedresult):
        if token == 'token':
            token = self.token
        DataAll = eval(RequestData)
        text = base.get_response(self.url,RequestMethod,**DataAll)

        if expectedresult.lower() == 'true':
            result = text.get('result')
            self.assertEqual(result,True)
        else:
            errorMessage = text.get(u'errorMessage')
            self.assertEqual(errorMessage, expectedresult)

    def tearDown(self):
        base.userLogout(self.token)

if __name__ == "__main__":
    unittest.main()
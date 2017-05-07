#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:  unittest的父类
"""

import unittest
import sys
from ddt import ddt,data,unpack
sys.path.append('./public')
from public import base

testcasefile = 'baseinfo_advertise_getAdvertiseByPageCode_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestDatainfo = base.get_data(testcasefile,'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
RequestData = AllData[1][3]
TestData = tuple(TestDatainfo[1:])

@ddt
class BaseUnittest(unittest.TestCase):
    '''Base类'''
    def setUp(self):
        self.url = base.get_url(EndPoint)
        self.token = base.userlogin('15210110149','123456')

    @data(*TestData)
    @unpack
    def test_base_unittest(self,expectedresult):
        DataAll = eval(RequestData)
        text = base.get_response(self.url,RequestMethod,**DataAll)
        print(text)

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
#!/usr/bin/env python
"""
@author:     jinzj
@desc:
接口分类：个人中心HTTP接口
接口名称：提问技师标签接口
请求方式：POST GET
"""

import unittest
import sys
from ddt import ddt,data,unpack
sys.path.append('./public')
from public import HttpService
from public import base

class CommunityPostTechPostLabels(unittest.TestCase):
    '''提问技师问题标签'''
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('community/post/techPostLabels')
        self.token = base.userlogin('15210110149','123456')

    def test_community_postlist_techPostLabels(self):
        headers = {'token':self.token}
        params={'labelType':1,'pageNo':'1','pageSize':'5'}
        DataAll = {'headers':headers,'params': params}
        text = HttpService.MyHTTP().post(self.url, **DataAll)
        print(text)
        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        base.userLogout(self.token)

if __name__ == "__main__":
    unittest.main()
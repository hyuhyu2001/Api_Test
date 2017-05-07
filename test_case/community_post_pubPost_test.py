#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
接口分类：个人中心HTTP接口
接口名称：发布帖子
接口类型：http
请求地址：rootUrl/community/post/pubPost
请求方式：POST
"""

import unittest
import sys
from ddt import ddt,data,unpack
sys.path.append('./public')
from public import base

testcasefile = 'community_post_pubPost_test_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestDatainfo = base.get_data(testcasefile,'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
RequestData = AllData[1][3]
TestData = tuple(TestDatainfo[1:])


@ddt
class CommunityPostPubPost(unittest.TestCase):
    '''发布帖子'''
    def setUp(self):
        self.url = base.get_url(EndPoint)
        self.token = base.userlogin('15210110149','123456')

    @data(*TestData)
    @unpack
    def test_post_pubPost(self,token,deviceType,platformNo,channelId,imgTexts,postTypeId,rewardTypeId,carTypeId,postLabelId,expectedresult):
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
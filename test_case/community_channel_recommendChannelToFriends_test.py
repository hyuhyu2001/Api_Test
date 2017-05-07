#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:向好友推荐社区接口
"""
import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class CommunityChannelRecommendChannelToFriends(unittest.TestCase):
    '''向好友推荐社区'''
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('community/channel/recommendChannelToFriends')
        self.token = base.userlogin('15210110149', '123456')
        userId = base.bs64('1023886')
        self.mobileslist = [userId]

    def test_recommend_channel_tofriends(self):
        '''向好友推荐社区成功'''
        headers = {'token': self.token}
        params = {'channelId':306}
        json = self.mobileslist
        DataAll = {'params': params,'headers': headers,'json':json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
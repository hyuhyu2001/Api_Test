#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc: 社区成员列表
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class CommunityChannelAttendedUsers(unittest.TestCase):
    def setUp(self):
        self.channelId = 306
        self.url = HttpService.MyHTTP().get_url('community/channel/attendedUsers/%s'%self.channelId)
        self.token = base.userlogin('15210110149', '123456')

    def test_attended_users_token(self):
        '''有token，有分页'''
        headers = {'token': self.token}
        params = {'pageSize': 2, 'pageNo': 2}
        DataAll = {'headers': headers, 'params': params}
        text = HttpService.MyHTTP().get(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_attended_users_notoken(self):
        '''无token，无分页'''
        headers = {'token': ''}
        DataAll = {'headers': headers}
        text = HttpService.MyHTTP().get(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result, True)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
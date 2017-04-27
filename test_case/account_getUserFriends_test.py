#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:查询好友列表
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class AccountGetUserFriends(unittest.TestCase):
    '''查询好友列表'''
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('account/getUserFriends')
        self.token = base.userlogin('15210110149', '123456')
        self.userId = base.bs64('1023886')

    def test_get_user_friends_own(self):
        '''查询自己用户好友列表'''
        headers = {'token': self.token}
        params = { 'pageNo': 1,'pageSize':5}
        DataAll = {'headers': headers, 'params': params}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_get_user_friends_other(self):
        '''查询他人用户好友列表'''
        headers = {'token': self.token}
        params = {'userIdStr': self.userId, 'pageNo': 1,'pageSize':5}
        DataAll = {'headers': headers, 'params': params}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
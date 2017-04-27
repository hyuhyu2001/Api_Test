#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:获取用户通讯录
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class AccountGetInvitedList(unittest.TestCase):
    '''获取用户通讯录测试'''
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('account/getInvitedList')
        self.token = base.userlogin('15210110149', '123456')
        m1=base.md5('15810293081')
        m2=base.md5('13312345678')
        self.mobileslist = [m1,m2]

    def test_get_InvitedList(self):
        '''成功获取通讯录好友'''
        headers = {'token': self.token}
        json = self.mobileslist
        DataAll = {'headers': headers, 'json': json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:社区用户举报
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class UgcComplaintComplaintUser(unittest.TestCase):
    '''社区用户举报'''
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('ugc/complaint/complaintUser')
        self.token = base.userlogin('15210110149', '123456')
        self.userId = base.bs64('1023886')

    def test_complaint_user(self):
        '''校验举报是否成功'''
        headers = {'token': self.token}
        params = {'userIdStr': self.userId, 'complaintsReason': 1}
        DataAll = {'headers': headers, 'params': params}
        text = HttpService.MyHTTP().get(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
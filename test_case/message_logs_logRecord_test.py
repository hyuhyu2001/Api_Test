#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:APP上传日志
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class MessageLogsLogRecord(unittest.TestCase):
    '''APP上传日志'''
    def setUp(self):
        self.settings=[{"LogId":734,"clientRecordDate":1486558077043,"logLevel":"error","logType":3,"requestParam":"","requestUrl":"https://api.00bang.net/community/post/columns","responseData":"code:502"}]
        self.url = HttpService.MyHTTP().get_url('message/logs/logRecord/')
        self.token = base.userlogin('15210110149', '123456')

    def test_log_record_token(self):
        '''有token，上传成功'''
        headers = {'deviceType':'ios','platformNo':'ios'}
        json ={'logStorageInfo':self.settings,'token': self.token}
        DataAll = {'headers': headers,'json':json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_log_record_notoken(self):
        '''无token，上传失败'''
        headers = {'deviceType': 'ios', 'platformNo': 'ios'}
        json = {'logStorageInfo':self.settings, 'token': ''}
        DataAll = {'headers': headers, 'json': json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_log_record_space(self):
        '''日志为空'''
        headers = {'deviceType': 'ios', 'platformNo': 'ios'}
        json = {'logStorageInfo': '', 'token':self.token}
        DataAll = {'headers': headers, 'json': json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get(u'errorMessage')
        self.assertEqual(result,u'没有有效日志数据')

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
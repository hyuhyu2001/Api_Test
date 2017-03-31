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
sys.path.append('./public')
from public import HttpService
from public import base

class TestAccountUserRegister(unittest.TestCase):
    def setUp(self):
        self.url = HttpService.MyHTTP().get_url('community/post/pubPost')
        self.token = base.userlogin('15210110149','123456')

    def test_post_pubPost(self):
        '''发图文帖成功'''
        headers={'token':self.token,
                 'deviceType':'android',
                 'platformNo':'Android'
                 }
        data = {'rewardTypeId':'1',
                'channelId': '306',
                'imgTexts':     [{"text": "超级便宜的衣服特卖了f000good"}, {"img": "T1tVKTB4bT1RCvBVdK.jpg", "width": "922", "height": "1280", "text": "大家快来看啦，顶顶顶"}],
                'postTypeId': '0' }
        DataAll = {'headers': headers,'json':data}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        print(result)
        self.assertEqual(result, True)

    def test_post_pubPost_token(self):
        '''token不能为空'''
        headers={'token':'',
                 'deviceType':'android',
                 'platformNo':'Android'
                 }
        data = {'rewardTypeId':'1',
                'channelId': '306',
                'imgTexts':     [{"text": "超级便宜的衣服特卖了f000good"}, {"img": "T1tVKTB4bT1RCvBVdK.jpg", "width": "922", "height": "1280", "text": "大家快来看啦，顶顶顶"}],
                'postTypeId': '0' }
        DataAll = {'headers': headers,'json':data}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get(u'errorMessage')
        self.assertEqual(result, u'token不能为空!')

    def tearDown(self):
        base.userLogout(self.token)

if __name__ == "__main__":
    unittest.main()
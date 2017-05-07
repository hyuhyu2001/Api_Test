#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:评论帖子
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import base

class UgcCommentCommentPost(unittest.TestCase):
    '''评论帖子'''
    def setUp(self):
        self.postId = 45271
        self.url = HttpService.MyHTTP().get_url('ugc/comment/commentPost/%s'%self.postId)
        self.token = base.userlogin('15210110149', '123456')

    def test_comment_post_token(self):
        '''有token，回复成功'''
        headers = {'token': self.token}
        json = {"commentContent":"yggvq","images":"T1OEKTBCDT1RCvBVdK.jpg","praiseCount":0,"isPraise":0,"accept":0}
        DataAll = {'headers': headers,'json':json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_comment_post_notoken(self):
        '''无token，回复不成功'''
        headers = {'token': ''}
        json = {"commentContent": "hhhjjh", "praiseCount": 0, "isPraise": 0, "accept": 0}
        DataAll = {'headers': headers, 'json': json}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get(u'errorMessage')
        self.assertEqual(result, u'token不能为空!')

    def tearDown(self):
        base.userLogout(self.token)

if __name__ == "__main__":
    unittest.main()
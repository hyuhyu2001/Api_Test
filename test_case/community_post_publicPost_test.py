#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:帖子公告
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import SqlService
from public import base

class CommunityPostPublicPost(unittest.TestCase):
    '''帖子公告'''
    def setUp(self):
        self.postId = 45280
        self.url = HttpService.MyHTTP().get_url('community/post/publicPost/%s'%self.postId)
        self.token = base.userlogin('15210110149', '123456')

    def test_public_post(self):
        '''帖子公告成功'''
        params = {'title':'公共贴'}
        headers = {'deviceType':'ios','platformNo':'ios','token': self.token}
        DataAll = {'params': params,'headers': headers}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        '''取消帖子公告'''
        sql1 = "UPDATE llb_community_test.post SET is_public=0 WHERE post_id=%s"%(self.postId)
        sql2 = "UPDATE llb_community_test.post_operate SET STATUS=0 WHERE opera_type=0 AND post_id=%s"%(self.postId)
        DB = SqlService.MyDB()
        DB.execute_update(sql1)
        DB.execute_update(sql2)
        DB.close()

if __name__ == "__main__":
    unittest.main()
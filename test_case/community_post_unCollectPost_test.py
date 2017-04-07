#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:取消收藏帖子
"""
import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import SqlService
from public import base

class CommunityPostUnCollectPost(unittest.TestCase):
    def setUp(self):
        self.postId = 45280
        self.url = HttpService.MyHTTP().get_url('community/post/unCollectPost/%s'%self.postId)
        self.token = base.userlogin('15210110149', '123456')

    def test_UnCollect_post(self):
        '''帖子取消收藏成功'''
        headers = {'token': self.token}
        DataAll = {'headers': headers}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        '''重新设置收藏insert'''
        sql = "insert into `llb_ugc_test`.`collection` (collection_target_id,operation_type_id,user_id,creation_date) values ('45280','4','1001757','2017-04-07 10:29:29')"
        DB = SqlService.MyDB()
        DB.execute_insert(sql)
        DB.close()

if __name__ == "__main__":
    unittest.main()
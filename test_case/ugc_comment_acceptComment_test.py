#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:技师问题，采纳回复
"""
import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import SqlService
from public import base

class UgcCommentAcceptComment(unittest.TestCase):
    def setUp(self):
        self.commentId = 212854
        self.commentTargetId = 45271
        self.url = HttpService.MyHTTP().get_url('ugc/comment/acceptComment/%s'%self.commentId)
        self.token = base.userlogin('15801006286', '123456')

    def test_comment_acceptcomment_token(self):
        '''有token，采纳回复成功'''
        headers = {'token': self.token}
        # params = {'commentTargetId':self.commentTargetId}
        DataAll = {'headers': headers}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def test_comment_acceptcomment_notoken(self):
        '''无token，采纳回复不成功'''
        headers = {'token': ''}
        params = {'commentTargetId':self.commentTargetId}
        DataAll = {'headers': headers,'params':params}
        text = HttpService.MyHTTP().post(self.url, **DataAll)

        result = text.get(u'errorMessage')
        self.assertEqual(result, u'token不能为空!')

    def tearDown(self):
        sql = "UPDATE llb_ugc_test.COMMENT SET accept = '0' WHERE comment_id = %s AND comment_target_id = %s"%(self.commentId,self.commentTargetId)
        DB = SqlService.MyDB()
        result = DB.execute_update(sql)
        DB.close()

if __name__ == "__main__":
    unittest.main()
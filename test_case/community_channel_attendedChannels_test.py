#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:退出社区接口
"""

import unittest
import sys
sys.path.append('./public')
from public import HttpService
from public import SqlService
from public import base

class CommunityChannelAttendedChannels(unittest.TestCase):
    def setUp(self):
        self.channelId = 306
        self.url = HttpService.MyHTTP().get_url('community/channel/attendedChannels/%s'%self.channelId)
        self.token = base.userlogin('15801006286', '123456')

    def test_channel_getattended_users(self):
        '''正常退出社区'''
        headers = {'token': self.token}
        DataAll = {'headers': headers}
        text = HttpService.MyHTTP().delete(self.url, **DataAll)

        result = text.get('result')
        self.assertEqual(result,True)

    def tearDown(self):
        '''重新加入社区'''
        sql = "insert into `llb_community_test`.`channel_join_record`  (channel_id,user_id,creation_date,channel_role_id) values ('306','1002800','2017-04-07 10:59:30','2')"
        DB = SqlService.MyDB()
        DB.execute_insert(sql)
        DB.close()

if __name__ == "__main__":
    unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""
import requests
import json
from public import HttpService
from public import base

'''
#get测试
url = HttpService.MyHTTP().get_url('account/userLogin')
params = {'mobile': '15210110149', 'password': '123456'}
text = HttpService.MyHTTP().get(url, **params)
print(text)
'''

#post测试
token = base.userlogin('15210110149', '123456')
url = HttpService.MyHTTP().get_url('/account/userLogout')
headers = {'token': token}
DataAll = {'headers': headers}
text = HttpService.MyHTTP().post(url, **DataAll)
print(text)

# url = HttpService.MyHTTP().get_url('community/post/pubPost')
# headers = {'token': token,
#            'deviceType': 'android',
#            'platformNo': 'Android'
#            }
# data = {'rewardTypeId': '1',
#         'channelId': '306',
#         'imgTexts': [{"text": "超级便宜的衣服特卖了f000good"},
#                      {"img": "T1tVKTB4bT1RCvBVdK.jpg", "width": "922", "height": "1280", "text": "大家快来看啦，顶顶顶"}],
#         'postTypeId': '0'}
# DataAll = {'headers':headers,
#             'json':data}
#
# DataAll = {'headers': headers, 'json': data}
# text = HttpService.MyHTTP().post(url, **DataAll)
# print(text)






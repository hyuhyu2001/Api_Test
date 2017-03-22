#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'laifuyu'

import urllib.request
import http.cookiejar
import urllib.parse
import ssl

class MyHttp:
    '''配置要测试接口服务器的ip、端口、域名等信息，封装http请求方法，http头设置'''

    def __init__(self, protocol, host, port, header = {}):
        # 从配置文件中读取接口服务器IP、域名，端口
        self.protocol = protocol
        self.host = host
        self.port = port
        self.headers = header  # http 头

        #install cookie
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)

        # 添加以支持ssl # 注意，发起的请求要为443端口
        https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv2))
        opener = urllib.request.build_opener(https_sslv3_handler)
        urllib.request.install_opener(opener)


    # 封装HTTP xxx请求方法
    # 自由扩展
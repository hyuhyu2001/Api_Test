#!/usr/bin/env python
"""
@author:     jinzj
@desc:
接口分类：个人中心HTTP接口
接口名称：用户登录
接口类型：http
请求地址：rootUrl/account/userLogin
请求方式：POST GET
增加数据驱动框架ddt
"""

import unittest
import sys,os
from ddt import ddt,data,unpack
sys.path.append('./public')
from public import base
from public import SqlService

#读取所有excel的用例数据
filename=os.listdir(r'D:\python_pycharmWorkspace\python36\Api_Test\test_data')
TestData=[]
for i in range(0,len(filename)):
    testcasefile = filename[i]
    TestDatainfo = base.get_data(testcasefile, 'TestData')
    TestData=TestData+TestDatainfo[1:]
@ddt
class AccountUserLogin(unittest.TestCase):
    '''接口自动化测试'''
    def setUp(self):
        pass

    @data(*TestData)
    @unpack
    def test_llb(self,endPoint,requestMethod,other,requestData,token,expectedresult,path,*args):
        tok=eval(token)
        if tok['token']=='token':
            mobile=tok['mobile']
            password=tok['password']
            token=base.userlogin(mobile,password)
        else:
            token=tok['token']
        #DataAll = eval(requestData)
        url=base.get_url(endPoint)
        #判断是否需要其他接口数据
        if other!='':
            other_data=eval(other)
            other_url=base.get_url(other_data['endpoint'])
            other_method=other_data['requestmethod']
            other_dataAll=other_data['para']
            sql=other_data['sql']
            other_path=other_data['path']
            #判断是否通过查询数据库获取数据
            if sql!='':
                base.get_response(other_url+other_path,other_method,**other_dataAll)
                DB = SqlService.MyDB()
                res=DB.execute_select_one(sql)
                DB.close()
                DataAll = eval(requestData)
                self.text = base.get_response(url+path,requestMethod,*args,**DataAll)
                if expectedresult.lower() == 'true':
                    result = self.text.get('result')
                    self.assertEqual(result,True)
                else:
                    errorMessage = self.text.get(u'errorMessage')
                    self.assertEqual(errorMessage, expectedresult)
            else:
                #使用其他接口返回的数据
                response=base.get_response(other_url+other_path,other_method,**other_dataAll)
                expect=other_data['expect']
                rep=[n for n in range(len(expect))]
                for i in range(len(expect)):
                    s=expect[i].split('/')
                    r=response.get(s[0])
                    if len(s)==1:
                        rep[i]=r
                    else:
                        for j in range(1,len(s)):
                            rep[i]=r.get(s[i])
                DataAll = eval(requestData)
                self.text = base.get_response(url+path,requestMethod,*args,**DataAll)
                if expectedresult.lower() == 'true':
                    result = self.text.get('result')
                    self.assertEqual(result,True)
                else:
                    errorMessage = self.text.get(u'errorMessage')
                    self.assertEqual(errorMessage, expectedresult)
        else:
            DataAll = eval(requestData)
            self.text = base.get_response(url+path,requestMethod,*args,**DataAll)
            if expectedresult.lower() == 'true':
                result = self.text.get('result')
                self.assertEqual(result,True)
            else:
                errorMessage = self.text.get(u'errorMessage')
                self.assertEqual(errorMessage, expectedresult)

    def tearDown(self):
        print(self.text)

if __name__ == "__main__":
    unittest.main()


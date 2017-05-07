#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:从excel里读取数据，传递给数据驱动框架ddt
"""

import xlrd

class XLDataInfo(object):
    def __init__(self,path = ''):
        self.xl = xlrd.open_workbook(path)

    def get_sheet_info(self):
        infolist = []
        for row in range(0,self.sheet.nrows):#从0开始循环
            info = self.sheet.row_values(row)
            info = info[:-1]
            infolist.append(info)
        return infolist

    def get_sheetinfo_by_name(self,name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self,index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()

if __name__ == '__main__':
    datainfo = XLDataInfo(r'D:\python_pycharmWorkspace\python36\Api_Test\test_data\account_userLogin_test_data.xlsx')
    AllData = datainfo.get_sheetinfo_by_name('AllData')
    print(AllData)

    # for i in RequestData:
    #     print(i)
    # for i in ParamsData:
    #     dictParams[i] = i
    # for m in dictParams:
    #     m = dictParams.get(m)
    #     for i in range(len(ParamsData)):
    #         print(i)
    #         t = ParamsData[i] + '=%s' % (ParamsData[i])
    #         print(t)
    #         exec(t)
    #         eval(ParamsData[i])
    #     print(m)
    # print(TestData)


    # class Test:
    #     pass
    # a = Test()

    # for xx in range(97, 123):
    #     t = chr(xx) + '=Test()'
    #     print(t)
    #     exec(t)
    #     print
    #     eval(chr(xx))

    # print(a)




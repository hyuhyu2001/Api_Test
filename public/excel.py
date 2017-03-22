#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""
import os
import xlrd

def getdata():
    testfile = 'TestCase.xlsx'
    file = os.path.join(os.getcwd(),testfile)
    case = xlrd.open_workbook(file)
    sheet = case.sheet_by_index(0)
    t = []
    for i in range(0,sheet.nrows):
        data = sheet.row_values(i)
        t.append(data)
    return t


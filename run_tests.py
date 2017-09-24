#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:jinzj
@contact:
@others:
@desc:
"""
import time, sys, os
sys.path.append('./test_case')
sys.path.append('./public')
from HTMLTestRunner import HTMLTestRunner
import unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import xlrd
from public import SqlService

def send_email(filename):
    mail_host='smtp.exmail.qq.com'#SMTP.cloud-young.com
    mail_user='********'
    mail_pass='****'

    sender='****'
    receivers=['****']

    message = MIMEMultipart('related')

    f = open(filename, 'rb')
    mail_body = f.read()
    # 编写HTML类型的邮件正文
    msg = MIMEText(mail_body, 'html', 'utf-8')
    message.attach(msg)
    # 发送附件：添加附件，附件需要添加到正文后，否则mac版自带邮箱收不到内容
    att = MIMEText(mail_body, 'base64', 'uft-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att)
    f.close()

    message['From'] = sender
    message['To'] = ",".join(receivers)
    message['Subject'] = Header("测试报告", 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receivers, message.as_string())
    smtp.quit()


def report(testreport): #查找最新的测试报告
    lists = os.listdir(testreport)  #定义文件目录
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))#通过sort()方法重新按时间对目录下的文件进行排序
    filename = os.path.join(testreport, lists[-1])#list[-1]取最新生成的文件或者文件夹
    print(filename)
    return filename

def get_sql_info(file):
    path=r'D:\python_pycharmWorkspace\python36\Api_Test\test_data\%s'%file
    wk=xlrd.open_workbook(path)
    sheet=wk.sheet_by_name('TestData')
    col=sheet.ncols
    val=sheet.col_values(col-1)
    return val

if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据
    # 指定测试用例为当前文件夹下的 interface 目录
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='AllTestCase.py')
    #运行测试前清理数据
    filename=os.listdir(r'D:\python_pycharmWorkspace\python36\Api_Test\test_data')
    sqllist=[]
    for i in range(0,len(filename)):
        testcasefile = filename[i]
        sqlinfo = get_sql_info(testcasefile)
        sqllist=sqllist+sqlinfo[1:]
    DB = SqlService.MyDB()
    for sql in sqllist:
        if sql!='':
            DB.execute_delete(sql)
    DB.close()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Ling Ling Bang Interface Test Report',
                            description='The results are following:')
    runner.run(discover)
    fp.close()

    # test_report = './report' #定义报告文件目录
    # rep = report(test_report)
    # send_email(rep)

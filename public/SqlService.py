#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author:     jinzj
@desc:数据库连接获取信息
"""
import sys
import pymysql
from public import Config

class MyDB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(**Config.sql_conn_dict)
            self.cur = self.conn.cursor()
        except Exception as e:
            print('初始化数据连接失败：%s' % e)
            sys.exit()

    def get_conn(self):
        return self.conn

    def execute_select_one(self,sql):
        '''#查询引用此方法，返回一条记录'''
        try:
            reCount = self.cur.execute(sql)
            query_result = self.cur.fetchall()
            self.conn.commit()
            return query_result[0][0]
        except Exception as e:
            print('查询失败：%s' %e)
            self.conn.rollback()

    def execute_select_many(self,sql,data = ''):
        '''返回结果包含多条记录'''
        try:
            if data:
                self.cur.execute(sql, data)#execute 可以接受两个参数， 第一个参数是sql语句， 不过这个sql中的values的内容使用占位符%s表示，第二个参数是实际的写入的values列表
            else:
                self.cur.execute(sql)
            query_result = self.cur.fetchall()
            self.conn.commit()
            return query_result
        except Exception as e:
            print('查询失败：%s' %e)
            self.conn.rollback()

    def execute_insert(self, query, data):
        try:
            self.cur.execute(query, data)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()

    def execute_update(self, query, data):
        query = query % data
        try:
            self.cur.execute(query)
            self.conn.commit()
            return ('',True)
        except Exception as e:
            self.conn.rollback()
            return (e, False)

    def execute_delete(self,sql):
        '''删除引用此方法'''
        try:
            reCount = self.cur.execute(sql)
            self.conn.commit() #insert/update/delete时必须加入commmit,commit是所有语句全部提交一次
        except Exception as e:
            print('删除失败：%S' %e)
            self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()  # 关闭门
V2版本说明：
1、sqlservice独立，改为面向对象：支持增删改查（查询一条记录多条记录）
2、HttpService独立，改为面向对象：支持获取url、get、post
3、接口脚本说明：
-（1）account_userlogin_test，用户登陆接口：get方法（params=params）
-（2）account_userRegister_test，用户注册接口：post方法（data=data表单形式），数据库查询（返回一条记录，短信验证码），数据库删除（删除注册用户数据）
-（3）userLogout，用户注销接口：post方法（headers=headers）
-（4）post_pubPost_test，发帖接口：post方法（headers=headers，json=json，非表单，字符串形式）

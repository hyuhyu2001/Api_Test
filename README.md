V5版本说明：
1、sqlservice独立，改为面向对象：支持增删改查（查询一条记录多条记录）
2、HttpService独立，改为面向对象：支持获取url、get、post、delete
3、接口脚本说明：
（1）account_userlogin_test，用户登陆接口：get方法（params=params）
（2）account_userRegister_test，用户注册接口：post方法（data=data表单形式），数据库查询（返回一条记录，短信验证码），数据库删除（删除注册用户数据）
（3）userLogout，用户注销接口：post方法（headers=headers）
（4）post_pubPost_test，发帖接口：post方法（headers=headers，json=json，非表单，字符串形式）
（5）complaint_user_test，用户举报，get方法（params=params，headers=headers），bs64加密
（6）get_attendedUsers_test，获取社区成员列表，get方法（有分页params和headers，无分页headers）
（7）accept_comment_test，采纳答案，post方法（headers=headers），数据库更新（update）
（8）log_record_test，上传日志，post方法（headers=headers，json=json），参数中含有列表
（9）comment_post_test，帖子回复，post方法（headers=headers，json=json）
（10）get_friends_test，获取好友列表，post方法（带分页data和params，不带分页headers），bs64加密
（11）get_invited_list_test，获取用户通讯录，post方法（headers=headers，json=json），md5加密
（12）public_post_test，帖子公告，post方法（params=params，headers=headers）
（13）recommend_channel_test，社区推荐，post方法（params=params，headers=headers，json=json）
（14）uncollect_post_test，取消收藏帖子，post方法（headers=headers），url需要携带帖子的ID
（15）exit_channel_test，退出社区，delete方法
4、测试数据分离（excel+脚本形式）
5、改成一个脚本执行所有的excel用例，不用单独编写代码文件

5、增加log记录
6、增加files的示例
7、测试数据、方法、结果全部放在excel中
8、nose和pytest框架


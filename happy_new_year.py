import itchat
import random
import time
import os
import sys

have_send=False
name_dic={}

group_dic={'李小勇':0}
greet_dic={0:'老师祝你新年快乐',1:'同学祝你中秋快乐'}
t='20:30:10'
   
itchat.auto_login()
for user in group_dic:
    name_dic[user]=itchat.search_friends(name=user)[0]['UserName'] 
print('get userInfo successfully!')
for user in group_dic:
    print('姓名:'+user+' 分组:'+str(group_dic[user]))
              
while 1:
    if time.strftime("%H:%M:%S")==t:
        if have_send==False:
            for user in group_dic:
                greet=greet_dic[group_dic[user]]
                itchat.send(greet,toUserName=name_dic[user])
                print(user+':'+greet)
            have_send=True
            print('发送完毕！')
            


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 11:57:01 2017

@author: ASeeder
"""


import smtplib
from email.mime.text import MIMEText  
from email.header import Header  
  
# 第三方 SMTP 服务  
mail_host="smtp.qq.com"  #设置服务器  
mail_user="2210132692@qq.com"#用户名  
mail_pass="ushcsjfrfaxeebfh"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格  


sender = mail_user
receivers = ['2210132692@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱  
   
message = MIMEText('a test for python', 'plain', 'utf-8')  
message['From'] = Header("ppyy", 'utf-8')  
message['To'] =  Header("you", 'utf-8')  
  
subject = 'my test'  
message['Subject'] = Header(subject, 'utf-8')  
  
try:  
  smtpObj = smtplib.SMTP_SSL(mail_host, 465)   
  smtpObj.login(mail_user,mail_pass)
  smtpObj.sendmail(sender, receivers, message.as_string())  
  smtpObj.quit()  
  print u"邮件发送成功"  
except smtplib.SMTPException,e:  
  print e  
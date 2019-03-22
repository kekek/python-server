#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import argparse
 
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
def get_host_name():
    return os.uname()[1]

def sendmail(subject, mail_msg, to= ["jinyf@ktkt.com"]):
    # 第三方 SMTP 服务
    mail_host="smtp.exmail.qq.com"  #设置服务器
    mail_user="xxx@qq.com"    #用户名
    mail_pass="xxxx"   #口令 
    mail_port= 25   #口令 

    sender = 'xxx@qq.com'
    receivers = to  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
    # mail_msg = """
    # <p>Python 邮件发送测试...</p>
    # <p><a href="http://www.runoob.com">这是一个链接</a></p>
    # """
    message = MIMEText(mail_msg, 'html', 'utf-8')
    message['From'] = Header(get_host_name(), 'utf-8')
    message['To'] =  Header("测试", 'utf-8')
    
    # subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, mail_port)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("发送报警邮件")
    parser.add_argument("-s", "--subject", help='邮件主题', dest="subject", required=True)
    parser.add_argument("-m", "--message", help='邮件内容', dest = "message",required=True)
    parser.add_argument("-t", "--to", help='收件人user1 user2', nargs='+', action='store',dest='to')
    args=parser.parse_args()

    print "message:", args.message
    print "Subject:", args.subject
    print "to", args.to

    receivers = ["jinyf@ktkt.com"]
    # print type(args.to)
    if len(args.to) > 0:
        receivers = args.to
    
    sendmail(args.subject, args.message, args.to)


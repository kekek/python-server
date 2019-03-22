### python 发送邮件
   
	简单发送邮件

#### 兼容性

- sendmail.py 最低兼容python2.3, [python-argparse 只在python2.3以上版本测试]

- 由于python-argparse 在python2.6以下是以第三方包存在， 需要在2.6 及以下使用，使用以下命令安装 python-argparse依赖 

```
   // install depence
   yum -y instsall python-argparse
```

#### example
```
./sendmail.py -s "test subject " -m "test msg" -t jinyf@ktkt.com
```
#### usage 
```
./sendmail.py -h

usage: 发送报警邮件 [-h] -s SUBJECT -m MESSAGE [-t TO [TO ...]]

optional arguments:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT
                        邮件主题
  -m MESSAGE, --message MESSAGE
                        邮件内容
  -t TO [TO ...], --to TO [TO ...]
                        收件人user1 user2
```

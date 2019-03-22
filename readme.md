### python 发送邮件

#### 兼容性
- sendmail.py 最低兼容2.7

- sendmail_v1.py 兼容2.6

- 2.6 使用python argparse 使用执行：
```
   // install depence
   yum -y instsall python-argparse
```

#### example
```
./sendmail.py -s "test subject " -m "test msg" -t jinyf@ktkt.com
```

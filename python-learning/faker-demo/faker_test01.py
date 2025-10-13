"""
Faker是一个用于生成虚假数据的Python库，它提供了一种简单而强大的方式来生成各种类型的随机数据，包括姓名、地址、电子邮件、文本、日期、数字等。
    1.运行前需要安装第三方库 faker，可使用以下命令进行安装：
        pip install faker
    2.若安装过程中出现超时问题，可使用国内镜像源进行安装，命令如下：
        pip install -i https://mirrors.aliyun.com/pypi/simple/ faker
"""

from faker import Faker


fake_en = Faker()
print('\n英文数据：')
print(fake_en.name())
print(fake_en.address())
print(fake_en.ssn())
print(fake_en.company())

fake_cn = Faker('zh_CN')  # 支持中文！
print('\n中文数据：')
print(fake_cn.name())
print(fake_cn.address())
print(fake_cn.ssn())
print(fake_cn.company())

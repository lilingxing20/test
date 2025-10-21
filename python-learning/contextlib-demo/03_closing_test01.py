"""
closing 上下文管理器
  1. closing 上下文管理器可以在代码块执行完毕后自动关闭资源
  2. closing 上下文管理器必须实现 __enter__() 和 __exit__() 方法
  3. __enter__() 方法返回的值会绑定到 as 子句中的目标变量上
"""

import os
from contextlib import closing


# 示例1：使用 closing 上下文管理器关闭文件
print('示例1：使用 closing 上下文管理器关闭文件')
current_dir = os.path.dirname(__file__)
with closing(open(os.path.join(current_dir, 'test.txt'), 'w')) as f:
    f.write('hello world')
with open(os.path.join(current_dir, 'test.txt'), 'r') as f: 
    print(f.read())
""" 执行结果
hello world
"""


# 示例2：使用 closing 上下文管理器关闭网络连接
# 如果对象没有实现上下文，就不能用with语句。此时可以用closing()来把该对象变为上下文对象。
from urllib.request import urlopen
print('示例2：使用 closing 上下文管理器关闭网络连接')
url = 'https://python.org'
with closing(urlopen(url)) as page:
    for line in page:
        print(line.decode('utf-8'))     

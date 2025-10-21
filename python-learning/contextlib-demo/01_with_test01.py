"""
with 语句
  1. 上下文管理器必须实现 __enter__() 和 __exit__() 方法
  2. with 语句会在代码块执行前调用 __enter__() 方法，执行后调用 __exit__() 方法
  3. __enter__() 方法返回的值会绑定到 as 子句中的目标变量上
"""

import os


# 示例1：使用 with 语句打开文件
current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'test.txt'), 'w') as f:
    f.write('hello world')
    # 不需要调用 f.close() 方法，with 语句会自动调用 __exit__() 方法关闭文件
with open(os.path.join(current_dir, 'test.txt'), 'r') as f: 
    print(f.read())

""" 执行结果
hello world
"""


# 示例2：自定义上下文管理器
class Work(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin do work')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error do work')
        else:
            print('End do work')

    def do_work(self):
        print('%s do work ...' % self.name)


with Work('Bob') as q:
    q.do_work()
    
"""执行结果
Begin do work
Bob do work ...
End do work
"""

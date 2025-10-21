"""
contextmanager 装饰器
  1. contextmanager 装饰器可以将一个函数转换为上下文管理器
  2. 被装饰的函数必须包含一个 yield 语句，yield 语句之前的代码会在 __enter__() 方法中执行，yield 语句之后的代码会在 __exit__() 方法中执行
  3. yield 语句返回的值会绑定到 as 子句中的目标变量上
"""

import contextlib


# 示例1：使用 contextmanager 装饰器定义上下文管理器
print('示例1：使用 contextmanager 装饰器定义上下文管理器')
@contextlib.contextmanager
def work(name):
    print('Begin do work')
    yield name
    print('End do work')


with work('Bob') as q:
    print(q)
""" 执行结果
Begin do work
Bob
End do work
"""


# 示例2： 使用 contextmanager 装饰器定义上下文管理器，处理异常
print('示例2： 使用 contextmanager 装饰器定义上下文管理器，处理异常')
class Work(object):
    def __init__(self, name):
        self.name = name

    def do_work(self):
        print('%s do work ...' % self.name)


@contextlib.contextmanager
def cwork(name):
    print('Begin do work')
    work = Work(name)
    yield work
    print('End do work')


with cwork('Bob') as worker:
    worker.do_work()
""" 执行结果
Begin do work
Bob do work ...
End do work
"""

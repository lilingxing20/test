"""
5. 其他重要关键字
"""

# import/from/as 模块导入
import math as m
from os import path

# global/nonlocal 变量作用域
x = 10
def func():
    global x
    x = 20

# assert 断言
assert 2+2 == 4, "数学错误"

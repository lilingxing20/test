"""
2. 函数相关关键字
"""

# def/return/yield 函数定义
def add(a, b):
    return a + b

def generator():
    yield 1
    yield 2


# lambda 匿名函数
square = lambda x: x**2
print(square(5))  # 输出25

""" 函数参数定义：
1. 参数默认不可变变量
2. 参数默认可变变量
"""


# 1. 参数默认不可变变量
def add_mutable(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

# 2. 参数默认可变变量
def add_immutable(value, items=[]):
    items.append(value)
    return items

# 测试
print(add_mutable(1))  # [1]
print(add_mutable(2))  # [2]
print(add_mutable(3))  # [3]

print(add_immutable(1))  # [1]
print(add_immutable(2))  # [1, 2]
print(add_immutable(3))  # [1, 2, 3]

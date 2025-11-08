""" 变量类型
1. 可变类型：int、float、bool、str、list、set、dict, 修改时内存地址不变。
2. 不可变类型：int、float、bool、str、tuple、frozenset、bytes、bytearray, 修改时内存地址改变。
"""

# 可变类型
def add_mutable(items, value):
    items.append(value)
    return items

# 不可变类型
def add_immutable(items, value):
    items += (value,)
    return items


# 测试可变类型
my_list = [1, 2, 3]
add_mutable(my_list, 4)
print(my_list)    # [1, 2, 3, 4]

# 测试不可变类型
my_tuple = (1, 2, 3)
add_immutable(my_tuple, 4)
print(my_tuple)    # (1, 2, 3)

""" 推导式
    1. 列表推导式
    2. 字典推导式
    3. 集合推导式
    4. 生成器推导式
    5. 元组推导式
    6. 嵌套推导式
    7. 条件推导式
    8. 循环推导式
    9. 嵌套循环推导式
    10. 嵌套条件推导式
    11. 嵌套循环条件推导式
"""

# 1. 列表推导式
# 语法：
# [表达式 for item in iterable if 条件]
# 功能：根据条件对iterable中的元素进行筛选，符合条件的元素将会被表达式计算并生成新的列表。

# 示例1：
# 计算1到10的平方
print("1.1 列表推导式示例1：")
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 示例2：
# 计算1到10的偶数平方
print("1.2 列表推导式示例2：")
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]


# 2. 字典推导式
# 语法：
# {key表达式:value表达式 for item in iterable if 条件}
# 功能：根据条件对iterable中的元素进行筛选，符合条件的元素将会被key表达式和value表达式计算并生成新的字典。

# 示例1：
# 计算1到10的偶数平方和偶数的和
print("2.1 字典推导式示例1：")
even_squares_and_sum = {f"k{x}":f"v{x**2}" for x in range(1, 11) if x % 2 == 0}
print(even_squares_and_sum)  # {'k2': 'v4', 'k4': 'v16', 'k6': 'v36', 'k8': 'v64', 'k10': 'v100'}


# 3. 集合推导式
# 语法：
# {表达式 for item in iterable if 条件}
# 功能：根据条件对iterable中的元素进行筛选，符合条件的元素将会被表达式计算并生成新的集合。

# 示例1：
print("3.1 集合推导式示例1：")
# 计算1到10的偶数平方和偶数的和
even_squares_and_sum = {x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares_and_sum)  # {64, 100, 4, 36, 16}  无序


# 4. 生成器推导式
# 语法：
# (表达式 for item in iterable if 条件)
# 功能：根据条件对iterable中的元素进行筛选，符合条件的元素将会被表达式计算并生成新的生成器。

# 示例1：
print("4.1 生成器推导式示例1：")
# 计算1到10的偶数平方和偶数的和
even_squares_and_sum = (x**2 for x in range(1, 11) if x % 2 == 0)
print(even_squares_and_sum)  # <generator object <genexpr> at 0x10a3a3a90>
print(list(even_squares_and_sum))  # [4, 16, 36, 64, 100]


# 5. 元组推导式
# 语法：
# (表达式 for item in iterable if 条件)
# 功能：根据条件对iterable中的元素进行筛选，符合条件的元素将会被表达式计算并生成新的元组。

# 示例1：
# 计算1到10的偶数平方和偶数的和
print("5.1 元组推导式示例1：")
even_squares_and_sum = (x**2 for x in range(1, 11) if x % 2 == 0)
print(even_squares_and_sum)  # <generator object <genexpr> at 0x10a3a3a90>
print(tuple(even_squares_and_sum))  # (4, 16, 36, 64, 100)


# 6. 嵌套推导式
# 语法：
# [表达式 for item in iterable1 for item in iterable2 if 条件]
# 功能：对iterable1中的元素进行迭代，对每个元素的iterable2中的元素进行迭代，符合条件的元素将会被表达式计算并生成新的列表。

# 示例1：
# 计算1到3的所有可能的组合
print("6.1 嵌套推导式示例1：")
combinations = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(combinations)  # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# 7. 条件推导式
# 语法：
# [表达式 if 条件 else 表达式2 for item in iterable]
# 功能：对iterable中的元素进行迭代，如果条件为真，则表达式计算并生成新的列表，否则表达式2计算并生成新的列表。

# 示例1：
# 计算1到10的偶数平方和奇数的立方a
print("7.1 条件推导式示例1：")
even_squares_or_odd_cubes = [x**2 if x % 2 == 0 else x**3 for x in range(1, 11)]
print(even_squares_or_odd_cubes)  # [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]


# 8. 循环推导式
# 语法：
# [表达式 for item in iterable for item in iterable2]
# 功能：对iterable中的元素进行迭代，对每个元素的iterable2中的元素进行迭代，将所有元素计算并生成新的列表。

# 示例1：
# 计算1到3的所有可能的组合
print("8.1 循环推导式示例1：")
combinations = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(combinations)  # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# 9. 嵌套循环推导式
# 语法：
# [表达式 for item in iterable1 for item in iterable2 for item in iterable3]
# 功能：对iterable1中的元素进行迭代，对每个元素的iterable2中的元素进行迭代，对每个元素的iterable3中的元素进行迭代，将所有元素计算并生成新的列表。

# 示例1：
# 计算1到3的所有可能的组合
print("9.1 嵌套循环推导式示例1：")
combinations = [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]
print(combinations)  # [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3), (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), (2, 3, 3), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2


# 10. 嵌套条件推导式
# 语法：
# [表达式 if 条件 else 表达式2 for item in iterable1 for item in iterable2 if 条件]
# 功能：对iterable1中的元素进行迭代，对每个元素的iterable2中的元素进行迭代，如果条件为真，则表达式计算并生成新的列表，否则表达式2计算并生成新的列表。

# 示例1：
# 计算1到3的所有可能的组合
print("10.1 嵌套条件推导式示例1：")
combinations = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(combinations)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# 11. 嵌套循环条件推导式
# 语法：
# [表达式 if 条件 else 表达式2 for item in iterable1 for item in iterable2 if 条件]
# 功能：对iterable1中的元素进行迭代，对每个元素的iterable2中的元素进行迭代，如果条件为真，则表达式计算并生成新的列表，否则表达式2计算并生成新的列表。

# 示例1：
# 计算1到3的所有可能的组合
print("11.1 嵌套循环条件推导式示例1：")
combinations = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(combinations)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

""" pandas 系列（Series）

Series 是 pandas 中最基本的数据结构，它类似于一维数组，但它可以包含多个数据类型。

Series 的索引（index）是Series的重要组成部分，它是Series的标签，用于标识Series中的数据。
Series 的切片（slicing）是Series的另一个重要操作，它可以用来选取Series中的一部分数据。

Series 可以通过多种方式创建，包括从列表、字典、numpy数组等。

Series 的核心属性有：

- `values`：获取Series的数值数组
- `index`：获取Series的索引标签
- `dtype`：获取Series的数据类型
- `name`：获取或设置Series的名称

Series 的基本操作包括：
- 算术运算：加减乘除、求和、求均值、求方差、求最大值、求最小值等
- 统计运算：求均值、求方差、求最大值、求最小值、求百分位数等
- 向量化运算：对Series中的每个元素进行操作，如对Series中的每个元素进行平方、对Series中的每个元素进行求和等

本文将介绍Series的创建、核心属性、索引和切片、基本操作等内容。

"""

import pandas as pd


print("="*50)
print("2. Series的核心属性")
print("="*50)

# 创建一个示例Series
students = pd.Series([90, 85, 92, 88, 95], 
                    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

print("Series数据：")
print(students)
print("\n核心属性：")
print(f"索引：{students.index}")      # 获取索引
print(f"值：{students.values}")      # 获取值数组
print(f"形状：{students.shape}")     # 获取形状
print(f"数据类型：{students.dtype}") # 数据类型
print(f"大小：{students.size}")      # 元素个数
print()


""" 运行结果：
==================================================
2. Series的核心属性
==================================================
Series数据：
Alice      90
Bob        85
Charlie    92
David      88
Eve        95
dtype: int64

核心属性：
索引：Index(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], dtype='object')
值：[90 85 92 88 95]
形状：(5,)
数据类型：int64
大小：5

"""

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
print("4. Series的基本操作")
print("="*50)

# 数学运算
print("所有成绩加5分：")
print(students + 5)

print("\n成绩乘以1.1：")
print(students * 1.1)

# 统计操作
print(f"\n平均分：{students.mean()}")
print(f"最高分：{students.max()}")
print(f"最低分：{students.min()}")
print(f"标准差：{students.std()}")

# 向量化操作
bonus = pd.Series([5, 3, 2, 4, 1], index=students.index)
print("\n加上额外加分：")
print(students + bonus)


""" 运行结果：
==================================================
4. Series的基本操作
==================================================
所有成绩加5分：
Alice       95
Bob         90
Charlie     97
David       93
Eve        100
dtype: int64

成绩乘以1.1：
Alice       99.0
Bob         93.5
Charlie    101.2
David       96.8
Eve        104.5
dtype: float64

平均分：90.0
最高分：95
最低分：85
标准差：3.8078865529319543

加上额外加分：
Alice      95
Bob        88
Charlie    94
David      92
Eve        96
dtype: int64
"""

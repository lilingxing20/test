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
print("3. Series的索引和切片")
print("="*50)

print("原始Series：")
print(students)
print()

# 按标签索引
print("Bob的成绩：", students['Bob'])
print("Charlie的成绩：", students.loc['Charlie'])

# 按位置索引
print("第一个元素：", students.iloc[0])  # 使用iloc来明确按位置访问
print("前三个元素：", students.iloc[:3])

# 布尔索引
print("90分以上的学生：")
print(students[students > 90])

# 多标签索引
print("多个学生成绩：")
print(students[['Alice', 'David', 'Eve']])
print()


""" 运行结果：
==================================================
3. Series的索引和切片
==================================================
原始Series：
Alice      90
Bob        85
Charlie    92
David      88
Eve        95
dtype: int64

Bob的成绩： 85
Charlie的成绩： 92
第一个元素： 90
前三个元素： Alice      90
Bob        85
Charlie    92
dtype: int64
90分以上的学生：
Charlie    92
Eve        95
dtype: int64
多个学生成绩：
Alice    90
David    88
Eve      95
dtype: int64

"""

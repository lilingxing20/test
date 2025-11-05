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
import numpy as np


print("="*50)
print("1. 创建Series的多种方式")
print("="*50)

# 方式1：从列表创建（最常用）
data_list = [90, 85, 92, 88]
scores = pd.Series(data_list)
print("从列表创建：")
print(scores)
print()

# 方式2：从列表创建并指定索引
scores_named = pd.Series([90, 85, 92, 88], 
                        index=['张三', '李四', '王五', '赵六'])
print("带自定义索引的Series：")
print(scores_named)
print()

# 方式3：从字典创建（键自动成为索引）
data_dict = {'张三': 90, '李四': 85, '王五': 92, '赵六': 88}
scores_dict = pd.Series(data_dict)
print("从字典创建：")
print(scores_dict)
print()

# 方式4：从numpy数组创建
arr = np.array([90, 85, 92, 88])
scores_np = pd.Series(arr, index=['A', 'B', 'C', 'D'])
print("从numpy数组创建：")
print(scores_np)
print()


""" 运行结果：
==================================================
1. 创建Series的多种方式
==================================================
从列表创建：
0    90
1    85
2    92
3    88
dtype: int64

带自定义索引的Series：
张三    90
李四    85
王五    92
赵六    88
dtype: int64

从字典创建：
张三    90
李四    85
王五    92
赵六    88
dtype: int64

从numpy数组创建：
A    90
B    85
C    92
D    88
dtype: int64

"""

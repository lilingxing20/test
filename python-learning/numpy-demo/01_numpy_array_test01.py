""" NumPy ndarray对象
NumPy是Python中用于科学计算的基础软件包，其核心数据结构是ndarray（n-dimensional array）。
numPy最重要的一个特点是其N维数组对象ndarray，它是一系列同类型数据的集合，以0下标为开始进行集合中元素的索引。
ndarray对象是用于存放同类型元素的多维数组。
ndarray中的每个元素在内存中都有相同存储大小的区域。

ndarray内部由以下内容组成：
  - 一个指向数据（内存或内存映射文件中的一块数据）的指针。
  - 数据类型或dtype，描述在数组中的固定大小值的格子。
  - 一个表示数组形状（shape）的元组，表示各维度大小的元组。

numPy的数组中比较重要ndarray对象属性有：
  - ndarray.shape：数组的维度，例如，(2,3)表示2行3列的数组。
  - ndarray.size：数组元素的总个数，等于数组的所有维度的乘积。
  - ndarray.dtype：数组中元素的类型，例如，int32、float64等。
  - ndarray.itemsize：数组中每个元素的字节大小，例如，一个float64类型的元素占用8个字节。
  - ndarray.nbytes：数组占用的总字节数，等于数组元素的总个数乘以每个元素的字节大小。
  - ndarray.ndim：数组的维度数。
  - ndarray.data：数组中数据的指针。
  - ndarray.strides：数组在内存中的步长，用于访问数组的不同元素。

NumPy的ndarray对象可以进行很多操作，包括：
  - 数组的创建和转换
  - 数组的索引和切片
  - 数组的运算和操作
  - 数组的广播（broadcasting）
  - 数组的排序和搜索
  - 数组的统计和聚合函数
  - 数组的输入输出

本文主要介绍ndarray对象，并通过实例介绍ndarray的创建、索引、切片、运算、广播、排序、统计和聚合函数等操作。
"""

import numpy as np

# 创建ndarray对象
print("1. 创建ndarray对象")
a = np.array([1, 2, 3])
print(a)
# 输出：[1 2 3]

# 数组的维度
print("2. 数组的维度")
print(a.shape)
# 输出：(3,)

# 数组元素的总个数
print("3. 数组元素的总个数")
print(a.size)
# 输出：3


# 数组中元素的类型
print("4. 数组中元素的类型")
print(a.dtype)
# 输出：int64

# 数组中每个元素的字节大小
print("5. 数组中每个元素的字节大小")
print(a.itemsize)
# 输出：8

# 数组占用的总字节数
print("6. 数组占用的总字节数")
print(a.nbytes)
# 输出：24

# 数组的维度数
print("7. 数组的维度数")
print(a.ndim)
# 输出：1

# 数组中数据的指针
print("8. 数组中数据的指针")
print(a.data)

# 数组在内存中的步长
print("9. 数组在内存中的步长")
print(a.strides)

# 数组的创建和转换
print("10. 数组的创建和转换")
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# 输出：[[1 2 3]
#       [4 5 6]]

# 数组的索引和切片
print("11. 数组的索引和切片")
print(b[0, 1])
# 输出：2
print(b[1, :])
# 输出：[4 5 6]


# 数组的运算和操作
print("12. 数组的运算和操作")
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(c + d)
# 输出：[5 7 9]
print(c * 2)
# 输出：[2 4 6]


# 数组的广播（broadcasting）
print("13. 数组的广播（broadcasting）")
e = np.array([1, 2, 3])
f = np.array([4, 5, 6])
print(e + f)
# 输出：[5 7 9]


# 数组的排序和搜索
print("14. 数组的排序和搜索")
g = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
print(np.sort(g))       # 返回排序后的数组
# 输出：[1 1 2 3 3 4 5 5 5 6 9]
print(np.argsort(g))    # 返回排序后的索引
# 输出：[1 3 0 2 4 5 8 7 9 6 10]


# 数组的统计和聚合函数
print("15. 数组的统计和聚合函数")
print(np.mean(g))    # 计算平均值
# 输出：4.545454545454546
print(np.median(g))  # 计算中位数
# 输出：4.5
print(np.std(g))     # 计算标准差
# 输出：2.8027681662099564
print(np.sum(g))     # 计算和
# 输出：45
print(np.prod(g))    # 计算乘积
# 输出：1080
print(np.max(g))     # 计算最大值
# 输出：9
print(np.min(g))     # 计算最小值
# 输出：1
print(np.median(g))  # 计算中位数
# 输出：4.5
print(np.std(g))     # 计算标准差
# 输出：2.8027681662099564
print(np.sum(g))     # 计算和
# 输出：45
print(np.prod(g))    # 计算乘积
# 输出：1080
print(np.max(g))     # 计算最大值
# 输出：9
print(np.min(g))     # 计算最小值
# 输出：1


# 数组的输入输出
print("16. 数组的输入输出")
np.save('test.npy', g)
h = np.load('test.npy')
print(h)
# 输出：[3 1 4 1 5 9 2 6 5 3 5]


""" 运行结果：
1. 创建ndarray对象
[1 2 3]

2. 数组的维度
(3,)

3. 数组元素的总个数
3

4. 数组中元素的类型
int64

5. 数组中每个元素的字节大小
8

6. 数组占用的总字节数
24

7. 数组的维度数
1

8. 数组中数据的指针
<memory at 0x10402f580>

9. 数组在内存中的步长
(8,)

10. 数组的创建和转换
[[1 2 3]
 [4 5 6]]

11. 数组的索引和切片
2
[4 5 6]

12. 数组的运算和操作
[5 7 9]
[2 4 6]

13. 数组的广播（broadcasting）
[5 7 9]

14. 数组的排序和搜索
[1 1 2 3 3 4 5 5 5 6 9]
[1 3 0 2 4 5 8 7 9 6 10]

15. 数组的统计和聚合函数
4.545454545454546
4.5
2.8027681662099564
45
1080
9
1

16. 数组的输入输出
[3 1 4 1 5 9 2 6 5 3 5]
"""

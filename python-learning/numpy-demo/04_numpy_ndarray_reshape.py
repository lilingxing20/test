""" 切片和索引及修改数组维度
"""

import numpy as np


# 改变数组的形状(维度),修改维度时，修改后的数据包含元素与修改的数据个数要相等，如a 12个 ,b 3*4个 ，c 2*2*3个
a = np.arange(12)
print(a)
b = a.reshape((3, 4))    # 改变数组的形状 3行4列
print(b)
c = a.reshape((2, 2, 3))  # 改变数组的形状 2行2列3层
print(c)
d = np.reshape(c,(2,6))   # 改变数组的形状 2行6列
print(d)
 
# 将多维数组修改为一维数组
print(d.reshape(-1))
 
# 切片操作
print(a[::-1])  # 倒置反转
# 切片使用[行进行切片,列进行切片]  [start:stop:step,start:stop:step,start:stop:step]
print(c[1][1][2])   # 使用方法同list
# 通过坐标法获取
print(c[1,1,2])
# 同时获取不同的行和列数据
print(c[(0,0,0),(0,1,1),(1,1,1)])

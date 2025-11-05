""" 数组的拼接
    numpy.concatenate函数用于沿指定轴连接相同形状的两个或多个数组，
    numpy.concatenate((al, a2,...), axis)，参数说明：
      - al, a2,....相同类型的数组
      - axis:沿着它连接数组的轴，默认为0，0为垂直，1为水平
"""

import numpy as np
 
a = np.random.randint(1, 6, size=(2, 4))    # 随机生成2行4列的数组
b = np.random.randint(5, 11, size=(2, 4))    # 随机生成2行4列的数组
print(a)
print(b)
c = np.hstack([a, b])  # 水平合并
print(c)
d = np.vstack([a, b])  # 垂直合并
print(d)
e = np.concatenate((a, b), axis=0)  # 0为垂直
print(e)
f = np.concatenate((a, b), axis=1)  # 1为水平
print(f)

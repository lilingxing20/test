import numpy as np


# 1. 使用array创建一个一维数组，一层[]括号
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(a), a)
# 打印结果：<class 'numpy.ndarray'> [1 2 3 4 5 6 7 8 9]

# 2. 使用array创建一个二维数组，两层[]括号
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
# 打印结果：[[1 2 3]

# 3. array 的dtype参数使用，指定创建的数组类型是浮点型，默认为整数型
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='float')
print('指定dtype参数创建数组：', c)
# 打印结果：指定dtype参数创建数组： [1. 2. 3. 4. 5. 6. 7. 8. 9.]

# 4. array 的ndmin参数使用，指定创建数组的维度
d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], ndmin=3)  # 创建三维数组
print('指定ndmin参数创建数组：', d)
# 打印结果：指定ndmin参数创建数组： [[[1 2 3]
#                               [4 5 6]
#                               [7 8 9]]]

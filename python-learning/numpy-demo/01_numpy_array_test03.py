""" NumPy ndarray数组
创建方法：
1. 从Python列表或元组创建ndarray数组
2. 从现有数组创建新的ndarray数组
3. 使用NumPy提供的函数创建ndarray数组

"""

from re import I
import numpy as np


# 1. 从Python列表或元组创建ndarray数组
print("1. 从Python列表或元组创建ndarray数组")
a = np.array([1, 2, 3, 4, 5])
print(a)

# 2. 从现有数组创建新的ndarray数组
print("2. 从现有数组创建新的ndarray数组")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

# 3. 使用NumPy提供的函数创建ndarray数组: zeros, ones, empty, arange, linspace, random
print("3. 使用NumPy提供的函数创建ndarray数组")
a = np.zeros((2, 3))
print(a)

b = np.ones((2, 3))
print(b)

c = np.empty((2, 3))
print(c)

d = np.arange(10, 30, 5)
print(d)

e = np.linspace(0, 2, 9)
print(e)

f = np.random.random((2, 3))
print(f)

# 4. 数组的属性和方法
print("4. 数组的属性和方法")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
c = np.array([[1, 2], [4, 5]])
print("# 1. 数组的形状")
print(a.shape)
print("# 2. 数组的元素的数据类型")
print(a.dtype)
print("# 3. 数组元素的总个数")
print(a.size)
print("# 4. 数组的维度")
print(a.ndim)
print("# 5. 数组的元素")
print(a.item(0))
print(a.item(0, 1))
print("# 6. 数组的转置")
print(a.T)
print("# 7. 改变数组的形状")
print(a.reshape(3, 2))
print("# 8. 数组的拼接 (纵向拼接)")
print(np.vstack((a, b)))
print("# 9. 数组的拼接 (横向拼接)")
print(np.hstack((a, c)))
print("# 10. 数组的切片")
print(a[0, 1])  # 数组的第一个元素的第二个元素
print(a[0, :])  # 数组的第一个元素的所有元素
print(a[:, 1])  # 数组的所有元素的第二个元素
print(a[0, 1:3])  # 数组的第一个元素的第二个元素到第三个元素
print(a[0, ::2])  # 数组的第一个元素的所有元素，步长为2
print(a[0, ::-1])  # 数组的第一个元素的所有元素，逆序
print(a[0, 1:3:2])  # 数组的第一个元素的第二个元素到第三个元素，步长为2
print(a[0, 1::2])  # 数组的第一个元素的第二个元素到最后一个元素，步长为2
print(a[0, ::-2])  # 数组的第一个元素的所有元素，逆序，步长为2
print("# 11. 数组的展开")
print(a.flatten())
print("# 12. 数组的转换")
print(a.tolist())
print("# 14. 数组的最大值所在的索引")
print(a.argmax())
print("# 15. 数组的最小值所在的索引")
print(a.argmin())
print("# 16. 数组的平均值")
print(a.mean())
print("# 17. 数组的标准差")
print(a.std())
print("# 18. 数组的累加和")
print(a.cumsum())
print("# 19. 数组的裁剪")
print(a.clip(1, 5))
print("# 20. 数组的四舍五入")
print(a.round(2))
print("# 21. 数组的元素的布尔值")
print(a[a > 2])
print("# 22. 数组的迹")
print(a.trace())

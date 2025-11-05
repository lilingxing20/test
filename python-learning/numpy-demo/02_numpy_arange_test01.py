""" NumPy arange函数
NumPy的arange函数用于创建一个数组，其元素是一个范围内的连续整数。
该函数可以传入一个整数类型的参数n，函数返回值看着像一个列表，其实返回值类型是numpy.ndarray。这是Numpy中特有的数组类型。如果传入arange函数的参数值是n，那么arange,函数会返回0到n-1的ndarray类型的数组。（左闭右开原则），用来创建指定范围数据数组，语法格式：numpy.arange(start, stop, step, dtype)
参数：
  - start：起始值，默认为0  
  - stop ： 终止值（不包含，符合左闭右开原则）
  - step ：步长，默认为1  ，
  - dtype : 返回的数据类型，如果没有指定，返回输入时的数据类型
"""

import numpy as np


# 1. 传入一个整数n，返回0到n-1的ndarray类型数组
print("1. 传入一个整数n，返回0到n-1的ndarray类型数组")
arr1 = np.arange(5)
print(arr1)  # [0 1 2 3 4]
print(type(arr1))  # <class 'numpy.ndarray'>

# 2. 传入起始值、终止值、步长，返回指定范围的ndarray类型数组
print("2. 传入起始值、终止值、步长，返回指定范围的ndarray类型数组")
arr2 = np.arange(2, 10, 2)
print(arr2)  # [2 4 6 8]

# 3. 传入起始值、终止值、步长、数据类型，返回指定范围的ndarray类型数组
print("3. 传入起始值、终止值、步长、数据类型，返回指定范围的ndarray类型数组")
arr3 = np.arange(2.0, 10.0, 2.0, dtype=np.int32)
print(arr3)  # [2 4 6 8]

# 4. 创建空数组
print("4. 创建空数组")
arr4 = np.array(())
print(arr4)  # array([], dtype=float64)
arr4 = np.array([])
print(arr4)  # array([], dtype=float64)
arr4 = np.array({})
print(arr4)  # array([], dtype=float64)
arr4 = np.array(None)
print(arr4)  # array(None, dtype=object)
arr4 = np.arange(0)
print(arr4)  # array([], dtype=int64)

# 5. 传入一个浮点数，返回一个数组，其中元素为该浮点数
print("5. 传入一个浮点数，返回一个数组，其中元素为该浮点数")
arr5 = np.arange(3.14)
print(arr5)  # [0. 1. 2.]

# 6. 传入一个负数，返回一个数组，其中元素为该负数
print("6. 传入一个负数，返回一个数组，其中元素为该负数")
arr6 = np.arange(-3)
print(arr6)  # [-3 -2 -1]
arr6 = np.arange(-5)
print(arr6)  # [-5 -4 -3 -2 -1]

# 7. 传入一个布尔值，返回一个数组，其中元素为该布尔值的整数值
print("7. 传入一个布尔值，返回一个数组，其中元素为该布尔值的整数值")
arr7 = np.arange(True)
print(arr7)  # [1]
arr7 = np.arange(False)
print(arr7)  # [0]

# 8. 传入一个字符串，返回一个数组，其中元素为该字符串的ASCII码值
print("8. 传入一个字符串，返回一个数组，其中元素为该字符串的ASCII码值")
arr8 = np.array('hello')
print(arr8)  # [104 101 108 108 111]

# 9. 传入多个参数，返回一个数组，其中元素为参数的笛卡尔积
print("9. 传入多个参数，返回一个数组，其中元素为参数的笛卡尔积")    
arr9 = np.arange(1, 4)
print(arr9)  # [1 2 3]
arr9 = np.arange(1, 4, 0.5)
print(arr9)  # [1.  1.5 2.  2.5 3. ]
arr9 = np.arange(1, 4, 0.5, dtype=np.int32)
print(arr9)  # [1 1 2 2 3]
arr9 = np.arange(1, 4, 1, dtype=np.int32)
print(arr9)  # [1 2 3]

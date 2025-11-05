
import numpy as np


# 1. 生成一个从0到9的数组
a = np.arange(10) 
print(a,type(a))

# 2. 生成一个从5到9的浮点数数组
b = np.arange(5, 10, dtype='float', step=2)
print(b)

""" 运行结果：
1. 生成一个从0到9的数组
[0 1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'>

2. 生成一个从5到9的浮点数数组
[5. 7. 9.]
"""

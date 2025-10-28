"""
4. 对象操作函数
"""


# type(), isinstance(), id(), dir()
print(type(10))  # <class 'int'>
print(isinstance(10, int))  # True
print(id(10))  # 内存地址
print(dir(str))  # 查看字符串方法

# hasattr(), getattr(), setattr()
class Test: pass
t = Test()
setattr(t, "x", 10)   # 设置属性值
print(getattr(t, "x"))  # 10 获取属性值

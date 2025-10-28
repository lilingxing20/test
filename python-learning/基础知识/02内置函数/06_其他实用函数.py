"""
6. 其他实用函数
"""

# help(), eval(), exec()
help(print)  # 查看print帮助
print(eval("2+2"))  # 4 计算字符串表达式的值
exec("x=10; print(x)")  # 10 运行字符串代码

# chr(), ord(), ascii()
print(ord("A"))  # 65 获取字符的ASCII码
print(chr(65))  # 'A' 获取ASCII码对应的字符
print(ascii("中文"))  # "'\\u4e2d\\u6587'" 获取字符串的ASCII码

# any(), all()
print(any([False, True]))  # True 任意一个为True则返回True
print(all([True, False]))  # False 所有元素都为True才返回True

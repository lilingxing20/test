""" generator 列表生成器
    生成器可以用来模拟列表的行为，但是不会占用额外的内存空间
"""

# 使用range函数生成列表
for i in range(5):
    print(i)

# 使用列表生成器
g = (x * x for x in range(5))
print(g)
print(next(g))
print(next(g))

for i in g:
    print(i)


""" 输出结果：
0
1
2
3
4
<generator object <genexpr> at 0x103099220>
0
1
4
9
16
"""

"""变量传递：按对象引用 (地址) 传递。
在Python中，函数参数传递有两种方式：值传递和引用传递。

值传递：当函数的参数为不可变类型时，如整数、浮点数、布尔值、字符串等，则传递的是变量的值。

引用传递：当函数的参数为可变类型时，如列表、字典、自定义对象等，则传递的是变量的引用（地址）。

当函数修改了参数变量的值时，由于传递的是引用，因此函数外部的变量也会受到影响。

可变类型：列表、字典、集合等。

不可变类型：整数、浮点数、布尔值、字符串等。
"""

# 不可变类型：引用传递
a = 10
b = a
c = b
print(f"a的值：{a}, 地址：{id(a)}")
print(f"b的值：{b}, 地址：{id(b)}")
print(f"c的值：{c}, 地址：{id(c)}")
a = 20
b = 30
print(f"a的值：{a}, 地址：{id(a)}")
print(f"b的值：{b}, 地址：{id(b)}")
print(f"c的值：{c}, 地址：{id(c)}")


# 可变类型：引用传递
print("可变类型：引用传递")
a = [1, 2, 3]
b = a
c = b
print(f"a的值：{a}, 地址：{id(a)}")
print(f"b的值：{b}, 地址：{id(b)}")
print(f"c的值：{c}, 地址：{id(c)}")
a.append(4)
b.append(5)
print(f"a的值：{a}, 地址：{id(a)}")
print(f"b的值：{b}, 地址：{id(b)}")
print(f"c的值：{c}, 地址：{id(c)}")


# 可变类型：值传递
print("可变类型：值传递")
a = [1, 2, 3]
b = a.copy()
c = b.copy()
print(f"a的值：{a}, 地址：{id(a)}")
print(f"b的值：{b}, 地址：{id(b)}")
print(f"c的值：{c}, 地址：{id(c)}")
a.append(4)
b.append(5)
print(f"a的值：{a}, 地址：{id(a)}")
print(f"b的值：{b}, 地址：{id(b)}")
print(f"c的值：{c}, 地址：{id(c)}")


# 值传递：
print("函数参数：值传递")
def change_value(a):
    a = 20

a = 10
change_value(a)
print(a)  # 输出：10


# 引用传递：
print("函数参数：引用传递")
def change_list(lst):
    lst.append(4)

a = [1, 2, 3]
b = a
change_list(a)
print(a)  # 输出：[1, 2, 3, 4]
print(b)  # 输出：[1, 2, 3, 4]

"""
nonlocal 关键字用于声明一个变量来自外层函数作用域（但不是全局作用域）。
"""


def inc1():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn


def inc2():
    x = 0
    def fn():
        # 声明 x 来自外层函数作用域，而非全局作用域
        nonlocal x
        x = x + 1
        return x
    return fn


if __name__ == '__main__':
    f1 = inc1()
    for i in range(4):
        print("f1: ", f1())

    f2 = inc2()
    for i in range(4):
        print("f2: ", f2())

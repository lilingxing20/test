""" 闭包的核心使用场景:
2. 函数工厂模式

闭包可以用来创建函数工厂，根据不同的参数生成不同的函数。

示例：创建不同加法器
"""


def adder_factory(x):
    def adder(y):
        return x + y
    return adder


if __name__ == '__main__':
    add_5 = adder_factory(5)
    add_10 = adder_factory(10)

    print(add_5(3))   # 输出8
    print(add_10(3))  # 输出13
    print(adder_factory(2)(3))  # 输出5

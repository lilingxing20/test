""" 闭包的核心使用场景:
1. 数据隐藏与封装
闭包可以用来隐藏数据，创建私有的变量，防止外部直接访问，实现类似面向对象中的封装特性。
示例：计数器实现
"""


def make_counter():
    count = 0  # 私有变量
    def counter():
        # 声明 count 变量来自外层函数作用域，而非全局作用域
        nonlocal count
        count += 1
        return count
    return counter


if __name__ == '__main__':
    counter = make_counter()
    print(counter())  # 输出1
    print(counter())  # 输出2
    print(counter())  # 输出3

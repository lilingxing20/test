""" 获取 generator return 返回值

1. 使用 yield 关键字，可以返回一个 generator 对象，可以迭代获取值。
2. 调用 generator 的 next() 方法，可以获取 generator 的第一个值。
3. 调用 generator 的 send() 方法，可以向 generator 发送一个值，并获取下一个值。
4. 调用 generator 的 close() 方法，可以关闭 generator。
5. 调用 generator 的 throw() 方法，可以抛出异常。
6. 调用 generator 的 __iter__() 方法，可以获取 generator 的迭代器。
7. 调用 generator 的 __next__() 方法，可以获取 generator 的下一个值。
8. 调用 generator 的 __del__() 方法，可以销毁 generator。
9. 调用 generator 的 __str__() 方法，可以打印 generator 的字符串表示。
10. 调用 generator 的 __repr__() 方法，可以打印 generator 的调试信息。
"""


def fib_generator(max):
    ret_val = []
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        ret_val.append(b)
        a, b = b, a + b
        n = n + 1
    return ret_val


def test_fib_generator():
    """
    使用for 循环调用 generator 时，是拿不到 return 的返回值的，只能通过 next() 方法获取。
    """
    print("test_fib_generator:")
    g = fib_generator(5)
    for i in g:
        print(i)


def test_fib_generator_while():
    """
    如果想要拿到 generator 的 return 返回值，必须调用next()方法获取，然后捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中。
    """
    print("test_fib_generator_while:")
    g = fib_generator(5)
    print(next(g))  # 1
    while True:
        try:
            print(next(g))
        except StopIteration as e:
            print(e.value)
            break


if __name__ == '__main__':
    test_fib_generator()
    test_fib_generator_while()


""" 运行结果：
test_fib_generator:
1
1
2
3
5
test_fib_generator_while:
1
1
2
3
5
[1, 1, 2, 3, 5]
"""

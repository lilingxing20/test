""" 创建 generator：yield
generator 是一种特殊的函数，它使用 yield 语句返回一个值，并在每次调用 next() 方法时执行。

我们可以用 yield 语句来创建 generator，语法如下：

```python
def generator_func():
    for i in range(5):
        yield i
```

在上面的代码中，generator_func() 函数是一个 generator，它会生成 0 到 4 的整数。

我们可以用 next() 方法来调用 generator，每次调用都会返回 generator 的下一个值：

```python
g = generator_func()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
```

在上面的代码中，我们用 next() 方法调用了 generator_func() 函数三次，每次都返回了 generator 的下一个值。

我们也可以用 for 循环来遍历 generator，每次循环都会调用 generator 的下一个值：

```python
g = generator_func()
for i in g:
    print(i)
```

在上面的代码中，我们用 for 循环遍历了 generator_func() 函数生成的 0 到 4 的整数。

最后，我们可以用 list() 函数将 generator 转换为列表：

```python
g = generator_func()
print(list(g))  # [0, 1, 2, 3, 4]
```

在上面的代码中，我们用 list() 函数将 generator_func() 函数生成的 0 到 4 的整数转换为列表。
"""


def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        n = n + 1
    return n

def test_fibonacci_generator():
    print("test_fibonacci_generator:")
    g = fibonacci_generator(10)
    print(next(g))  # 0
    print(next(g))  # 1
    print(next(g))  # 1
    print(next(g))  # 2

def test_fibonacci_generator_for():
    print("test_fibonacci_generator_for:")
    g = fibonacci_generator(5)
    for i in g:
        print(i)

def test_fibonacci_generator_list():
    print("test_fibonacci_generator_list:")
    g = fibonacci_generator(10)
    print(list(g))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


if __name__ == '__main__':
    test_fibonacci_generator()
    test_fibonacci_generator_for()
    test_fibonacci_generator_list()


""" 运行结果：
test_fibonacci_generator:
0
1
1
2
test_fibonacci_generator_for:
0
1
1
2
3
test_fibonacci_generator_list:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

""" doctest 模块
忽略输出:
  你可以使用 doctest.ELLIPSIS 选项来忽略输出中的某些部分。
  这在处理动态内容（如时间戳、随机数等）时非常有用。
"""

import doctest


class MyClass:
    def __repr__(self):
        """
        处理对象地址等变化信息
        >>> obj = MyClass()
        >>> repr(obj)  # doctest: +ELLIPSIS
        '<MyClass object at 0x...>'
        """
        return f"<{self.__class__.__name__} object at {hex(id(self))}>"


def get_dynamic_data():
    """
    处理动态内容

    >>> get_dynamic_data()  # doctest: +ELLIPSIS
    <object object at 0x...>
    """
    return object()


def process_data():
    """
    忽略中间输出
    >>> process_data()
    Start processing...
    Intermediate step 1
    Intermediate step 2
    Finished successfully
    """
    print("Start processing...")
    print("Intermediate step 1")
    print("Intermediate step 2")
    print("Finished successfully")


def divide(a, b):
    """
    返回两个数字的商。

    示例：
    >>> divide(10, 2)
    5.0
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return a / b


if __name__ == "__main__":
    # 如果你直接运行该脚本，它会自动执行文档测试。
    doctest.testmod(verbose=True)
    # doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)


""" 执行程序：
lixx@LixxMacPro python-learning % uv run python -m doctest exception-demo/51_doctest_test02.py --verbose
Trying:
    obj = MyClass()
Expecting nothing
ok
Trying:
    repr(obj)  # doctest: +ELLIPSIS
Expecting:
    '<MyClass object at 0x...>'
ok
Trying:
    divide(10, 2)
Expecting:
    5.0
ok
Trying:
    divide(5, 0)
Expecting:
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
ok
Trying:
    get_dynamic_data()  # doctest: +ELLIPSIS
Expecting:
    <object object at 0x...>
ok
Trying:
    process_data()
Expecting:
    Start processing...
    Intermediate step 1
    Intermediate step 2
    Finished successfully
ok
2 items had no tests:
    __main__
    __main__.MyClass
4 items passed all tests:
   2 tests in __main__.MyClass.__repr__
   2 tests in __main__.divide
   1 test in __main__.get_dynamic_data
   1 test in __main__.process_data
6 tests in 6 items.
6 passed.
Test passed.
"""

""" Docstring Tests 文档测试
Docstring Tests（文档字符串测试），是一种通过直接在文档字符串（docstring）中嵌入测试代码并通过 Python 的 doctest 模块来运行这些测试的方式。
在文档字符串中插入示例代码，并通过工具自动运行这些代码，确保代码和文档的同步性。它非常适合用来确保文档中的代码示例是可执行且正确的。

doctest 模块
doctest 模块是 Python 标准库中的一个模块，用于从文档字符串中提取并执行交互式代码片段，然后检查实际输出是否与文档中预期的输出一致。
  - 文档字符串：为函数 add 写了文档字符串，文档字符串中包含了多个示例，这些示例以 >>> 开头，并且紧跟着期望的输出结果。
  - doctest.testmod() ：
    testmod() 查找当前模块（即脚本中的所有函数和类）中的文档字符串，并执行其中的所有示例代码。
    它会验证文档字符串中的输出是否与实际代码的输出匹配。
      * 如果所有的输出匹配，默认无任何输出。
      * 如果某些示例不匹配，它会显示错误和不匹配的部分。
  - 启用详细模式: 可以通过在调用 testmod() 时传递 verbose=True 参数来启用详细模式。
    这会显示更多的信息，包括每个测试用例的输入、输出和是否通过。
  - 忽略输出
    如果你不关心某一部分输出（比如时间戳、机器生成的输出等），你可以使用 doctest.ELLIPSIS 来忽略部分输出。
"""

import doctest


def add(a, b):
    """
    返回两个数字的和。

    示例:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b


def factorial(n):
    """
    计算阶乘
    
    >>> factorial(5)
    120
    >>> factorial(1)
    1
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    # 如果你直接运行该脚本，它会自动执行文档测试。
    doctest.testmod(verbose=True)


""" 执行程序：
lixx@LixxMacPro python-learning % uv run python -m doctest exception-demo/51_doctest_test01.py --verbose
Trying:
    add(2, 3)
Expecting:
    5
ok
Trying:
    add(-1, 1)
Expecting:
    0
ok
Trying:
    add(0, 0)
Expecting:
    0
ok
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    factorial(1)
Expecting:
    1
ok
1 item had no tests:
    __main__
2 items passed all tests:
   3 tests in __main__.add
   2 tests in __main__.factorial
5 tests in 3 items.
5 passed.
Test passed.
"""

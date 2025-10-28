""" unittest 单元测试
unittest 是 Python 的标准库之一，用于编写和运行单元测试。单元测试是指对程序中的单个模块、函数或方法进行独立验证，以确保它们按预期工作。
unittest 提供了一组功能来组织测试代码，检查函数结果，并在测试失败时提供详细的报告。

断言方法
unittest 提供了一些常用的断言方法，用于验证函数或方法的输：
  - assertEqual(a, b) : 检查 a == b。
  - assertNotEqual(a, b) : 检查 a != b。
  - assertTrue(x) : 检查 x 为 True。
  - assertFalse(x) : 检查 x 为 False。
  - assertIsNone(x) : 检查 x 为 None。
  - assertIsNotNone(x) : 检查 x 不为 None。
  - assertRaises(exception, callable, *args, **kwargs) : 检查是否抛出指定的异常。

运行测试
编写一个继承自 unittest.TestCase 的类，定义测试方法。在每个测试方法前，你通常会给方法加上 test_ 前缀，以便 unittest 框架能识别它是一个测试用例。
在终端中运行测试文件时，unittest.main() 会自动发现并执行类中所有以 test_ 开头的方法：
python -m unittest 50_unittest_test01.py
"""

import unittest


# 被测试的代码
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b


# 单元测试类
class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # 断言 1 + 2 == 3

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)  # 断言 5 - 3 == 2

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)  # 断言 -1 + (-1) == -2


# 如果当前是直接运行的主程序，则直接执行 unittest.main()
if __name__ == '__main__':
    """
    unittest.main() 是 unittest 模块中的一个函数，用于自动发现并运行当前脚本中所有的测试用例。
    自动搜索所有继承自 unittest.TestCase 的类；
    自动运行所有以 test_ 开头的方法；
    在测试结束后打印出测试结果。
    """
    unittest.main()


""" 执行程序：
lixx@LixxMacPro python-learning % uv run python -m unittest exception-demo/50_unittest_test01.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""

""" 执行程序：
lixx@LixxMacPro python-learning % uv run python exception-demo/50_unittest_test01.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""

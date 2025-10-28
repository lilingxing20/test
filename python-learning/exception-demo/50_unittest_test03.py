""" 测试套件（Test Suites）
通过 unittest.TestSuite 创建一个测试套件， 并将多个测试用例添加到该套件中。
然后使用 unittest.TextTestRunner 运行该测试套件。
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

def suite():
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestMathFunctions("test_add"))
    testsuite.addTest(TestMathFunctions("test_subtract"))
    testsuite.addTest(TestMathFunctions("test_add_negative"))
    return testsuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


""" 执行程序：
lixx@LixxMacPro python-learning % uv run python -m unittest exception-demo/50_unittest_test03.py 
Setting up for a test
Cleaning up after a test
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""

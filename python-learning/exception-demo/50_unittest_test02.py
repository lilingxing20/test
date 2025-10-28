""" 设置和清理
unittest 允许在每个测试之前和之后执行一些代码。
这通常通过 setUp 和 tearDown 方法来实现：
  - setUp() ：在每个测试方法调用前执行。
  - tearDown() ：在每个测试方法调用后执行。
"""

import unittest


class TestMathFunctions(unittest.TestCase):
    
    def setUp(self):
        print("Setting up for a test")
        self.a = 1
        self.b = 2

    def tearDown(self):
        print("Cleaning up after a test")
        del self.a
        del self.b

    def test_add(self):
        result = self.a + self.b
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()


""" 执行程序：
lixx@LixxMacPro python-learning % uv run python -m unittest exception-demo/50_unittest_test02.py 
Setting up for a test
Cleaning up after a test
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""

"""
sys.argv 是获取命令行参数的基础方法，适合用于简单的命令行参数传递和处理，但如果参数较复杂（比如需要处理可选参数、类型转换、帮助信息等），argparse 会更加方便和强大。
sys.argv 是一个列表，包含了从命令行传递给 Python 脚本的所有参数。
sys.argv[0] 是脚本本身的文件名（即执行的 Python 文件）。
后续的元素（从 sys.argv[1] 开始）是传递给脚本的命令行参数。

运行示例：
python sys_argv_test01.py arg1 arg2 arg3

运行结果：
['sys_argv_test01.py', 'arg1', 'arg2', 'arg3']

说明：
    sys.argv[0] = 'example.py'（脚本文件名）
    sys.argv[1] = 'arg1'（第一个传递的参数）
    sys.argv[2] = 'arg2'（第二个传递的参数）
    sys.argv[3] = 'arg3'（第三个传递的参数）
"""

import sys
print(sys.argv)

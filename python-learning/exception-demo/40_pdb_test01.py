""" Python Debugger
pdb（Python Debugger）是 Python 内建的调试工具，用于在 Python 程序中逐步执行代码、检查变量的状态，并发现和修复错误。
pdb 允许你在代码中设置断点、查看堆栈跟踪以及修改代码状态。

常用的 pdb 调试命令
进入调试模式后，你可以使用以下命令来控制代码的执行：
  - n（next） : 执行当前行，并暂停在下一行代码。如果当前行调用了函数，n 会执行完该函数并返回到当前行。
  - s（step） : 执行当前行代码，并进入函数内部。如果当前行调用了函数，s 会进入该函数。
  - c（continue） : 继续执行代码，直到遇到下一个断点或者程序结束。
  - l（list） : 显示当前行周围的代码，帮助你查看上下文。
  - p（print） : 打印一个表达式的值。例如，p a 会显示变量 a 的值。
  - q（quit） : 退出调试器并终止程序。

进入调试模式方式：
  - 1. 在代码中插入 import pdb; pdb.set_trace() 语句。
    在你的代码中想要暂停的位置插入 pdb.set_trace() 语句，当你运行程序时，程序将在 pdb.set_trace() 处暂停并进入调试模式。
    此时，你可以在调试模式下使用一系列命令来控制程序的执行。
  - 2. 使用命令行参数启动 Python 脚本。
    你可以在运行 Python 脚本时使用 -m pdb 作为参数，这会在脚本执行前自动启动 pdb 调试器。
    例如，python -m pdb your_script.py 会在执行 your_script.py 前启动 pdb 调试器。
"""


import pdb

def add(a, b):
    result = a + b
    pdb.set_trace()  # 在此处设置断点
    return result

add(1, 2)

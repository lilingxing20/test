"""
subprocess 子进程
subprocess 模块允许你创建新的进程，连接到它们的输入/输出/错误管道，并获取它们的返回码。

subprocess 模块提供了两个函数：

- subprocess.Popen()：创建子进程，并返回一个Popen对象。
- subprocess.call()：创建子进程，等待它结束，并返回它的返回码。

下面是一个例子，演示了如何使用 subprocess.Popen() 创建一个子进程，并获取它的返回码：

在这个例子中，我们创建了一个子进程来执行 `ls -l` 命令。我们通过 `stdout=subprocess.PIPE` 和 `stderr=subprocess.PIPE` 来捕获子进程的标准输出和标准错误。然后，我们使用 `communicate()` 方法等待子进程结束，并获取它的输出和错误。最后，我们打印出输出、错误和返回码。

注意，`communicate()` 方法会阻塞当前进程，直到子进程结束。如果子进程需要很长时间才能完成，你可能需要使用 `Popen.poll()` 方法来检查子进程是否还在运行。

"""

import subprocess


# 创建子进程
process = subprocess.Popen(['date', '+%Y-%m-%d %H:%M:%S'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 等待子进程结束
stdout, stderr = process.communicate()

# 获取子进程的返回码
returncode = process.returncode

# 打印输出和错误
print("stdout:", stdout.decode())
print("stderr:", stderr.decode())
print("returncode:", returncode)

""" 执行结果：
stdout: 2023-12-24 14:45:00

stderr: 
returncode: 0
"""

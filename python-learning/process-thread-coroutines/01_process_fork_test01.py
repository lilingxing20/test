"""
fork 实现多进程
Unix/Linux操作系统提供了一个fork()系统调用，fork() 操作系统自动把当前进程（称为父进程）复制了一份（称为子进程）。
通过 fork 调用，进程在接到新任务时能派生子进程处理。Apache 服务器通过父进程监听端口，收到请求时 fork 子进程处理。
os.fork() 是一个系统调用，用于创建一个新的子进程。它在当前进程（父进程）上调用，并返回两次：
  - 在父进程中返回子进程的进程ID（PID）
  - 在子进程中返回 0,表示它是一个子进程。
"""

import os

# 打印当前进程的 PID
print(f"当前进程PID: {os.getpid()}")

# 调用os.fork 函数, 创建子进程。 在父进程中返回子进程的 PID, 在子进程中返回 0
pid = os.fork()

# 打印子进程的 PID
print(f"PID: {pid}")
# 父进程打印子进程的 PID
if pid > 0:
    print("当前进程是父进程")
    print(f"父进程创建子进程成功, fork 返回子进程PID: {pid}")
else:
    print("当前进程是子进程")
    print(f"查询当前子进程PID: {os.getpid()}")


"""执行结果：
当前进程PID: 66545
PID: 66546
当前进程是父进程
父进程创建子进程成功, fork 返回子进程PID: 66546
PID: 0
当前进程是子进程
查询当前子进程PID: 66546
"""

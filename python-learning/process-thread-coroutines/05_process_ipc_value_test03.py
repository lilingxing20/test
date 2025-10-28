"""
IPC 进程之间的通信
在 Python 中，进程间通信（Inter-Process Communication，简称 IPC）通常是指不同进程之间交换数据的机制。由于每个进程都有自己的内存空间，不能直接共享数据，因此需要使用专门的 IPC 方法来实现数据传递。
Python 提供了几种常用的进程间通信方式，主要通过 multiprocessing 模块来实现。常见的进程间通信方式包括：
  - Queue：适用于多个进程间的消息传递，支持先进先出（FIFO）的方式。
  - Pipe：适用于两个进程之间的双向通信。
  - Value 和 Array：适用于简单数据类型（如整数、浮点数）的共享内存。
  - Manager：适用于复杂的数据结构（如字典、列表等）的共享。
"""

# Value 和 Array 提供了共享内存，用于在进程之间共享数据。这种方式适用于共享基本数据类型（如整数、浮点数等）。

import multiprocessing


def worker(shared_value0):
    # 修改共享值
    shared_value0.value = 10


if __name__ == '__main__':
    # 创建了一个共享内存对象，可以在多个进程间共享数据
    shared_value = multiprocessing.Value('i', 0)

    # 创建子进程
    p = multiprocessing.Process(target=worker, args=(shared_value,))
    p.start()

    p.join()  # 等待子进程结束

    # 输出共享内存中的值
    print(shared_value.value)  # 输出 10


""" 运行结果：
10
"""

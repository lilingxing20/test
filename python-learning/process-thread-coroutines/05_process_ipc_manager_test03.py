"""
IPC 进程之间的通信
在 Python 中，进程间通信（Inter-Process Communication，简称 IPC）通常是指不同进程之间交换数据的机制。由于每个进程都有自己的内存空间，不能直接共享数据，因此需要使用专门的 IPC 方法来实现数据传递。
Python 提供了几种常用的进程间通信方式，主要通过 multiprocessing 模块来实现。常见的进程间通信方式包括：
  - Queue：适用于多个进程间的消息传递，支持先进先出（FIFO）的方式。
  - Pipe：适用于两个进程之间的双向通信。
  - Value 和 Array：适用于简单数据类型（如整数、浮点数）的共享内存。
  - Manager：适用于复杂的数据结构（如字典、列表等）的共享。
"""

# Manager 提供了一个更加灵活的共享对象机制，允许在进程间共享复杂的数据结构（如列表、字典等）。

import multiprocessing


def worker(shared_dict0):
    # 向共享字典添加数据
    shared_dict0['key'] = 'value'


if __name__ == '__main__':
    # 创建一个共享管理器，允许多个进程访问同一个对象
    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()  # 创建共享字典对象

        # 创建子进程
        p = multiprocessing.Process(target=worker, args=(shared_dict,))
        p.start()

        p.join()  # 等待子进程结束

        # 输出共享字典中的数据
        print(shared_dict)  # 输出 {'key': 'value'}


""" 运行结果：
{'key': 'value'}
"""

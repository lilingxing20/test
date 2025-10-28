"""
multiprocessing 跨平台实现多进程
multiprocessing 模块提供了一种更高级的 API 来创建和管理进程，它提供了更加灵活的进程创建方式，可以跨平台使用。

multiprocessing 模块的主要接口有两个：
  - Process：用于创建新的进程
    - Queue：用于进程间通信

multiprocessing 模块的使用步骤如下：
  - 导入 multiprocessing 模块
  - 创建 Process 对象
  - 调用 Process 对象的 start() 方法启动进程
  - 调用 Process 对象的 join() 方法等待进程结束
  - 进程执行完成后，会自动退出
  - 可以使用 Process 对象的 is_alive() 方法来检查进程是否还在运行
  - 可以使用 Process 对象的 terminate() 方法来终止进程
  - 可以使用 Process 对象的 daemon 属性来设置进程是否为守护进程
    - 守护进程会在主进程退出时自动退出
    - 非守护进程会在主进程退出时等待子进程退出
    下面是一个简单的示例：
"""

import os
import multiprocessing


def runin_process(worker):
    print(f'子进程运行中，pid: {os.getpid()}, worker: {worker}')


if __name__ == "__main__":
    # 打印主进程ID
    print("主进程ID:", os.getpid())
    # 创建子进程
    p = multiprocessing.Process(target=runin_process, args=('业务处理',))
    # 启动子进程
    print("子进程启动")
    p.start()
    # 判断子进程是否还在运行
    print("子进程是否还在运行:", p.is_alive())
    # 等待子进程结束
    print("等待子进程结束")
    p.join()
    print("子进程执行完成")

""" 执行结果
主进程ID: 74541
子进程启动
子进程是否还在运行: True
等待子进程结束
子进程运行中，pid: 74543, worker: 业务处理
子进程执行完成
"""

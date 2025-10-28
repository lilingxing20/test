"""
multiprocessing pool 进程池
multiprocessing 模块还提供了一个 Pool 类，用于创建进程池。进程池可以同时运行多个进程，并且可以方便地管理这些进程。

Pool 类的主要方法有：
  - apply(func, args=(), kwds={})：同步调用函数 func，参数为 args 和 kwds
  - apply_async(func, args=(), kwds={})：异步调用函数 func，参数为 args 和 kwds
  - map(func, iterable, chunksize=None)：将可迭代对象 iterable 中的每个元素作为参数，调用函数 func，返回结果列表
  - map_async(func, iterable, chunksize=None)：异步调用函数 func，参数为 iterable 中的每个元素，返回结果列表
  - close()：关闭进程池，防止进一步的任务提交
  - terminate()：终止进程池中的所有进程
  - join()：等待进程池中的所有进程结束

下面是一个简单的示例：
"""

import os
import multiprocessing


def runin_process(worker):
    print('Run task %s (%s)...' % (worker, os.getpid()))
    return 'Task %s runs in process %s' % (worker, os.getpid())

if __name__ == '__main__':
    # 创建进程池，指定最大进程数为 4
    pool = multiprocessing.Pool(processes=4)
    print("进程池创建成功")
    # 提交任务到进程池
    print("提交任务到进程池")
    results = []
    for i in range(5):
        results.append(pool.apply_async(runin_process, args=(i,)))
    # 关闭进程池，防止进一步的任务提交
    print("关闭进程池")
    pool.close()
    # 等待所有任务完成
    print("等待所有任务完成")
    pool.join()
    # 打印任务结果
    print("任务结果:")
    for result in results:
        print(result.get())
    # 进程池终止
    print("进程池终止")
    pool.terminate()
    print("进程池终止完成")
    # 打印进程池状态
    print("进程池状态:", pool._state)

""" 执行结果
进程池创建成功
提交任务到进程池
关闭进程池
等待所有任务完成
Run task 0 (74543)...
Run task 1 (74544)...
Run task 2 (74545)...
Run task 3 (74546)...
Run task 4 (74543)...
任务结果:
Task 0 runs in process 74543
Task 1 runs in process 74544
Task 2 runs in process 74545
Task 3 runs in process 74546
Task 4 runs in process 74543
进程池终止
进程池终止完成
进程池状态: TERMINATED
"""

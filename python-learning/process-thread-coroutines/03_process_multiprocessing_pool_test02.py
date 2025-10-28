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

import multiprocessing
import os
import random
import time


def runin_process_task(index):
    print('subprocess[%s] %s started' % (os.getpid(), index))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('subprocess[%s] %s finished in %.2f seconds' % (os.getpid(), index, end - start))


if __name__ == '__main__':
    print('parent process id is %s' % os.getpid())
    pool = multiprocessing.Pool(3)
    for i in range(5):
        pool.apply_async(runin_process_task, args=(i,))
    print('waiting all subprocess done')
    pool.close()
    pool.join()
    print('all subprocess done')

"""执行结果
parent process id is 9752
waiting all subprocess done
subprocess[9754] 0 started
subprocess[9755] 1 started
subprocess[9756] 2 started
subprocess[9754] 0 finished in 0.34 seconds
subprocess[9754] 3 started
subprocess[9756] 2 finished in 2.18 seconds
subprocess[9756] 4 started
subprocess[9755] 1 finished in 2.38 seconds
subprocess[9754] 3 finished in 2.58 seconds
subprocess[9756] 4 finished in 0.77 seconds
all subprocess done
"""

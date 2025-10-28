"""
线程（Thread）
Python提供了两个相关模块：_thread 和 threading。其中，_thread 是底层模块，而 threading 是封装了 _thread 的高级模块。绝大多数情况下，我们应优先使用 threading 模块。
"""

import threading


def runin_threading():
    print('thread[%s] started' % threading.current_thread().name)
    for i in range(5):
        print('thread[%s][%s] started' % (threading.current_thread().name, i))
    print('thread[%s] finished' % threading.current_thread().name)


if __name__ == "__main__":
    # 创建线程
    t = threading.Thread(target=runin_threading, name='TestThread')
    t.start()
    t.join()
    print('thread[%s] finished' % threading.current_thread().name)


"""执行结果
thread[TestThread] started
thread[TestThread][0] started
thread[TestThread][1] started
thread[TestThread][2] started
thread[TestThread][3] started
thread[TestThread][4] started
thread[TestThread] finished
thread[MainThread] finished
"""

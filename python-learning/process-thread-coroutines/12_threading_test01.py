"""
多核 CPU
"""

import multiprocessing
import threading


def loop():
    x = 0
    s = ""
    for i in range(10000000):
        x = x ^ 1
        s = s + str(x)
    print("thread[{}] finished".format(threading.current_thread().name))


if __name__ == '__main__':

    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop)
        print("thread[{}] started".format(t.name))
        t.start()


""" 运行结果：
thread[Thread-1 (loop)] started
thread[Thread-2 (loop)] started
thread[Thread-3 (loop)] started
thread[Thread-4 (loop)] started
thread[Thread-5 (loop)] started
thread[Thread-6 (loop)] started
thread[Thread-7 (loop)] started
thread[Thread-8 (loop)] started
thread[Thread-7 (loop)] finished
thread[Thread-1 (loop)] finished
thread[Thread-3 (loop)] finished
thread[Thread-6 (loop)] finished
thread[Thread-5 (loop)] finished
thread[Thread-8 (loop)] finished
thread[Thread-4 (loop)] finished
thread[Thread-2 (loop)] finished
"""

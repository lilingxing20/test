"""
线程锁 Lock
多线程和多进程的主要区别在于，多进程中每个进程有独立的变量拷贝，互不影响；
而多线程中，所有线程共享同一变量，因此多个线程同时修改同一变量可能导致数据混乱。
"""

import threading
import time


# 余额:
balance = 0


def add_balance(n):
    global balance
    a = balance
    # 模拟程序执行1秒
    time.sleep(1)
    balance = a + n
    print(f"余额为:{a}, 增加:{n}")


def min_balance(n):
    global balance
    a = balance
    # 模拟程序执行2秒
    time.sleep(2)
    balance = a - n
    print(f"余额为:{a}, 减少:{n}")


if __name__ == "__main__":
    t1 = threading.Thread(target=add_balance, args=(3,))
    t2 = threading.Thread(target=min_balance, args=(3,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"最终余额为: {balance}") # 结果为 0


""" 运行结果：
余额为:0, 增加:3
余额为:0, 减少:3
最终余额为: -3
"""

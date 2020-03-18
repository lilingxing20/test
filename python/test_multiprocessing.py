# -*- coding:utf-8 -*-
import multiprocessing
import time

def func(msg):
    print("msg:", msg)
    time.sleep(3)
    print("end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in range(4):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))
    pool.close()
    print("Sub-process(es) done.")
    time.sleep(100)

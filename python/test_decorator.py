#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Sun 22 Mar 2020 12:08:34 AM CST
File Name   : test_decorator.py
Description : 
'''

import time
from functools import wraps


def func_run_times1(fn):
    def _func(*args, **kv):
        start = time.time()
        ret = fn(*args, **kv)
        end = time.time()
        times = end - start
        print("The function %s completion time %s seconds." %(_func.__name__, times))
        return ret
    return _func


def func_run_times2(fn):
    @wraps(fn)
    def _func(*args, **kv):
        start = time.time()
        ret = fn(*args, **kv)
        end = time.time()
        times = end - start
        print("The function %s completion time %s seconds." %(_func.__name__, times))
        return ret
    return _func


@func_run_times1
def run1():
    print('run1 start')
    time.sleep(3)
    print('run1 end')


@func_run_times2
def run2():
    print('run2 start')
    time.sleep(3)
    print('run2 end')


if __name__ == "__main__":
    run1()
    run2()


"""
[root@lixx python]# python3 test_decorator.py 
run1 start
run1 end
The function _func completion time 3.0031375885009766 seconds.
run2 start
run2 end
The function run2 completion time 3.0031063556671143 seconds.
"""


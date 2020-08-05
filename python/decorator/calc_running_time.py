#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Sun 22 Mar 2020 09:03:07 AM CST
File Name   : calc_running_time.py
Description : 
'''

import time


def calc_running_time(fn):
    def _calc_running_time(*vargs, **kv):
        start = time.time()
        print('========== start %s' % fn.__name__)

        result = fn(*vargs, **kv)

        end = time.time()
        print('========== end %(fname)s, cost: %(cost).2f secs' %
                {'fname': fn.__name__, 'cost': end - start})
        
        return result
    return _calc_running_time

@calc_running_time
def test_func():
    print('2013-12-25')

test_func()

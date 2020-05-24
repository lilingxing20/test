#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Sun 22 Mar 2020 09:03:07 AM CST
File Name   : log_time.py
Description : 
'''

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__), end='')
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2013-12-25')

now()

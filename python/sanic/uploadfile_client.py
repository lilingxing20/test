#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Wed 25 Mar 2020 10:02:29 AM CST
File Name   : client.py
Description : 
'''

import requests


data = ""
for i in range(1, 25):
    data += str(i)
#with open('test.txt', 'w') as f:
#    f.write(data)
#
##url = 'http://127.0.0.1:8000/files'
#url = 'http://127.0.0.1:8000/stream'
#files = {
#        'file1': open('test.txt', 'rb'),
#        'file2': open('test1.txt', 'rb')
#        }
#r = requests.post(url, files=files)
#print(r.text)

#r = requests.post('http://127.0.0.1:8000/stream', data=data)
#print(r.text)
#r = requests.put('http://127.0.0.1:8000/bp_stream', data=data)
#print(r.text)
#r = requests.post('http://127.0.0.1:8000/composition_view', data=data)
#print(r.text)
r = requests.post('http://127.0.0.1:8000/method_view', data=data)
print(r.text)

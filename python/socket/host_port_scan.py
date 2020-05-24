#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Sun 24 May 2020 03:18:59 PM CST
File Name   : host_port_scan.py
Description : 先import这socket模块并且调用connect()函数去连接指定的IP地址与端口。它就会建立一个TCP连接(SYN/SYN-ACK/ACK)并且我们再通过send()函数给服务器发送一个真实的数据，然后使用recv()打印出响应的内容。
'''

import socket


host = '127.0.0.1'
host = '172.30.126.51'

s = socket.socket()

for port in range(20,25):
    try:
        print "[+] Attempting to connect to %s:%d" % (host, port)
        s.connect((host, port))
        s.send('Primal Security \n')
        banner = s.recv(1024)
        if banner:
            print "[+] Port %d open: %s" % (port, banner)
        s.close()
    except: pass

"""
[root@lixx git]# vim host_port_scan.py
[root@lixx git]# python  host_port_scan.py
[+] Attempting to connect to 127.0.0.1:20
[+] Attempting to connect to 127.0.0.1:21
[+] Attempting to connect to 127.0.0.1:22
[+] Port 22 open: SSH-2.0-OpenSSH_7.4
Protocol mismatch.

[+] Attempting to connect to 127.0.0.1:23
[+] Attempting to connect to 127.0.0.1:24
[root@lixx git]#
[root@lixx git]# vim host_port_scan.py
[root@lixx git]# python  host_port_scan.py
[+] Attempting to connect to 172.30.126.51:20
[+] Attempting to connect to 172.30.126.51:21
[+] Attempting to connect to 172.30.126.51:22
[+] Port 22 open: SSH-2.0-OpenSSH_6.6.1

[+] Attempting to connect to 172.30.126.51:23
[+] Attempting to connect to 172.30.126.51:24
"""

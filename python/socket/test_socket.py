#!/usr/bin/env python
# coding=utf-8

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Thu 24 Aug 2017 05:57:32 PM CST
File Name   : test_socket.py
Description : 
'''
import socket
s = socket.socket()

for port in range(20,30):
    try:
        print "[+] Attempting to connect to 172.0.0.1:"+str(port)
        s.connect(('127.0.0.1', port))
        s.send('Primal Security \n')    
        banner = s.recv(1024)
        if banner:
            print "[+] Port "+str(port)+" open: "+banner
        s.close()
    except: pass

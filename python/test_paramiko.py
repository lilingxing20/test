#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Fri 17 Apr 2020 10:09:27 AM CST
File Name   : test_paramiko.py
Description : 
'''

import datetime
import time
import paramiko
 
hostname = "172.16.134.33"
username = "root"
password = "Passw0rd"
cmd_list1 = ['hostname\n', 'df -h\n']
cmd_list2 = ['hostname', 'df -h']
 
# 方式一
def ssh_runcmd1(hostname, username, password, cmd_list):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #创建ssh连接
        client.connect(hostname=hostname, port=22, username=username, password=password)
        # 开启ssh管道
        ssh = client.get_transport().open_session()
        ssh.get_pty()
        ssh.invoke_shell()
        #执行指令
        for cmd in cmd_list:
            ssh.sendall(cmd)
            time.sleep(0.5)
            result = ssh.recv(102400)
            result = result.decode(encoding='UTF-8',errors='strict')
            print (result)
    except Exception as e:
        print ("[%s] %s target failed, the reason is %s" % (datetime.datetime.now(), hostname, str(e)))
    else:
        print ("[%s] %s target success" % (datetime.datetime.now(), hostname))
    finally:
        ssh.close()
        client.close()
 
# 方式二
def ssh_runcmd2(hostname, username, password, cmd_list):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #创建ssh连接
        client.connect(hostname=hostname, port=22, username=username, password=password)
        #执行指令
        for cmd in cmd_list:
            stdin, stdout, stderr = client.exec_command(cmd)
            result = stdout.read()
            result = result.decode(encoding='UTF-8',errors='strict')
            print (result)
    except Exception as e:
        print ("[%s] %s target failed, the reason is %s" % (datetime.datetime.now(), hostname, str(e)))
    else:
        print ("[%s] %s target success" % (datetime.datetime.now(), hostname))
    finally:
        client.close()
 
 
if __name__ == '__main__':
    ssh_runcmd1(hostname, username, password, cmd_list1)
    ssh_runcmd2(hostname, username, password, cmd_list2)

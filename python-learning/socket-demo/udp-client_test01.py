"""
Python 提供了 socket 模块来进行 TCP 和 UDP 的网络编程。
UDP 不需要建立连接，可以直接发送数据。
"""

import socket


# 创建 UDP 套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送数据
client_socket.sendto("你好，服务器！".encode(), ('localhost', 12345))
# 接收数据
data, server_address = client_socket.recvfrom(1024)
print(f"接收到的数据: {data.decode()} 来自: {server_address}")
# 关闭套接字
client_socket.close()

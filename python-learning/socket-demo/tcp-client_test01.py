"""
Python 提供了 socket 模块来进行 TCP 和 UDP 的网络编程。
"""

import socket


# 创建 TCP 套接字 并 连接
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
# 发送数据
client_socket.sendall("你好，服务器！".encode())
# 接收数据
data = client_socket.recv(1024)
print(f"接收到的数据: {data.decode()}")
# 关闭连接
client_socket.close()

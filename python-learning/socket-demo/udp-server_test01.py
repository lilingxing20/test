"""
Python 提供了 socket 模块来进行 TCP 和 UDP 的网络编程。
UDP 不需要建立连接，可以直接发送数据。
"""

import socket


# 创建 UDP 套接字，绑定服务器地址和端口
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("等待接收数据...")
# 接收数据
data, client_address = server_socket.recvfrom(1024)
print(f"接收到的数据: {data.decode()} 来自: {client_address}")
# 发送数据
server_socket.sendto("你好，客户端！".encode(), client_address)
# 关闭套接字
server_socket.close()

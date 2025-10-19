"""
Python 提供了 socket 模块来进行 TCP 和 UDP 的网络编程。
"""

import socket

# 创建 TCP 套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("等待客户端连接...")
# 等待客户端连接
client_socket, client_address = server_socket.accept()
print(f"客户端 {client_address} 已连接")
# 接收数据
data = client_socket.recv(1024)
print(f"接收到的数据: {data.decode()}")
# 发送数据
client_socket.sendall("你好，客户端！".encode())
# 关闭连接
client_socket.close()
server_socket.close()

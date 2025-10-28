"""
subprocess 子进程
subprocess 模块允许你创建新的进程，连接到它们的输入/输出/错误管道，并获取它们的返回码。

subprocess 模块提供了两个函数：

- subprocess.Popen()：创建子进程，并返回一个Popen对象。
- subprocess.call()：创建子进程，等待它结束，并返回它的返回码。

下面是一个例子
在Python中执行命令nslookup
```bash
set q=mx
python.org
exit
```
"""

import subprocess


# subprocess.Popen 启动一个子进程
# 1. ['nslookup']：命令和参数的列表，表示启动 nslookup。
# 2. stdin=subprocess.PIPE：允许向子进程的标准输入发送数据（即模拟键盘输入）。
# 3. stdout=subprocess.PIPE：允许从子进程的标准输出读取数据（即获取命令输出）。
# 4. stderr=subprocess.PIPE：允许从子进程的标准错误输出读取数据（即获取错误信息）。
r1 = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# communicate() 用于与子进程进行交互，发送数据到子进程的标准输入（stdin），并读取标准输出（stdout）和标准错误输出（stderr)
output, err = r1.communicate(b'set q=mx\npython.org\nexit\n')

# utf-8编码转换输出
print(f"Output: {output.decode('utf-8')}")
# stderr 为空
print(f"Error: {err.decode('utf-8')}")
# r1.returncode 获取子进程的退出状态码。如果返回值为 0，表示进程成功执行；其他值表示出错。
print(f"Exit code: {r1.returncode}")
print(f"Popen: {r1}")


""" 执行结果：
Output: Server:         198.18.0.2
Address:        198.18.0.2#53

python.org      mail exchanger = 50 mail.python.org.


Error: 
Exit code: 0
Popen: <Popen: returncode: 0 args: ['nslookup']>
"""

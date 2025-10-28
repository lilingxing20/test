""" os 模块操作文件和目录

操作系统提供了 dir、cd、cp、ls 等命令来操作文件和目录，而在Python中内置的os模块就可以直接调用操作系统提供的接口函数。

os模块主要包含以下功能：
  - os.access(path, mode): 检查文件或目录的权限，mode参数可以是r、w、x等，分别表示可读、可写、可执行。
  - os.chdir(path): 改变当前工作目录到指定的path。
  - os.listdir(path): 列出指定目录下的所有文件和目录。
  - os.mkdir(path): 创建一个新的目录。
  - os.remove(path): 删除一个文件。
  - os.rename(src, dst): 重命名文件或目录。
  - os.stat(path): 获取文件或目录的状态。
  - os.path.join(path, *paths): 将多个路径组合后返回，第一个路径可以是绝对路径也可以是相对路径。
"""

import os
import shutil


# posix：Linux、Unix或Mac OS X
# nt：Windows系统
print("OS系统平台", os.name)

# 要获取详细的系统信息
print("OS系统详细信息：", os.uname())  
# posix.uname_result(sysname='Darwin', nodename='cqqMacBook-Pro.local', release='23.4.0', version='Darwin Kernel Version 23.4.0: Fri Mar 15 00:11:05 PDT 2024; root:xnu-10063.101.17~1/RELEASE_X86_64', machine='x86_64')

# 获取系统的环境变量(操作系统中定义的环境变量，都保存在os.environ)
print("OS系统环境变量中HOME的值：", os.environ.get('HOME'))

# 获取当前目录
current_dir = os.path.dirname(__file__)
print("文件当前目录：", current_dir)

# 切换工作目录
print("OS系统切换工作目录：", current_dir)
os.chdir(current_dir)

# 获取当前目录的绝对路径
print("OS系统当前目录的绝对路径：", os.path.abspath('.'))

# 在当前目录下，创建一个新目录
a = "./test"
print("OS系统在当前目录下创建一个新目录：", a)

# 创建目录
print("OS系统创建目录：", a)
os.mkdir(a)

# 删除一个目录
print("OS系统删除目录：", a)
os.rmdir(a)

# os.path.join() 拼接的路径可正确处理不同操作系统的路径分隔符
# os.path.split() 拆分路径可正确处理不同操作系统的分割符
# os.path.split：后部分是文件或者最后一级目录
print("OS系统拆分路径：", os.path.split('./path/to/test.txt')) # ('./path/to', 'test.txt')

# os.path.splitext：后部分是文件的扩展名
print("OS系统拆分文件扩展名：", os.path.splitext('./path/to/test.txt')) # ('./path/to/test', '.txt')

# 文件重命名
print("OS系统重命名文件：", './path/to/test.txt', './path/to/new.txt')
open('./path/to/test.txt', 'w').close() # 创建文件
os.rename('./path/to/test.txt', './path/to/new.txt')

# 删除文件
print("OS系统删除文件：", './path/to/new.txt')
os.remove('./path/to/new.txt')

# 复制文件
open('./path/to/test.txt', 'w').close() # 创建文件
# shutil模块提供了copyfile()，shutil模块中有很多实用函数，可以看做是os模块的补充
print("OS系统复制文件：", './path/to/test.txt', './path/to/new.txt')
shutil.copyfile('./path/to/test.txt', './path/to/new.txt')
os.remove('./path/to/new.txt')

# 列出目录中的所有文件和目录
print("OS系统列出目录中的所有文件和目录：", os.listdir('.'))

# 过滤目录中的文件
print("OS系统过滤目录中的文件：", os.listdir('.'))
files = [x for x in os.listdir('.') if os.path.isfile(x)]
print(files)

# 过滤所有的 .py 文件
print("OS系统过滤所有的 .py 文件：", os.listdir('.'))
py_files = [x for x in os.listdir(current_dir + '/.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(py_files)


""" 运行结果：
OS系统平台 posix
OS系统详细信息： posix.uname_result(sysname='Darwin', nodename='LixxMacPro', release='25.0.0', version='Darwin Kernel Version 25.0.0: Mon Aug 25 21:17:45 PDT 2025; root:xnu-12377.1.9~3/RELEASE_ARM64_T8103', machine='arm64')
OS系统环境变量中HOME的值： /Users/lixx
文件当前目录： /Users/lixx/workspace/github/lilingxing20/test/python-learning/io-demo
OS系统切换工作目录： /Users/lixx/workspace/github/lilingxing20/test/python-learning/io-demo
OS系统当前目录的绝对路径： /Users/lixx/workspace/github/lilingxing20/test/python-learning/io-demo
OS系统在当前目录下创建一个新目录： ./test
OS系统创建目录： ./test
OS系统删除目录： ./test
OS系统拆分路径： ('./path/to', 'test.txt')
OS系统拆分文件扩展名： ('./path/to/test', '.txt')
OS系统重命名文件： ./path/to/test.txt ./path/to/new.txt
OS系统删除文件： ./path/to/new.txt
OS系统复制文件： ./path/to/test.txt ./path/to/new.txt
OS系统列出目录中的所有文件和目录： ['20_io_stringio_test01.py', 'path', '20_io_bytesio_test01.py', '30_os_file_path_test01.py', 'readme.md', '10_io_open_test01.py', 'test.txt']
OS系统过滤目录中的文件： ['20_io_stringio_test01.py', 'path', '20_io_bytesio_test01.py', '30_os_file_path_test01.py', 'readme.md', '10_io_open_test01.py', 'test.txt']
['20_io_stringio_test01.py', '20_io_bytesio_test01.py', '30_os_file_path_test01.py', 'readme.md', '10_io_open_test01.py', 'test.txt']
OS系统过滤所有的 .py 文件： ['20_io_stringio_test01.py', 'path', '20_io_bytesio_test01.py', '30_os_file_path_test01.py', 'readme.md', '10_io_open_test01.py', 'test.txt']
['20_io_stringio_test01.py', '20_io_bytesio_test01.py', '30_os_file_path_test01.py', '10_io_open_test01.py']
"""

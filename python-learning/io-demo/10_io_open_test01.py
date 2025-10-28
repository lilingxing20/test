""" open() 打开文件
如果文件不存在，open()函数就会抛出一个IOError的错误
打开文件的模式：

'r'：只读模式（默认），文件必须存在。
'w'：写模式，文件不存在时会创建，文件存在时会覆盖内容。
'a'：追加模式，文件不存在时会创建，文件存在时会在末尾追加内容。
'b'：二进制模式，适用于处理非文本文件（如图片、音频等）。
'r+'：读写模式，文件必须存在。
"""

import os


def write_file(filename, content, mode='w'):
    """写入文件内容
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    content：要写入的内容
    mode：文件打开模式，默认为写模式'w'
    返回值：None
    """
    print(f"写入文件{filename}，模式{mode}，内容{content}")
    with open(filename, mode) as file:
        file.write(content)
        file.write("\n")


def append_file(filename, content, mode='a'):
    """追加文件内容
    参数：
    """
    print(f"追加文件{filename}，模式{mode}，内容{content}")
    with open(filename, mode) as file:
        file.write(content)


def read_file(filename, mode='r'):
    """读取文件所有内容
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    mode：文件打开模式，默认为只读模式'r'
    返回值：文件所有内容
    """
    print(f"读取文件{filename}所有内容，模式{mode}")
    file = open(filename, mode)
    # content = file.read()  # 读取整个文件
    # content = file.read(10)  # 读取10个字节
    content = file.readline() # 读取一行数据
    print(content)
    file.close()


def read_file_lines(filename, mode='r'):
    """读取文件所有行
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    mode：文件打开模式，默认为只读模式'r'
    返回值：文件所有行内容
    """
    print(f"读取文件{filename}所有行，模式{mode}")
    file = open(filename, mode)
    lines = file.readlines()  # 读取所有行
    for line in lines:
        print(line.strip())  # 去掉每行末尾的换行符
    file.close()


def open_file_use_with(filename, mode='r'):
    """使用with语句打开文件
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    mode：文件打开模式，默认为只读模式'r'
    返回值：文件内容
    """
    print(f"使用with语句打开文件{filename}，模式{mode}")
    with open(filename, mode) as file:
        content = file.read()  # 读取整个文件
        print(content)
        # 不需要手动关闭文件，with语句会自动关闭


def open_big_file_use_with(filename, mode='r'):
    """使用with语句打开大文件，避免内存溢出
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    mode：文件打开模式，默认为只读模式'r'
    返回值：文件所有内容
    """
    print("使用while循环读取大文件")
    with open(filename, mode) as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())  # 去掉每行末尾的换行符
    print("使用for循环读取大文件")
    with open(filename, mode) as file:
        for line in file:
            print(line.strip())  # 去掉每行末尾的换行符


def read_binary_file(filename):
    """读取二进制文件
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    返回值：文件所有内容
    """
    print(f"读取二进制文件{filename}")
    with open(filename, 'rb') as file:
        content = file.read()
        print(content)
        # 对于二进制文件，需要使用'rb'模式打开文件，然后调用read()方法读取文件内容
        # 读取到的内容是一个字节串（bytes），需要根据具体的文件类型进行处理


def read_file_use_encoding(filename, encoding='gbk'):
    """读取文件所有内容，指定编码，处理非UTF-8编码的文件
    参数：
    filename：文件路径，可以是绝对路径或相对路径
    encoding：文件编码，默认为'gbk'
    返回值：文件所有内容
    """
    print(f"读取文件{filename}，指定编码{encoding}")
    with open(filename, 'r', encoding=encoding, errors='ignore') as file:
        content = file.read()
        print(content)
        # 对于非UTF-8编码的文件，需要指定正确的编码，否则会抛出UnicodeDecodeError错误
        # 可以使用errors='ignore'参数忽略解码错误，或者使用try-except语句处理异常


if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)  # 当前目录
    os.chdir(current_dir)                    # 切换工作目录到当前目录
    test_file = "test.txt"                   # 测试文件路径
    write_file(test_file, '第一行：这是要写入的内容')
    append_file(test_file, '第二行：这是要追加的内容')
    read_file(test_file)
    read_file_lines(test_file)
    open_file_use_with(test_file)
    open_big_file_use_with(test_file)
    read_binary_file(test_file)  # 读取二进制文件
    read_file_use_encoding(test_file, 'gbk')  # 读取GBK编码的文件


""" 运行结果：
写入文件test.txt，模式w，内容第一行：这是要写入的内容
追加文件test.txt，模式a，内容第二行：这是要追加的内容
读取文件test.txt所有内容，模式r
第一行：这是要写入的内容

读取文件test.txt所有行，模式r
第一行：这是要写入的内容
第二行：这是要追加的内容
使用with语句打开文件test.txt，模式r
第一行：这是要写入的内容
第二行：这是要追加的内容
使用while循环读取大文件
第一行：这是要写入的内容
第二行：这是要追加的内容
使用for循环读取大文件
第一行：这是要写入的内容
第二行：这是要追加的内容
读取二进制文件test.txt
b'\xe7\xac\xac\xe4\xb8\x80\xe8\xa1\x8c\xef\xbc\x9a\xe8\xbf\x99\xe6\x98\xaf\xe8\xa6\x81\xe5\x86\x99\xe5\x85\xa5\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9\n\xe7\xac\xac\xe4\xba\x8c\xe8\xa1\x8c\xef\xbc\x9a\xe8\xbf\x99\xe6\x98\xaf\xe8\xa6\x81\xe8\xbf\xbd\xe5\x8a\xa0\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9'
读取文件test.txt，指定编码gbk
绗涓琛岋細杩欐槸瑕佸啓鍏ョ殑鍐呭
绗浜岃岋細杩欐槸瑕佽拷鍔犵殑鍐呭
"""

""" 字节IO
BytesIO模块可以把内存中的字节操作看作文件操作。
"""

from io import BytesIO

def test_bytesio_write():
    """测试BytesIO的写入"""
    print('测试BytesIO的写入')
    f = BytesIO()
    f.write(b'hello')
    f.write(b' ')
    f.write(b'world')
    print(f.getvalue())  # b'hello world'


def test_bytesio_read():
    """测试BytesIO的读取"""
    print('测试BytesIO的读取')
    f = BytesIO(b'hello world')
    print(f.read(5))  # b'hello'
    print(f.read(6))  # b' world'
    print(f.read())  # b''


if __name__ == '__main__':
    test_bytesio_write()
    test_bytesio_read()


""" 输出结果：
测试BytesIO的写入
b'hello world'
测试BytesIO的读取
b'hello'
b' world'
b''
"""

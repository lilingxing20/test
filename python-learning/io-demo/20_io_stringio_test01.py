""" 字符串IO
StringIO模块可以把内存中的字符串操作看作文件操作。
"""

import io


def test_stringio_write():
    """测试StringIO的写入"""
    print('测试StringIO的写入')
    f = io.StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world')
    print(f.getvalue())  # hello world


def test_stringio_read():
    """测试StringIO的读取"""
    print('测试StringIO的读取')
    f = io.StringIO('hello world')
    print(f.read())  # hello world
    print(f.read())  # ''


if __name__ == '__main__':
    test_stringio_write()
    test_stringio_read()


""" 输出结果：
测试StringIO的写入
hello world
测试StringIO的读取
hello world
"""

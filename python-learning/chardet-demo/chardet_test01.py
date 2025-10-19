"""
chardet 是一个 Python 库，用于自动检测文本编码。它能根据字节序列推测出数据的字符编码，常用于处理来自不确定编码的文本数据，比如从网络获取的内容或读取文件时。
  1. 安装 chardet 库
     pip install chardet
  2. 使用 chardet 检测编码
     可以使用 chardet.detect() 函数检测文本的编码。该函数接受一个字节序列作为参数，返回一个字典，包含检测到的编码和置信度。
"""

import chardet


# 示例文本
text = b'Hello, World!'

# 检测编码
result = chardet.detect(text)
print(result)

# 输出示例：
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

"""
chardet 是一个 Python 库，用于自动检测文本编码。它能根据字节序列推测出数据的字符编码，常用于处理来自不确定编码的文本数据，比如从网络获取的内容或读取文件时。
  1. 安装 chardet 库
     pip install chardet
  2. 使用 chardet 检测编码
     可以使用 chardet.detect() 函数检测文本的编码。该函数接受一个字节序列作为参数，返回一个字典，包含检测到的编码和置信度。
"""

import os
import requests
import chardet


# 假设我们有一个字节串
byte_data = b'\xe4\xbd\xa0\xe5\xa5\xbd'  # 这是 "你好" 的 UTF-8 编码
result = chardet.detect(byte_data)
print(result)
""" 执行结果
{'encoding': 'utf-8', 'confidence': 0.99, 'language': 'zh'}

encoding: 检测到的编码类型
confidence: 编码的置信度（范围从 0 到 1）
language: 可能的语言（有时可能为空）
"""

# 检测文件编码
current_dir = os.path.dirname(os.path.abspath(__file__))
example_file_path = os.path.join(current_dir, 'example.txt')
with open(example_file_path, 'rb') as file:
   byte_data = file.read()
result = chardet.detect(byte_data)
print(result)

# 处理字节串
byte_data = b'\xe4\xbd\xa0\xe5\xa5\xbd'
encoding = chardet.detect(byte_data)['encoding']
decoded_data = byte_data.decode(encoding)
print(decoded_data)  # 输出 "你好"

# 以与其他库配合，比如在爬虫中判断网页的编码
response = requests.get('https://httpbin.org/get')
encoding = chardet.detect(response.content)['encoding']
text = response.content.decode(encoding)
print(text)

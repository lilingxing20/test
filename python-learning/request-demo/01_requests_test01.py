"""
requests 是一个简单易用的第三方库HTTP库，用于发送HTTP请求，提供了更简洁和强大的功能，能够更加方便地处理 URL 资源。
它支持GET、POST、PUT、DELETE等常用的HTTP方法，并且提供了丰富的功能和选项。

  1. 安装
    pip install requests
  2. request库的七个主要方法
    1) requests.get(url, params=None, **kwargs)
    2) requests.post(url, data=None, json=None, **kwargs)
    3) requests.put(url, data=None, **kwargs)
    4) requests.delete(url, **kwargs)
    5) requests.head(url, **kwargs)
    6) requests.options(url, **kwargs)
    7) requests.session()
  3. 常用参数
    1) url: 要请求的URL地址。
    2) params: 可选参数，用于在URL中传递查询参数。
    3) data: 可选参数，用于在POST请求中传递表单数据。
    4) json: 可选参数，用于在POST请求中传递JSON数据。
    5) **kwargs: 可选参数，用于传递其他HTTP请求头、超时时间等。
  4. 响应对象
    1) requests.Response对象
    2) 常用属性
      1) status_code: HTTP状态码，例如200表示成功。
      2) text: 响应内容的文本表示。
      3) json(): 响应内容的JSON表示。
      4) content: 响应内容的原始字节表示。
      5) headers: 响应头信息。

一个简单的 HTTP 请求和响应服务
  https://httpbin.org
  它提供了一些简单的接口，用于测试和调试 HTTP 请求和响应。
  例如：
    - GET 请求：https://httpbin.org/get
    - POST 请求：https://httpbin.org/post
    - PUT 请求：https://httpbin.org/put
    - DELETE 请求：https://httpbin.org/delete
    - HEAD 请求：https://httpbin.org/head
    - OPTIONS 请求：https://httpbin.org/options
"""

import os
import requests


# 1. 测试不同的 HTTP 方法
print("1. 测试不同的 HTTP 方法")
## 1.1 发送 GET 请求
print("1.1 发送 GET 请求")
response = requests.get('https://httpbin.org/get')
print(response.status_code)  # 状态码
print(response.json())  # 返回的内容

## 1.2 发送 POST 请求
print("1.2 发送 POST 请求")
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.status_code)
print(response.json())  # 如果返回的是 JSON 数据

## 1.3 发送 PUT 请求
print("1.3 发送 PUT 请求")
data = {'key': 'value'}
response = requests.put('https://httpbin.org/put', data=data)
print(response.status_code)
print(response.json())

## 1.4 发送 PATCH 请求
print("1.4 发送 PATCH 请求")
data = {'key': 'value'}
response = requests.patch('https://httpbin.org/patch', data=data)
print(response.status_code)
print(response.json())

## 1.5 发送 DELETE 请求
print("1.5 发送 DELETE 请求")
response = requests.delete('https://httpbin.org/delete')
print(response.status_code)
print(response.json())


# 2. 检查请求数据
print("2. 检查请求数据")
## 2.1 检查 请求 HEAD
print("2.1 检查 请求 HEAD")
headers = {'User-Agent': 'my-app'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())

## 2.2 检查 请求 Agent
print("2.2 检查 请求 Agent")
response = requests.get('https://httpbin.org/user-agent')
print(response.status_code)
print(response.json())

## 2.3 检查 请求 IP
print("2.3 检查 请求 IP")
response = requests.get('https://httpbin.org/ip')
print(response.status_code)
print(response.json())


# 3. 生成随机和动态数据
print("3. 生成随机和动态数据")
## 3.1 处理超时
try:
    response = requests.get('https://httpbin.org/delay/5', timeout=3)
except requests.exceptions.Timeout:
    print('Request timed out')


# 4. 上传文件
print("4. 上传文件")
## 4.1 创建测试文件
current_dir = os.path.dirname(os.path.abspath(__file__))
test_file_path = os.path.join(current_dir, 'test.txt')
with open(test_file_path, 'w') as f:
    f.write('Hello, World!')

## 4.2 上传测试文件
# 'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
files = {'file': open(test_file_path, 'rb')}  
response = requests.post('https://httpbin.org/post', files=files)
print(response.json())

## 4.3 处理cookies
cookies = {'session_id': '123456'}
response = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(response.json())

## 4.4 自定义认证
from requests.auth import HTTPBasicAuth
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=HTTPBasicAuth('user', 'pass'))
print(response.status_code)

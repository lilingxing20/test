"""
urllib 提供了用于操作 URL（Uniform Resource Locator）以及网络请求的功能。
urllib 模块的主要作用是处理 HTTP 请求、解析和构建 URL，以及进行编码和解码操作。
urllib 模块是 Python 标准库中的一个模块，用于处理 URL。
  1. 安装
    无需安装，Python 标准库中已经包含了 urllib 模块。
  2. 常用函数
    1) urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, *, cafile=None, capath=None, cadefault=False, context=None)
      用于打开一个 URL 地址，返回一个文件对象。
      参数：
        url: 要打开的 URL 地址。
        data: 可选参数，用于在 POST 请求中传递表单数据。
        timeout: 可选参数，指定超时时间，默认值为 socket._GLOBAL_DEFAULT_TIMEOUT。
        cafile, capath, cadefault, context: 可选参数，用于指定 SSL 证书验证相关的参数。
    2) urlretrieve(url, filename=None, reporthook=None, data=None)
      用于从 URL 地址下载文件到本地。
      参数：
        url: 要下载的 URL 地址。
        filename: 可选参数，指定保存的文件名。
        reporthook: 可选参数，用于指定下载进度回调函数。
        data: 可选参数，用于在 POST 请求中传递表单数据。

urllib 模块的子模块：
  1) urllib.request
    用于处理 URL 请求，包括打开 URL、发送请求、处理响应等。
  2) urllib.parse
    用于解析和构建 URL，包括 URL 编码、解码、拆分、合并等。
  3) urllib.error
    用于处理 URL 请求过程中可能出现的错误，包括网络错误、HTTP 错误等。
  4) urllib.robotparser
    用于解析 robots.txt 文件，用于判断是否允许访问某个 URL。
  5) urllib.response
    用于处理 URL 请求的响应，包括读取响应内容、解析响应头等。
"""

from urllib import request


# 1. 测试不同的 HTTP 方法
## 1.1 发送 GET 请求
print("1.1 发送 GET 请求")
req = request.urlopen('http://httpbin.org/get')
with req as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")


## 1.2 发送 POST 请求
print("1.2 发送 POST 请求")
req = request.urlopen('http://httpbin.org/post', data=b'key=value')
with req as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")


## 1.3 发送 PUT 请求
print("1.3 发送 PUT 请求")
req = request.Request('http://httpbin.org/put', data=b'key=value', method='PUT')
with request.urlopen(req) as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")


## 1.4 发送 PATCH 请求
print("1.4 发送 PATCH 请求")
req = request.Request('http://httpbin.org/patch', data=b'key=value', method='PATCH')
with request.urlopen(req) as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")


## 1.5 发送 DELETE 请求
print("1.5 发送 DELETE 请求")
req = request.Request('http://httpbin.org/delete', data=b'key=value', method='DELETE')
with request.urlopen(req) as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")


# 2. 检查请求数据
print("2. 检查请求数据")
## 2.1 检查 请求 HEAD
print("2.1 检查 请求 HEAD")
req = request.Request('http://httpbin.org/headers', data=b'key=value', method='HEAD')
with request.urlopen(req) as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")

## 2.2 检查 请求 IP
print("2.2 检查 请求 IP")
req = request.Request('http://httpbin.org/ip', data=b'key=value', method='GET')
with request.urlopen(req) as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")


## 2.3 检查 Agent
print("2.3 检查 Agent")
req = request.Request('http://httpbin.org/user-agent', data=b'key=value', method='GET')
with request.urlopen(req) as response:
    print(f"Status: {response.status} {response.reason}")
    for k, v in response.getheaders():
        print(f"{k}:{v}")
    print(f"Response Content: {response.read().decode('utf-8')}")

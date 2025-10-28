"""
asyncio的异步网络连接来获取sina、sohu和163的网站首页
"""

import asyncio


async def wget(host):
    print(f"wget {host}...")
    # 连接80端口:
    reader, writer = await asyncio.open_connection(host, 80)
    # 发送HTTP请求:
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode("utf-8"))
    # 等待直到缓冲区数据被完全发送
    await writer.drain()

    # 读取HTTP响应:
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()
    print(f"Done {host}.")


async def main():
    await asyncio.gather(wget("www.sina.com.cn"), wget("www.sohu.com"), wget("www.163.com"))


if __name__ == "__main__":
    asyncio.run(main())


""" 运行结果：
wget www.sina.com.cn...
wget www.sohu.com...
wget www.163.com...
www.sina.com.cn header > HTTP/1.1 302 Found
www.sina.com.cn header > Server: Tengine
www.sina.com.cn header > Date: Sat, 25 Oct 2025 15:39:34 GMT
www.sina.com.cn header > Content-Type: text/html
www.sina.com.cn header > Content-Length: 242
www.sina.com.cn header > Connection: close
www.sina.com.cn header > Location: https://www.sina.com.cn/
www.sina.com.cn header > X-DSL-CHECK: 5
www.sina.com.cn header > X-Via-CDN: f=aliyun,s=ens-cache26.cn8437,c=180.213.214.102;
www.sina.com.cn header > Via: ens-cache26.cn8437[,0]
www.sina.com.cn header > Timing-Allow-Origin: *
www.sina.com.cn header > EagleId: 6fe3772e17614067743755332e
Done www.sina.com.cn.
www.163.com header > HTTP/1.1 403 Forbidden
www.163.com header > Server: Tengine
www.163.com header > Date: Sat, 25 Oct 2025 15:39:34 GMT
www.163.com header > Content-Type: text/html; charset=utf-8
www.163.com header > Content-Length: 311
www.163.com header > Connection: close
www.163.com header > X-Tengine-Error: denied by UA ACL = blacklist
www.163.com header > cache_control: no-cache, no-store
www.163.com header > Pragma: no-cache
www.163.com header > Cache-Control: no-cache,no-store,private
www.163.com header > cdn-user-ip: 180.213.214.102
www.163.com header > cdn-source: Ali
www.163.com header > cdn-ip: 144.7.85.84
www.163.com header > Via: cache8.cn8800[,403011]
www.163.com header > Timing-Allow-Origin: *
www.163.com header > EagleId: 9007551c17614067743878672e
Done www.163.com.
www.sohu.com header > HTTP/1.1 302 Found
www.sohu.com header > Location: https://www.sohu.com/
www.sohu.com header > Content-Length: 0
www.sohu.com header > X-NWS-LOG-UUID: 10272627142140067618
www.sohu.com header > Connection: close
www.sohu.com header > Server: D0
www.sohu.com header > Date: Sat, 25 Oct 2025 15:39:34 GMT
www.sohu.com header > X-Cache-Lookup: Return Directly
Done www.sohu.com.
"""

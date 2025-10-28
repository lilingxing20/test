"""
aiohttp 异步HTTP客户端
asyncio 可以实现单线程并发 I/O 操作，特别适用于服务器端的高并发支持，如 Web 服务器。它支持 TCP、UDP、SSL 等协议。
aiohttp 是基于 asyncio 实现的 HTTP 框架。

示例：定义处理不同URL的async函数，通过app.add_routes()添加映射，最后通过run_app()以asyncio的机制启动整个处理流程。
"""

from aiohttp import web


async def index(request):
    text = "<h1>Index Page</h1>"
    return web.Response(text=text, content_type="text/html")


async def hello(request):
    name = request.match_info.get("name", "World")
    text = f"<h1>Hello, {name}</h1>"
    return web.Response(text=text, content_type="text/html")


# 创建web应用对象:
app = web.Application()
# 添加路由:
app.add_routes([
    web.get('/', index),
    web.get('/{name}', hello)
    ])


if __name__ == "__main__":
    # 启动服务:
    web.run_app(app)


""" 运行结果：
启动服务后，访问 http://localhost:8080/ 即可看到首页内容: Index Page
访问 http://localhost:8080/liming 即可看到问候内容: Hello, liming
"""

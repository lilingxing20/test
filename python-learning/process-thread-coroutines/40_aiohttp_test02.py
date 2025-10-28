"""
测试aiohttp异步请求，同时获取python官网首页标题和python社区首页标题，并发执行两个请求
"""

import aiohttp
import asyncio


async def fetch_title(session, url):
    async with session.get(url) as response:
        html = await response.text()
        title = html.split('<title>')[1].split('</title>')[0]
        return title


async def main():
    async with aiohttp.ClientSession() as session:
        # 并发执行两个请求
        python_org_title_task = fetch_title(session, 'http://python.org')
        python_community_title_task = fetch_title(session, 'https://www.python.org/community/')
        # 等待两个请求完成
        python_org_title, python_community_title = await asyncio.gather(
            python_org_title_task,
            python_community_title_task
        )
        # 打印结果
        print(python_org_title)
        print(python_community_title)


if __name__ == '__main__':
    asyncio.run(main())


""" 运行结果：
Welcome to Python.org
Our Community | Python.org
"""

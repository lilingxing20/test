#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Wed 08 Apr 2020 04:05:09 PM CST
File Name   : test_sanic_01.py
Description : 异步非阻塞
'''

from sanic import Sanic, response
import asyncio
import uvloop

app = Sanic('async demo')


async def task_sleep():
    print('sleep before')
    await asyncio.sleep(5)
    print('sleep after')


@app.route("/")
async def test(request):
    print(request.app.loop)
    myloop = request.app.loop
    myloop.create_task(task_sleep())
    # task = request.app.loop.create_task(task_sleep())
    return response.json({"hello": "body"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

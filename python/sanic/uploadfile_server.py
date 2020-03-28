#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Wed 25 Mar 2020 10:01:13 AM CST
File Name   : server.py
Description : 
'''

from sanic import Sanic
from sanic.views import CompositionView
from sanic.views import HTTPMethodView
from sanic.views import stream as stream_decorator
from sanic.blueprints import Blueprint
from sanic.response import stream, text

bp = Blueprint('blueprint_request_stream')
app = Sanic('request_stream')


# 1
@app.post('/files')
async def files_handler(request):
    async def files(response):
        for file in request.files.keys():
            while True:
                body = await request.files.get("")
                if body is None:
                    break
                print(len(body))
                body = body.decode('utf-8').replace('1', 'A')
                await response.write(body)
    return stream(files)


# 2
@app.post('/stream', stream=True)
async def stream_handler(request):
    async def streaming(response):
        while True:
            body = await request.stream.read()
            if body is None:
                break
            print(len(body))
            body = body.decode('utf-8').replace('1', 'A')
            await response.write(body)
    return stream(streaming)


# 3
@bp.put('/bp_stream', stream=True)
async def bp_handler(request):
    result = ''
    while True:
        body = await request.stream.read()
        if body is None:
            break
        print(len(body))
        result += body.decode('utf-8').replace('1', 'B')
    return text(result)

app.blueprint(bp)


# 4
async def post_handler(request):
    result = ''
    while True:
        body = await request.stream.read()
        if body is None:
            break
        print(len(body))
        result += body.decode('utf-8')
    return text(result)

view = CompositionView()
view.add(['POST'], post_handler, stream=True)
app.add_route(view, '/composition_view')


# 5
class SimpleView(HTTPMethodView):

    @stream_decorator
    async def post(self, request):
        result = ''
        while True:
            body = await request.stream.read()
            if body is None:
                break
            result += body.decode('utf-8')
        return text(result)

app.add_route(SimpleView.as_view(), '/method_view')


# print router
for k,v in app.router.routes_names.items():
    print(v[-1].uri)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

# --*-- coding: utf-8 --*--
# author: lixx
# email: lilingxing20@163.com

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'


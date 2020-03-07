#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx (https://github.com/lilingxing20)
Created Time: Sat Mar  7 12:03:54 2020
File Name   : demo2.py
Description : 
'''

from wsgiref.simple_server import make_server


def index():
    data = open('html/index.html').read()
    return data

def hello():
    data = '<html>hello</html>'
    return data

def RunServer(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    request_url = environ['PATH_INFO']

    url_list=[
        ('/hello',hello),
        ('/index',index),
    ]

    for url in url_list:
        if request_url == url[0]:
            return url[1]()
    else:
        return "404"


if __name__ == '__main__':
    httpd = make_server('',8000,RunServer)
    print "Server HTTP on port 8000..."
    httpd.serve_forever()

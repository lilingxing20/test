#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Author      : lixx
Created Time: Mon Sep 29 23:26:23 2025
File Name   : test.py
Description : 
'''

from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/<string:arg>')
def demo(arg):
    """示例接口
    ---
    parameters:
      - name: arg
        in: path
        type: string
        required: true
    responses:
      200:
        description: 成功响应
    """
    return {'data': arg}

if __name__ == '__main__':
    app.run(port=8021)


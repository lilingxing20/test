# -*- coding:utf-8 -*-

"""
简单的测试脚本，用于验证Sanic应用是否正常工作
"""

from sanic import Sanic
from sanic.response import json


app = Sanic("test_app")


@app.route("/")
async def test(request):
    return json({"message": "Sanic is working!"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
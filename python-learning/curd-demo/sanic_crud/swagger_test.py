#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Swagger测试脚本
用于验证Sanic应用的Swagger本地部署配置是否正常工作
"""

from tokenize import Ignore
from sanic import Sanic
from sanic.response import file, json
from sanic_ext import openapi

# 创建应用实例
app = Sanic("swagger_test")

# 配置Swagger使用本地资源
import os
def get_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir

# 设置默认UI为swagger
app.config.OAS_UI_DEFAULT = "swagger"
# 设置swagger html文件路径
app.config.OAS_PATH_TO_SWAGGER_HTML = get_root() + "/docs/swagger/swagger.html"
# 设置redoc html文件路径
app.config.OAS_PATH_TO_REDOC_HTML = get_root() + "/docs/redoc/redoc.html"
# 配置swagger-ui
app.config.SWAGGER_UI_CONFIGURATION = {
    "defaultModelsExpandDepth": -1,
    "docExpansion": "none"
}

# 配置静态文件路由
# app.static('/docs', get_root() + '/docs')
app.static('/static', get_root() + '/static')

# 添加swagger资源路由
@app.get("/swagger-src/<file_name>")
@openapi.tag("Swagger资源")
@openapi.description("获取Swagger资源文件")
@openapi.parameter("file_name", str, "path", required=True, description="资源文件名")
async def swagger_template_file(request, file_name):
    file_path = get_root() + "/docs/swagger/" + file_name
    return await file(file_path)


# 添加redoc资源路由
@app.get("/redoc-src/<file_name>")
@openapi.tag("ReDoc资源")
@openapi.description("获取ReDoc资源文件")
@openapi.parameter("file_name", str, "path", required=True, description="资源文件名")
async def redoc_template_file(request, file_name):
    file_path = get_root() + "/docs/redoc/" + file_name
    return await file(file_path)


# 添加一个测试接口，用于验证API文档
@app.get("/api/test")
@openapi.tag("API接口")
@openapi.description("测试接口")
@openapi.parameter("name", str, "query", required=False, description="测试参数")
@openapi.response(200, {"type": "object", "properties": {"data": {"type": "string"}, "message": {"type": "string"}}}, "成功响应")
async def test_api(request):
    name = request.args.get('name', 'World')
    return json({
        "data": name,
        "message": "Hello, " + name
    })


if __name__ == '__main__':
    # 启动应用
    print("Starting Sanic app with local Swagger UI...")
    print(f"Swagger UI docs: http://127.0.0.1:8022/docs")
    print(f"Swagger UI swagger: http://127.0.0.1:8022/docs/swagger")
    print(f"Swagger UI redoc: http://127.0.0.1:8022/docs/redoc")
    app.run(host="127.0.0.1", port=8022, debug=True, auto_reload=True)

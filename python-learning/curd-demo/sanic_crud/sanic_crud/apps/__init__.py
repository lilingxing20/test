# -*- coding:utf-8 -*-

from sanic import Sanic
from sanic.response import file
from sanic_cors import CORS
from sanic_ext import Extend
from sanic_ext import openapi
import os

from apps.controller import register_blueprint
from extends import register_extends


# 创建instance目录的函数
def create_instance_dir():
    """
    创建instance目录用于存放SQLite数据库文件
    """
    import os
    instance_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'instance')
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)


def get_root():
    """
    获取项目根目录
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(current_dir))
    return root_dir


def create_app():
    """
    创建Sanic应用实例
    """
    # 创建instance目录
    create_instance_dir()
    
    # 创建Sanic对象
    app = Sanic("sanic_crud")
    
    # 配置应用
    app.config.FALLBACK_ERROR_FORMAT = "json"

    # OpenAPI配置 
    app.config.OAS_AUTODOC = True
    app.config.OAS_IGNORE_OPTIONS = False
    # 配置Sanic Extensions - 解决内网环境swagger打不开的问题
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


    # 配置静态文件路由
    # app.static('/docs', get_root() + '/docs')
    app.static('/static', get_root() + '/static')

    # 初始化Sanic Extensions
    Extend(app, 
           openapi={
               "version": "1.0.0",
               "title": "Sanic CRUD API",
               "description": "Sanic CRUD API接口文档",
               "contact": {
                   "name": "API Support",
                   "url": "http://example.com/support",
                   "email": "support@example.com"
               },
               "license": {
                   "name": "MIT",
                   "url": "https://opensource.org/licenses/MIT"
               }
           })
    
    # 跨域处理
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True) 
    # CORS高级配置
    app.config.CORS_SUPPORTS_CREDENTIALS = True
    app.config.CORS_MAX_AGE = 3600
    
    # 依赖注入配置
    app.config.INJECTION_SKIP_NONE = True

    # 初始化扩展（数据库等）
    register_extends()
    
    # 注册蓝图
    register_blueprint(app)
    
    # 返回APP
    return app

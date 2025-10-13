# -*- coding:utf-8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

# 修复导入路径
from fastapi_crud.apps.controller import register_router
from fastapi_crud.extends.extends_sqlalchemy import engine, Base


def create_app():
    """创建FastAPI应用实例"""
    # 创建FastAPI对象 - 禁用自动文档
    app = FastAPI(
        title="FastAPI CURD 示例",
        description="基于FastAPI的CRUD示例应用",
        version="1.0.0",
        docs_url=None,  # 禁用默认Swagger UI
        redoc_url=None  # 禁用默认ReDoc
    )
    
    # 配置跨域中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 挂载静态文件目录 - 适配内网环境
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    # 注册自定义Swagger UI路由 - 使用本地静态文件
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
            swagger_favicon_url="/static/favicon.png",
        )

    # 注册OAuth2重定向路由
    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()
    
    # 注册自定义ReDoc路由 - 使用本地静态文件
    @app.get("/redoc", include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title=app.title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
        )
    
    # 注册路由
    register_router(app)
    
    # 初始化数据库（创建表）
    init_database()
    
    return app


def init_database():
    """初始化数据库，创建所有表"""
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        print("数据库表创建成功")
    except Exception as e:
        print(f"数据库表创建失败：{str(e)}")


def custom_openapi(app: FastAPI):
    """自定义OpenAPI文档"""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# -*- coding:utf-8 -*-

from fastapi import FastAPI

# 修复导入路径
from fastapi_crud.apps.controller.role import role_router


def register_router(app: FastAPI):
    """注册所有路由"""
    # 注册角色路由
    app.include_router(role_router)
    print("注册路由成功")
    return True
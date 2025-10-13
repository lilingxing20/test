# -*- coding:utf-8 -*-

from .role import role_bp


# 注册路由
def register_blueprint(app):
    """
    注册所有蓝图
    """
    # 角色模块
    app.blueprint(role_bp)
    print("注册路由成功")
    return True
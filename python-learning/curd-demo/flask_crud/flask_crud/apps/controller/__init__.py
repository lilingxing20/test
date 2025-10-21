from apps.controller.role import role_blue
from apps.controller.render import render_blue


def register_blueprint(app):
    """
    注册路由
    """
    # 角色模块
    app.register_blueprint(role_blue)
    # 渲染模块
    app.register_blueprint(render_blue)
    print("注册路由")
    return True

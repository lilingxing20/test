# -*- coding:utf-8 -*-

from apps import create_app
from config.env import SANIC_HOST, SANIC_PORT, SANIC_DEBUG


# 创建应用实例
app = create_app()


if __name__ == '__main__':
    # 启动应用
    print(f"应用启动地址：http://{SANIC_HOST}:{SANIC_PORT}/docs/swagger")
    app.run(host=SANIC_HOST, port=SANIC_PORT, debug=SANIC_DEBUG, auto_reload=True)

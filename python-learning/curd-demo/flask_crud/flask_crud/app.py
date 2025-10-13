# -*- coding:utf-8 -*-

from apps import create_app, create_swagger
from config.env import FLASK_HOST, FLASK_PORT, FLASK_DEBUG


# 创建应用实例
app = create_app()
# SwaggeUI配置
swagger = create_swagger(app)


if __name__ == '__main__':
    # 启动应用
    print(f"应用启动地址：http://{FLASK_HOST}:{FLASK_PORT}/apidocs")
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)

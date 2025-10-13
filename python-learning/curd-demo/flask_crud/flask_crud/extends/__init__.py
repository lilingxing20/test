from config.env import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_DATABASE
from extends.extends_sqlalchemy import db

# 注册扩展(扩展初始化)
def register_extends(app):
    # 配置数据库
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/flask_crud.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # 初始化数据库
    with app.app_context():
        print("初始化数据库")
        db.init_app(app)
        # db.drop_all()
        db.create_all()
    return app

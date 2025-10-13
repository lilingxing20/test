# -*- coding:utf-8 -*-

from .extends_sqlalchemy import init_db, get_db, Base
from config.env import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_DATABASE


# 注册扩展(扩展初始化)
def register_extends():
    """
    初始化数据库连接
    """
    # 配置数据库连接字符串
    # 这里使用SQLite作为默认数据库，与Flask版本保持一致
    # database_uri = "sqlite:///../instance/sanic_crud.db"
    # 但也提供MySQL连接的配置，注释掉的部分是MySQL连接
    database_uri = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4"
    
    # 初始化数据库
    engine, SessionLocal = init_db(database_uri)
    print("初始化数据库成功")
    
    return engine, SessionLocal
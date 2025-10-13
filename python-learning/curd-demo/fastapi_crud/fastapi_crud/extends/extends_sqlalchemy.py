# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

# 修复导入路径
from fastapi_crud.config.env import DB_DRIVER, DB_HOST, DB_PORT, DB_DATABASE, DB_USERNAME, DB_PASSWORD, DB_DEBUG

# 数据库连接配置
if DB_DRIVER == "sqlite":
    DATABASE_URL = f"sqlite:///{DB_DATABASE}"
else:
    DATABASE_URL = f"{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# 创建SQLAlchemy引擎
echo = DB_DEBUG  # 是否输出SQL语句
if DB_DRIVER == "sqlite":
    # SQLite特殊配置
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},  # SQLite多线程配置
        echo=echo
    )
else:
    # 其他数据库配置
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=1800,
        echo=echo
    )

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础模型类
Base = declarative_base()


# 获取数据库会话
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
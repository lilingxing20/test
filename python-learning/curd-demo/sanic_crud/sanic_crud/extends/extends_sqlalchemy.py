# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 创建基础模型类
Base = declarative_base()

# 数据库会话工厂
SessionLocal = None

# 数据库引擎
engine = None


def init_db(database_uri):
    """
    初始化数据库连接
    """
    global engine, SessionLocal
    engine = create_engine(database_uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    return engine, SessionLocal


def get_db():
    """
    获取数据库会话
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
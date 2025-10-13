# -*- coding:utf-8 -*-

import os


# 应用运行地址
FASTAPI_HOST = os.getenv('FASTAPI_HOST', '127.0.0.1')
# 应用运行端口
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT', 8023))
# 是否调试模式：是-True,否-False
FASTAPI_DEBUG = (os.getenv('FASTAPI_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
FASTAPI_DEMO = (os.getenv('FASTAPI_DEMO', 'True') == 'True')

# =============================================== 数据库配置 =================================================

# 数据库驱动 - 改为SQLite以简化开发环境配置
DB_DRIVER = os.getenv('DB_DRIVER', 'sqlite')
# 数据库地址（SQLite忽略）
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
# 数据库端口（SQLite忽略）
DB_PORT = os.getenv('DB_PORT', 3306)
# 数据库名称 - SQLite时为数据库文件路径
DB_DATABASE = os.getenv('DB_DATABASE', 'py_crud.db')
# 数据库账号（SQLite忽略）
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
# 数据库密码（SQLite忽略）
DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')
# 数据表前缀
DB_PREFIX = os.getenv('DB_PREFIX', 'fastapi_')
# 是否开启调试模式：是-True,否-False
DB_DEBUG = (os.getenv('DB_DEBUG', 'True') == 'True')

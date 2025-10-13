# -*- coding:utf-8 -*-

import os


# 应用运行地址
SANIC_HOST = os.getenv('SANIC_HOST', '127.0.0.1')
# 应用运行端口
SANIC_PORT = int(os.getenv('SANIC_PORT', 8022))
# 是否调试模式：是-True,否-False
SANIC_DEBUG = (os.getenv('SANIC_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
SANIC_DEMO = (os.getenv('SANIC_DEMO', 'True') == 'True')

# =============================================== 数据库配置 =================================================

# 数据库驱动
DB_DRIVER = os.getenv('DB_DRIVER', 'mysql')
# 数据库地址
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
# 数据库端口
DB_PORT = int(os.getenv('DB_PORT', 3306))
# 数据库名称
DB_DATABASE = os.getenv('DB_DATABASE', 'py_crud')
# 数据库账号
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
# 数据库密码
DB_PASSWORD = os.getenv('DB_PASSWORD', '123456')
# 数据表前缀
DB_PREFIX = os.getenv('DB_PREFIX', 'sanic_')
# 是否开启调试模式：是-True,否-False
DB_DEBUG = (os.getenv('DB_DEBUG', 'True') == 'True')
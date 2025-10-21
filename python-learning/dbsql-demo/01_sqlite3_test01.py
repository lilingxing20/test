"""
SQLite是一种嵌入式数据库，其数据库存储为单个文件。
由于SQLite由C语言编写且体积小，常被集成到各种应用中，包括iOS和Android应用。
Python内置SQLite3模块，无需安装。
"""
import os
import sqlite3


# 当前目录下创建sqlite3.db数据库文件
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'sqlite3.db')
if not os.path.exists(db_path):
    open(db_path, 'w').close()

# 连接数据库
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -- 其他字段...
)
''')

# 插入数据
cursor.execute("INSERT INTO users (name, age, email, phone, address) VALUES ('王林', 30, 'wanglin@example.com', '13800000000', '北京市海淀区')")
cursor.execute("INSERT INTO users (name, age, email, phone, address) VALUES ('李慕婉', 25, 'liuyun@example.com', '13900000000', '上海市浦东新区')") 
connection.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 更新数据
cursor.execute("UPDATE users SET age = 26 WHERE name = '王林'")
connection.commit()

# 删除数据
cursor.execute("DELETE FROM users WHERE name = '李慕婉'")
connection.commit()

# 查询数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

# 关闭连接
cursor.close()
connection.close()

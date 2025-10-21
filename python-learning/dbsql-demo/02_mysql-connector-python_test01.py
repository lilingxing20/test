"""
在Python中连接和操作MySQL数据库，通常使用第三方库mysql-connector-python(Mysql 官网提供)或PyMySQL
    1. 安装mysql-connector-python库
        pip install mysql-connector-python
    2. 导入库
        import mysql.connector
    3. 连接数据库
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='test'
        )
    4. 创建游标
        cursor = connection.cursor()
    5. 执行SQL语句
        cursor.execute("SELECT * FROM users")
    6. 提交事务
        connection.commit()
    7. 关闭游标和连接
        cursor.close()
        connection.close()
"""

import mysql.connector


# 连接到MySQL数据库
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="test",
    port=3306
)

# 创建游标
cursor = connection.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    email VARCHAR(255),
    phone VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# 插入数据
cursor.execute("INSERT INTO users (name, age, email, phone, address) VALUES (%s, %s, %s, %s, %s)", ("李慕婉", 30, "lixx@example.com", "13800000000", "北京市海淀区"))
cursor.execute("INSERT INTO users (name, age, email, phone, address) VALUES (%s, %s, %s, %s, %s)", ("王林", 25, "wanglin@example.com", "13900000000", "北京市朝阳区"))
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

# 关闭游标和连接
cursor.close()
connection.close()

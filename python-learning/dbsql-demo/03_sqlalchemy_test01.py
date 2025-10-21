"""
SQLAlchemy 是一个强大的 Python ORM（对象关系映射）库。使得你可以通过 Python 对象来表示数据库中的数据，而不是直接写 SQL 语句。
    - SQLAlchemy Core：是一个低级别的库，提供了与数据库的直接交互和 SQL 构建的能力。它使用的是 SQL 表达式语言，可以手动构建和执行 SQL 查询。
    - SQLAlchemy ORM：是一个高级的 ORM（对象关系映射）工具，提供了将 Python 类与数据库表进行映射的功能。它使得我们能够通过类和对象来操作数据库，而无需手写 SQL。

1. 安装 SQLAlchemy：
    - 你可以使用 pip 安装 SQLAlchemy：`pip install sqlalchemy`
2. 导入 SQLAlchemy：
    - 在 Python 脚本中导入 SQLAlchemy：`from sqlalchemy import create_engine`
3. 创建数据库引擎：
    - 使用 `create_engine` 函数创建一个数据库引擎，指定数据库的连接字符串。例如，连接到 MySQL 数据库：`engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')`
4. 定义数据库模型：
    - 使用 SQLAlchemy ORM 定义数据库模型，即 Python 类，映射到数据库表。每个类属性对应表中的一个列。
5. 数据库会话：
    - 使用 `Session` 类创建数据库会话，用于执行数据库操作。会话负责管理数据库连接和事务。
6. 数据库操作：
    - 使用会话执行数据库操作，如查询、插入、更新、删除等。会话会自动处理数据库事务。
7. 关闭会话：
    - 完成数据库操作后，记得关闭会话，释放数据库连接资源：`session.close()`
"""

import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# 创建数据库引擎（使用SQLite数据库）
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'sqlite3.db')
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# 创建基类
Base = declarative_base()

# 定义User类（数据库模型）
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String)
    phone = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

# 创建所有表
Base.metadata.create_all(engine)

# 创建Session类并启动会话
Session = sessionmaker(bind=engine)
session = Session()

# 插入数据
new_user = User(name="李慕婉", age=30, email="liuyun@example.com", phone="13900000000", address="上海市浦东新区")
session.add(new_user)
session.commit()

# 查询数据
users = session.query(User).all()
for user in users:
    print(user)

# 更新数据
user = session.query(User).filter_by(name="李慕婉").first()
if user:
    user.age = 31
    session.commit()

# 删除数据
user = session.query(User).filter_by(name="李慕婉").first()
if user:
    session.delete(user)
    session.commit()

# 关闭会话
session.close()

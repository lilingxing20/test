"""
python-dotenv 是一个 Python 库，用于从 .env 文件中加载环境变量到你的应用程序中。这是管理敏感信息（如数据库凭证、API 密钥和配置参数）的一种安全而灵活的方式，而无需将这些信息硬编码到代码中。
    1.安装
        pip install python-dotenv
    2.在项目的根目录下创建一个 .env 文件，里面包含你需要的环境变量。这些环境变量以 KEY=VALUE 的格式存储。
        DATABASE_URL=localhost:3306
        SECRET_KEY=a123456
        API_KEY=api_key
        DEBUG=True
    3.在 Python 代码中使用 dotenv，首先需要加载 .env 文件中的内容。
        load_dotenv 函数可用来加载变量，并通过 os.getenv() 或 os.environ 来访问这些变量。
"""

from dotenv import load_dotenv
import os

# 将 .env 文件中的环境变量加载到系统中
load_dotenv()

# 访问环境变量
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
api_key = os.getenv('API_KEY')
debug = os.getenv('DEBUG', 'False')
undefined_var = os.getenv('UNDEFINED_VAR')

print(f"Database URL: {database_url}")
print(f"Secret Key: {secret_key}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug}")
print(f"Undefined Var: {undefined_var}")

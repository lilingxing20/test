""" json 模块操作 JSON 数据
Python内置的json模块提供了对象和JSON的转换功能，包括将Python对象转换为JSON字符串，以及将JSON字符串转换为Python对象。
"""

import json

# 定义一个字典对象
dict0 = {'id': 123, 'name': '张三', 'email': '1@1.com'}

# 序列化为 JSON 字符串
# ensure_ascii 保留中文字符
user_json = json.dumps(dict0, ensure_ascii=False)
print(user_json)  # {"id": 123, "name": "张三", "email": "1@1.com"}

# 序列化为对象
user = json.loads(user_json)
print(user)  # {'id': 123, 'name': '张三', 'email': '1@1.com'}


""" 运行结果：
{"id": 123, "name": "张三", "email": "1@1.com"}
{'id': 123, 'name': '张三', 'email': '1@1.com'}
"""

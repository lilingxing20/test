"""
序列化对象
  序列化对象需要自定义序列化和反序列化的函数，这里使用json模块来序列化和反序列化对象。
"""

import json


class User:
    def __init__(self, id_no, name, email):
        self.id_no = id_no
        self.name = name
        self.email = email


def user_serializer(user):
    """自定义序列化函数"""
    return {
        'id': user.id_no,
        'name': user.name,
        'email': user.email
    }


def user_decoder(dct):
    """自定义反序列化函数"""
    if 'id' in dct and 'name' in dct and 'email' in dct:
        return User(dct['id'], dct['name'], dct['email'])
    return dct


if __name__ == '__main__':

    # 定义对象
    user = User(123, '张三', 'zhangsan@example.com')
    print("Original:", user.id_no, user.name, user.email)

    # 序列化为json
    # ensure_ascii=False 可以保留中文字符
    # default=user_serializer 指定自定义序列化函数
    user_obj_json = json.dumps(user, ensure_ascii=False, default=user_serializer)
    print("Serialized:", user_obj_json)

    # 反序列化为对象
    # object_hook=user_decoder 指定自定义反序列化函数
    user_obj = json.loads(user_obj_json, object_hook=user_decoder)
    print("Deserialized:", user_obj.id_no, user_obj.name, user_obj.email)


""" 运行结果：
Original: 123 张三 zhangsan@example.com
Serialized: {"id": 123, "name": "张三", "email": "zhangsan@example.com"}
Deserialized: 123 张三 zhangsan@example.com
"""

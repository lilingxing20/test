# -*- coding:utf-8 -*-

from marshmallow import fields, Schema
from sqlalchemy import Column, Integer, String

from config.env import DB_PREFIX
from extends import Base


# 角色模型
class Role(Base):
    # 设置表名
    __tablename__ = DB_PREFIX + "role"
    id = Column(Integer, primary_key=True)
    # 角色名称
    name = Column(String(150), nullable=False, comment="角色名称")
    # 角色编码
    code = Column(String(30), nullable=False, comment="角色编码")
    # 角色状态：1-正常 2-停用
    status = Column(Integer, default=1, comment="角色状态：1-正常 2-停用")
    # 角色排序
    sort = Column(Integer, default=0, comment="角色排序")
    # 角色备注
    note = Column(String(255), nullable=True, comment="角色备注")


class RoleSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    code = fields.String(required=True)
    status = fields.Integer(required=True)
    sort = fields.Integer(required=True)
    note = fields.String(required=False)
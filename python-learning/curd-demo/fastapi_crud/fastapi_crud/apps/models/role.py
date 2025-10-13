# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field, validator
from typing import Optional

# 修复导入路径
from fastapi_crud.config.env import DB_PREFIX
from fastapi_crud.extends.extends_sqlalchemy import Base


# 数据库模型
class Role(Base):
    __tablename__ = DB_PREFIX + "role"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, comment="角色名称")
    code = Column(String(30), nullable=False, comment="角色编码")
    status = Column(Integer, default=1, comment="角色状态：1-正常 2-停用")
    sort = Column(Integer, default=0, comment="角色排序")
    note = Column(String(255), nullable=True, comment="角色备注")


# Pydantic模型 - 用于创建和更新角色
class RoleBase(BaseModel):
    name: str = Field(..., max_length=150, description="角色名称")
    code: str = Field(..., max_length=30, description="角色编码")
    status: int = Field(..., ge=1, le=2, description="角色状态：1-正常 2-停用")
    sort: int = Field(..., description="角色排序")
    note: Optional[str] = Field(None, max_length=255, description="角色备注")

    class Config:
        from_attributes = True  # Pydantic v2的配置，替代v1的orm_mode


# Pydantic模型 - 用于创建角色请求体
class RoleCreate(RoleBase):
    pass


# Pydantic模型 - 用于更新角色请求体
class RoleUpdate(RoleBase):
    id: int = Field(..., description="角色ID")


# Pydantic模型 - 用于查询角色状态请求体
class RoleStatusUpdate(BaseModel):
    id: int = Field(..., description="角色ID")
    status: int = Field(..., ge=1, le=2, description="角色状态：1-正常 2-停用")


# Pydantic模型 - 用于返回角色数据
class RoleOut(RoleBase):
    id: int = Field(..., description="角色ID")

    class Config:
        from_attributes = True  # Pydantic v2的配置，替代v1的orm_mode


# Pydantic模型 - 用于返回分页角色列表
class RolePageOut(BaseModel):
    code: int = Field(200, description="状态码")
    message: str = Field("查询成功", description="响应消息")
    data: dict = Field(..., description="数据")


# Pydantic模型 - 用于返回通用响应
class CommonResponse(BaseModel):
    code: int = Field(..., description="状态码")
    message: str = Field(..., description="响应消息")
    data: Optional[dict] = Field(None, description="数据")
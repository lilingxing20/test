# -*- coding:utf-8 -*-

from fastapi import APIRouter, Depends, Query, Path, Body
from sqlalchemy.orm import Session

# 修复导入路径
from fastapi_crud.apps.services.role import (
    get_role_list,
    get_role_detail,
    add_role,
    update_role,
    delete_role,
    update_role_status
)
from fastapi_crud.apps.models.role import (
    RoleOut,
    RoleCreate,
    RoleUpdate,
    RoleStatusUpdate,
    RolePageOut,
    CommonResponse
)
from fastapi_crud.extends.extends_sqlalchemy import get_db


# 创建角色路由
role_router = APIRouter(
    prefix="/role",
    tags=["角色模块"],
    responses={404: {"description": "未找到"}}
)


# 查询角色分页列表
@role_router.get("/list", response_model=RolePageOut, summary="查询角色分页列表")
def role_list(
    page: int = Query(..., ge=1, description="页码，从1开始", example=1),
    limit: int = Query(..., ge=1, description="每页记录数", example=10),
    name: str = Query(None, description="角色名称搜索关键词", example="管理员"),
    db: Session = Depends(get_db)
):
    """查询角色列表，支持分页和按名称搜索"""
    result = get_role_list(db, page, limit, name)
    return {
        "code": 200,
        "message": "查询成功",
        "data": result
    }


# 查询角色详情
@role_router.get("/detail", response_model=CommonResponse, summary="查询角色详情")
def role_detail(
    id: int = Query(..., description="角色ID", example=1),
    db: Session = Depends(get_db)
):
    """根据角色ID获取角色的详细信息"""
    role = get_role_detail(db, id)
    # 将RoleOut对象转换为字典
    return {
        "code": 200,
        "message": "查询成功",
        "data": role.model_dump()  # 使用model_dump()将Pydantic模型转换为字典
    }


# 新增角色
@role_router.post("/add", response_model=CommonResponse, summary="新增角色")
def role_add(
    role_data: RoleCreate = Body(..., description="角色信息"),
    db: Session = Depends(get_db)
):
    """创建一个新的角色"""
    add_role(db, role_data)
    return {
        "code": 200,
        "message": "添加成功"
    }


# 修改角色
@role_router.put("/edit", response_model=CommonResponse, summary="修改角色")
def role_edit(
    role_data: RoleUpdate = Body(..., description="角色信息"),
    db: Session = Depends(get_db)
):
    """更新角色的基本信息"""
    update_role(db, role_data)
    return {
        "code": 200,
        "message": "更新成功"
    }


# 删除角色
@role_router.delete("/delete/{id}", response_model=CommonResponse, summary="删除角色")
def role_delete(
    id: int = Path(..., description="角色ID", example=3),
    db: Session = Depends(get_db)
):
    """根据角色ID删除指定的角色"""
    delete_role(db, id)
    return {
        "code": 200,
        "message": "删除成功"
    }


# 修改角色状态
@role_router.put("/status", response_model=CommonResponse, summary="修改角色状态")
def role_status(
    status_data: RoleStatusUpdate = Body(..., description="角色状态信息"),
    db: Session = Depends(get_db)
):
    """启用或停用指定的角色"""
    update_role_status(db, status_data)
    return {
        "code": 200,
        "message": "设置成功"
    }
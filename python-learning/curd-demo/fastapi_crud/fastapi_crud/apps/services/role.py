# -*- coding:utf-8 -*-

from sqlalchemy.orm import Session
from fastapi import HTTPException

# 修复导入路径
from fastapi_crud.apps.models.role import Role, RoleCreate, RoleUpdate, RoleStatusUpdate, RoleOut


# 获取角色分页列表
def get_role_list(db: Session, page: int, limit: int, name: str = None):
    try:
        # 构建查询
        query = db.query(Role)
        
        # 搜索过滤
        if name:
            query = query.filter(Role.name.contains(name))
        
        # 计算总数
        total = query.count()
        
        # 分页查询
        roles = query.offset((page - 1) * limit).limit(limit).all()
        
        # 计算总页数
        pages = (total + limit - 1) // limit
        
        # 将ORM对象转换为Pydantic模型
        role_models = [RoleOut.model_validate(role) for role in roles]
        
        return {
            "roles": role_models,
            "total": total,
            "page": page,
            "pages": pages
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")


# 获取角色详情
def get_role_detail(db: Session, role_id: int):
    try:
        role = db.query(Role).filter(Role.id == role_id).first()
        
        if not role:
            raise HTTPException(status_code=404, detail="角色不存在")
        
        # 将ORM对象转换为Pydantic模型
        return RoleOut.model_validate(role)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败：{str(e)}")


# 添加角色
def add_role(db: Session, role_data: RoleCreate):
    try:
        # 检查角色名称是否已存在
        if db.query(Role).filter(Role.name == role_data.name).first():
            raise HTTPException(status_code=400, detail="角色名称已存在")
        
        # 检查角色编码是否已存在
        if db.query(Role).filter(Role.code == role_data.code).first():
            raise HTTPException(status_code=400, detail="角色编码已存在")
        
        # 创建角色
        role = Role(
            name=role_data.name,
            code=role_data.code,
            status=role_data.status,
            sort=role_data.sort,
            note=role_data.note
        )
        
        db.add(role)
        db.commit()
        db.refresh(role)
        
        return role
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"添加失败：{str(e)}")


# 更新角色
def update_role(db: Session, role_data: RoleUpdate):
    try:
        # 查找角色
        role = db.query(Role).filter(Role.id == role_data.id).first()
        
        if not role:
            raise HTTPException(status_code=404, detail="角色不存在")
        
        # 检查角色名称是否已存在（排除当前角色）
        if db.query(Role).filter(Role.name == role_data.name, Role.id != role_data.id).first():
            raise HTTPException(status_code=400, detail="角色名称已存在")
        
        # 检查角色编码是否已存在（排除当前角色）
        if db.query(Role).filter(Role.code == role_data.code, Role.id != role_data.id).first():
            raise HTTPException(status_code=400, detail="角色编码已存在")
        
        # 更新角色信息
        role.name = role_data.name
        role.code = role_data.code
        role.status = role_data.status
        role.sort = role_data.sort
        role.note = role_data.note
        
        db.commit()
        db.refresh(role)
        
        return role
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"更新失败：{str(e)}")


# 删除角色
def delete_role(db: Session, role_id: int):
    try:
        # 查找角色
        role = db.query(Role).filter(Role.id == role_id).first()
        
        if not role:
            raise HTTPException(status_code=404, detail="角色不存在")
        
        # 删除角色
        db.delete(role)
        db.commit()
        
        return True
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"删除失败：{str(e)}")


# 更新角色状态
def update_role_status(db: Session, status_data: RoleStatusUpdate):
    try:
        # 查找角色
        role = db.query(Role).filter(Role.id == status_data.id).first()
        
        if not role:
            raise HTTPException(status_code=404, detail="角色不存在")
        
        # 更新角色状态
        role.status = status_data.status
        
        db.commit()
        db.refresh(role)
        
        return role
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"设置失败：{str(e)}")


# 获取所有角色（用于下拉选择等场景）
def get_all_roles(db: Session):
    try:
        roles = db.query(Role).all()
        # 将ORM对象转换为Pydantic模型
        return [RoleOut.model_validate(role) for role in roles]
    except Exception as e:
        print(f"获取角色列表失败：{str(e)}")
        return []
# -*- coding:utf-8 -*-

from sanic.response import json
from sqlalchemy.orm import Session

from apps.models.role import Role, RoleSchema
from apps.constants.message import PAGE_LIMIT
from extends import get_db


def get_db_session():
    """
    获取数据库会话
    """
    db_gen = get_db()
    db = next(db_gen)
    return db, db_gen


def RoleList(request):
    """
    查询角色分页数据
    """
    # 页码 - 显式转换为int类型
    page = request.args.get('page', '1')
    try:
        page = int(page)
    except ValueError:
        page = 1
    
    # 每页数 - 显式转换为int类型
    limit = request.args.get('limit', str(PAGE_LIMIT))
    try:
        limit = int(limit)
    except ValueError:
        limit = PAGE_LIMIT
    
    # 用户名
    name_filter = request.args.get('name', '')
    
    db, db_gen = get_db_session()
    try:
        # 分页查询
        query = db.query(Role)
        if name_filter:
            query = query.filter(Role.name.contains(name_filter))
        
        # 获取总数
        total = query.count()
        
        # 计算偏移量
        offset = (page - 1) * limit
        
        # 执行分页查询
        roles = query.offset(offset).limit(limit).all()
        
        # 序列化数据
        role_schema = RoleSchema(many=True)
        roles_data = role_schema.dump(roles)
        
        result = {
            'roles': roles_data,
            'total': total,
            'page': page,
            'pages': (total + limit - 1) // limit  # 计算总页数
        }
        
        return json(result)
    finally:
        db_gen.close()


def RoleDetail(request):
    """
    根据角色ID查询详情
    """
    # 移除type参数，手动转换为int类型
    role_id_str = request.args.get('id')
    if not role_id_str:
        return json({'message': '缺少角色ID'})
    try:
        role_id = int(role_id_str)
    except ValueError:
        return json({'message': '无效的角色ID'})
    
    db, db_gen = get_db_session()
    try:
        role = db.query(Role).filter_by(id=role_id).first()
        if role:
            role_schema = RoleSchema()
            role_data = role_schema.dump(role)
            return json(role_data)
        else:
            return json({'message': '角色不存在'})
    finally:
        db_gen.close()


def RoleAdd(request):
    """
    添加角色
    """
    data = request.json
    name = data.get('name')
    code = data.get('code')
    status = data.get('status')
    sort = data.get('sort')
    note = data.get('note')
    
    db, db_gen = get_db_session()
    try:
        role = Role(name=name, code=code, status=status, sort=sort, note=note)
        db.add(role)
        db.commit()
        db.refresh(role)  # 刷新对象获取ID
        return json({'message': '添加成功'})
    except Exception as e:
        db.rollback()
        return json({'message': f'添加失败: {str(e)}'})
    finally:
        db_gen.close()


def RoleEdit(request):
    """
    更新角色
    """
    data = request.json
    # 移除type参数
    role_id = data.get('id')
    if not role_id:
        return json({'message': '缺少角色ID'})
    try:
        role_id = int(role_id)
    except ValueError:
        return json({'message': '无效的角色ID'})
    
    db, db_gen = get_db_session()
    try:
        role = db.query(Role).filter_by(id=role_id).first()
        if role:
            name = data.get('name')
            code = data.get('code')
            status = data.get('status')
            sort = data.get('sort')
            note = data.get('note')
            
            role.name = name
            role.code = code
            role.status = status
            role.sort = sort
            role.note = note
            
            db.commit()
            return json({'message': '更新成功'})
        else:
            return json({'message': '角色不存在'})
    except Exception as e:
        db.rollback()
        return json({'message': f'更新失败: {str(e)}'})
    finally:
        db_gen.close()


def RoleDelete(request):
    """
    删除角色
    """
    # 从request.ctx.role_id获取ID，因为ID参数现在在URL路径中
    role_id = getattr(request.ctx, 'role_id', None)
    if not role_id:
        return json({'message': '缺少角色ID'})
    
    db, db_gen = get_db_session()
    try:
        role = db.query(Role).filter_by(id=role_id).first()
        if role:
            db.delete(role)
            db.commit()
            return json({'message': '删除成功'})
        else:
            return json({'message': '角色不存在'})
    except Exception as e:
        db.rollback()
        return json({'message': f'删除失败: {str(e)}'})
    finally:
        db_gen.close()


def RoleStatus(request):
    """
    设置角色状态
    """
    data = request.json
    # 移除type参数
    role_id = data.get('id')
    status = data.get('status')
    
    if not role_id:
        return json({'message': '缺少角色ID'})
    if status is None:
        return json({'message': '缺少状态值'})
    
    try:
        role_id = int(role_id)
        status = int(status)
    except ValueError:
        return json({'message': '无效的参数类型'})
    
    db, db_gen = get_db_session()
    try:
        role = db.query(Role).filter_by(id=role_id).first()
        if role:
            role.status = status
            db.commit()
            return json({'message': '设置成功'})
        else:
            return json({'message': '角色不存在'})
    except Exception as e:
        db.rollback()
        return json({'message': f'设置失败: {str(e)}'})
    finally:
        db_gen.close()


def getRoleList():
    """
    获取角色列表
    """
    db, db_gen = get_db_session()
    try:
        query = db.query(Role).all()
        role_schema = RoleSchema(many=True)
        roles = role_schema.dump(query)
        return roles
    finally:
        db_gen.close()

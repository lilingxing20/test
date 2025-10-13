# -*- coding:utf-8 -*-

from flask import jsonify, request

from apps.models.role import Role, RoleSchema
from apps.constants.message import PAGE_LIMIT
from extends.extends_sqlalchemy import db


def RoleList():
    """
    查询角色分页数据
    """
    try:
        # 页码
        page = request.args.get('page', 1, type=int)
        # 每页数
        limit = request.args.get('limit', PAGE_LIMIT, type=int)
        # 用户名
        name_filter = request.args.get('name', False, type=str)
        
        # 分页查询
        query = Role.query
        if name_filter:
            query = query.filter(Role.name.contains(name_filter))
        pagination = query.paginate(page=page, per_page=limit, error_out=False)
        roles = RoleSchema(many=True).dump(pagination.items)
        
        return jsonify({
            'code': 200,
            'data': {
                'roles': roles,
                'total': pagination.total,
                'page': pagination.page,
                'pages': pagination.pages
            },
            'message': '查询成功'
        })
    except Exception as e:
        return jsonify({
            'code': 500,
            'message': f'查询失败：{str(e)}'
        })


def RoleDetail():
    """
    根据角色ID查询详情
    """
    try:
        role_id = request.args.get('id', type=int)
        if not role_id:
            return jsonify({'code': 400, 'message': '角色ID不能为空'})
            
        role = Role.query.filter_by(id=role_id).first()
        if role:
            role_data = RoleSchema().dump(role)
            return jsonify({
                'code': 200,
                'data': role_data,
                'message': '查询成功'
            })
        else:
            return jsonify({'code': 404, 'message': '角色不存在'})
    except Exception as e:
        return jsonify({
            'code': 500,
            'message': f'查询失败：{str(e)}'
        })


def RoleAdd():
    """
    添加角色
    """
    try:
        data = request.json
        if not data:
            return jsonify({'code': 400, 'message': '请求数据不能为空'})
            
        # 参数验证
        required_fields = ['name', 'code', 'status', 'sort']
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'{field}不能为空'})
                
        # 检查角色名称和编码是否已存在
        if Role.query.filter_by(name=data['name']).first():
            return jsonify({'code': 400, 'message': '角色名称已存在'})
            
        if Role.query.filter_by(code=data['code']).first():
            return jsonify({'code': 400, 'message': '角色编码已存在'})
            
        # 创建角色
        role = Role(
            name=data['name'],
            code=data['code'],
            status=data['status'],
            sort=data['sort'],
            note=data.get('note', '')
        )
        
        db.session.add(role)
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '添加成功'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': f'添加失败：{str(e)}'
        })


def RoleEdit():
    """
    更新角色（与controller中调用的函数名保持一致）
    """
    try:
        data = request.json
        if not data or 'id' not in data:
            return jsonify({'code': 400, 'message': '角色ID不能为空'})
            
        role_id = data['id']
        role = Role.query.filter_by(id=role_id).first()
        
        if not role:
            return jsonify({'code': 404, 'message': '角色不存在'})
            
        # 参数验证
        required_fields = ['name', 'code', 'status', 'sort']
        for field in required_fields:
            if field not in data:
                return jsonify({'code': 400, 'message': f'{field}不能为空'})
                
        # 检查角色名称和编码是否已存在（排除当前角色）
        if Role.query.filter(Role.name == data['name'], Role.id != role_id).first():
            return jsonify({'code': 400, 'message': '角色名称已存在'})
            
        if Role.query.filter(Role.code == data['code'], Role.id != role_id).first():
            return jsonify({'code': 400, 'message': '角色编码已存在'})
            
        # 更新角色信息
        role.name = data['name']
        role.code = data['code']
        role.status = data['status']
        role.sort = data['sort']
        role.note = data.get('note', '')
        
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '更新成功'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': f'更新失败：{str(e)}'
        })


def RoleDelete(role_id):
    """
    删除角色
    """
    try:
        role = Role.query.filter_by(id=role_id).first()
        
        if not role:
            return jsonify({'code': 404, 'message': '角色不存在'})
            
        db.session.delete(role)
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '删除成功'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': f'删除失败：{str(e)}'
        })


def RoleStatus():
    """
    设置角色状态
    """
    try:
        data = request.json
        if not data or 'id' not in data or 'status' not in data:
            return jsonify({'code': 400, 'message': '角色ID和状态不能为空'})
            
        role_id = data['id']
        status = data['status']
        
        role = Role.query.filter_by(id=role_id).first()
        if not role:
            return jsonify({'code': 404, 'message': '角色不存在'})
            
        role.status = status
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '设置成功'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': f'设置失败：{str(e)}'
        })


def getRoleList():
    """
    获取角色列表
    """
    try:
        roles = Role.query.all()
        return RoleSchema(many=True).dump(roles)
    except Exception as e:
        print(f'获取角色列表失败：{str(e)}')
        return []

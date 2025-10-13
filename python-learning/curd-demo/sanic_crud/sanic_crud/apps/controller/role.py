# -*- coding:utf-8 -*-

from sanic import Blueprint
from sanic_ext import openapi

from apps.services import role


# 角色蓝图
role_bp = Blueprint('role', url_prefix='/role')


# 查询分页数据
@role_bp.get('/list')
@openapi.tag('角色管理')
@openapi.description('查询角色分页数据')
@openapi.parameter('page', int, location='query', required=True, description='页码')
@openapi.parameter('limit', int, location='query', required=True, description='每页数量')
@openapi.parameter('name', str, location='query', required=False, description='角色名称筛选')
@openapi.response(200, {'code': int, 'message': str}, description='角色列表数据')
def get_list(request):
    """
    查询角色分页数据
    """
    result = role.RoleList(request)
    return result


# 查询单条数据
@role_bp.get('/detail')
@openapi.tag('角色管理')
@openapi.description('根据ID查询角色详情')
@openapi.parameter('id', int, location='query', required=True, description='角色ID')
@openapi.response(200, {'code': int, 'message': str}, description='角色详情数据')
def get_detail(request):
    """
    根据ID查询角色详情
    """
    result = role.RoleDetail(request)
    return result


# 新增数据
@role_bp.post('/add')
@openapi.tag('角色管理')
@openapi.description('添加角色')
@openapi.body({
    'application/json': {
        'name': str,
        'code': str,
        'status': int,
        'sort': int,
        'note': str
    }
})
@openapi.response(200, {'code': int, 'message': str}, description='角色新增结果')
def add_data(request):
    """
    添加角色
    """
    result = role.RoleAdd(request)
    return result


# 修改数据 - 从POST改为PUT
@role_bp.put('/edit')
@openapi.tag('角色管理')
@openapi.description('更新角色信息')
@openapi.body({
    'application/json': {
        'id': int,
        'name': str,
        'code': str,
        'status': int,
        'sort': int,
        'note': str
    }
})
@openapi.response(200, {'code': int, 'message': str}, description='角色修改结果')
def edit_data(request):
    """
    更新角色信息
    """
    result = role.RoleEdit(request)
    return result


# 删除数据 - 从POST改为DELETE
@role_bp.delete('/delete/<id:int>')
@openapi.tag('角色管理')
@openapi.description('根据ID删除角色')
@openapi.parameter('id', int, location='path', required=True, description='角色ID')
@openapi.response(200, {'code': int, 'message': str}, description='角色删除结果')
def delete_data(request, id):
    """
    删除角色
    """
    # 将ID添加到请求对象中，以便服务层获取
    request.ctx.role_id = id
    result = role.RoleDelete(request)
    return result


# 修改状态 - 从POST改为PUT
@role_bp.put('/status')
@openapi.tag('角色管理')
@openapi.description('根据ID修改角色状态')
@openapi.body({
    'application/json': {
        'id': int,
        'status': int
    }
})
@openapi.response(200, {'code': int, 'message': str}, description='角色状态修改结果')
def change_status(request):
    """
    修改角色状态
    """
    result = role.RoleStatus(request)
    return result

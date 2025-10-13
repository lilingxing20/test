from flask import Blueprint
from apps.services import role

# 角色蓝图
role_blue = Blueprint('role', __name__, url_prefix='/role')


# 查询分页数据
@role_blue.get('/list')
def get_list():
    """
    查询角色分页列表
    ---
    tags:
      - 角色模块
    summary: 查询角色分页列表
    description: 获取角色列表，支持分页和按名称搜索
    parameters:
      - name: page
        in: query
        type: integer
        required: true
        description: 页码，从1开始
        example: 1
      - name: limit
        in: query
        type: integer
        required: true
        description: 每页记录数
        example: 10
      - name: name
        in: query
        type: string
        required: false
        description: 角色名称搜索关键词
        example: 管理员
    responses:
      200:
        description: 查询成功
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 200
            message:
              type: string
              description: 响应消息
              example: 查询成功
            data:
              type: object
              properties:
                roles:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: 角色ID
                        example: 1
                      name:
                        type: string
                        description: 角色名称
                        example: 超级管理员
                      code:
                        type: string
                        description: 角色编码
                        example: SUPER_ADMIN
                      status:
                        type: integer
                        description: 角色状态（1-正常，2-停用）
                        example: 1
                      sort:
                        type: integer
                        description: 排序号
                        example: 0
                      note:
                        type: string
                        description: 备注信息
                        example: 系统最高权限角色
                total:
                  type: integer
                  description: 总记录数
                  example: 20
                page:
                  type: integer
                  description: 当前页码
                  example: 1
                pages:
                  type: integer
                  description: 总页数
                  example: 2
      400:
        description: 参数错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 400
            message:
              type: string
              description: 错误消息
              example: 页码必须为正整数
      500:
        description: 服务器内部错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 500
            message:
              type: string
              description: 错误消息
              example: 查询失败：数据库错误
    """
    result = role.RoleList()
    return result


# 查询单条数据
@role_blue.get('/detail')
def get_detail():
    """
    查询角色详情
    ---
    tags:
      - 角色模块
    summary: 查询角色详情
    description: 根据角色ID获取角色的详细信息
    parameters:
      - name: id
        in: query
        type: integer
        required: true
        description: 角色ID
        example: 1
    responses:
      200:
        description: 查询成功
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 200
            message:
              type: string
              description: 响应消息
              example: 查询成功
            data:
              type: object
              properties:
                id:
                  type: integer
                  description: 角色ID
                  example: 1
                name:
                  type: string
                  description: 角色名称
                  example: 超级管理员
                code:
                  type: string
                  description: 角色编码
                  example: SUPER_ADMIN
                status:
                  type: integer
                  description: 角色状态（1-正常，2-停用）
                  example: 1
                sort:
                  type: integer
                  description: 排序号
                  example: 0
                note:
                  type: string
                  description: 备注信息
                  example: 系统最高权限角色
      400:
        description: 参数错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 400
            message:
              type: string
              description: 错误消息
              example: 角色ID不能为空
      404:
        description: 角色不存在
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 404
            message:
              type: string
              description: 错误消息
              example: 角色不存在
      500:
        description: 服务器内部错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 500
            message:
              type: string
              description: 错误消息
              example: 查询失败：数据库错误
    """
    result = role.RoleDetail()
    return result


# 新增数据
@role_blue.post('/add')
def add_data():
    """
    新增角色
    ---
    tags:
      - 角色模块
    summary: 新增角色
    description: 创建一个新的角色
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - code
            - status
            - sort
          properties:
            name:
              type: string
              description: 角色名称
              example: 普通用户
              maxLength: 150
            code:
              type: string
              description: 角色编码
              example: NORMAL_USER
              maxLength: 30
            status:
              type: integer
              description: 角色状态（1-正常，2-停用）
              example: 1
              enum: [1, 2]
            sort:
              type: integer
              description: 排序号
              example: 10
            note:
              type: string
              description: 备注信息
              example: 系统默认角色
              maxLength: 255
    responses:
      200:
        description: 添加成功
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 200
            message:
              type: string
              description: 响应消息
              example: 添加成功
      400:
        description: 参数错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 400
            message:
              type: string
              description: 错误消息
              example: 角色名称已存在
      500:
        description: 服务器内部错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 500
            message:
              type: string
              description: 错误消息
              example: 添加失败：数据库错误
    """
    result = role.RoleAdd()
    return result


# 修改数据
@role_blue.put('/edit')
def edit_data():
    """
    修改角色
    ---
    tags:
      - 角色模块
    summary: 修改角色
    description: 更新角色的基本信息
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - id
            - name
            - code
            - status
            - sort
          properties:
            id:
              type: integer
              description: 角色ID
              example: 2
            name:
              type: string
              description: 角色名称
              example: 编辑用户
              maxLength: 150
            code:
              type: string
              description: 角色编码
              example: EDIT_USER
              maxLength: 30
            status:
              type: integer
              description: 角色状态（1-正常，2-停用）
              example: 1
              enum: [1, 2]
            sort:
              type: integer
              description: 排序号
              example: 5
            note:
              type: string
              description: 备注信息
              example: 具有编辑权限的角色
              maxLength: 255
    responses:
      200:
        description: 更新成功
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 200
            message:
              type: string
              description: 响应消息
              example: 更新成功
      400:
        description: 参数错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 400
            message:
              type: string
              description: 错误消息
              example: 角色名称已存在
      404:
        description: 角色不存在
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 404
            message:
              type: string
              description: 错误消息
              example: 角色不存在
      500:
        description: 服务器内部错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 500
            message:
              type: string
              description: 错误消息
              example: 更新失败：数据库错误
    """
    result = role.RoleEdit()
    return result


# 删除数据
@role_blue.delete('/delete/<int:id>')
def delete_data(id):
    """
    删除角色
    ---
    tags:
      - 角色模块
    summary: 删除角色
    description: 根据角色ID删除指定的角色
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: 角色ID
        example: 3
    responses:
      200:
        description: 删除成功
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 200
            message:
              type: string
              description: 响应消息
              example: 删除成功
      404:
        description: 角色不存在
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 404
            message:
              type: string
              description: 错误消息
              example: 角色不存在
      500:
        description: 服务器内部错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 500
            message:
              type: string
              description: 错误消息
              example: 删除失败：数据库错误
    """
    result = role.RoleDelete(id)
    return result


# 修改状态
@role_blue.put('/status')
def change_status():
    """
    修改角色状态
    ---
    tags:
      - 角色模块
    summary: 修改角色状态
    description: 启用或停用指定的角色
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - id
            - status
          properties:
            id:
              type: integer
              description: 角色ID
              example: 2
            status:
              type: integer
              description: 角色状态（1-正常，2-停用）
              example: 2
              enum: [1, 2]
    responses:
      200:
        description: 设置成功
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 200
            message:
              type: string
              description: 响应消息
              example: 设置成功
      400:
        description: 参数错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 400
            message:
              type: string
              description: 错误消息
              example: 角色ID和状态不能为空
      404:
        description: 角色不存在
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 404
            message:
              type: string
              description: 错误消息
              example: 角色不存在
      500:
        description: 服务器内部错误
        schema:
          type: object
          properties:
            code:
              type: integer
              description: 状态码
              example: 500
            message:
              type: string
              description: 错误消息
              example: 设置失败：数据库错误
    """
    result = role.RoleStatus()
    return result

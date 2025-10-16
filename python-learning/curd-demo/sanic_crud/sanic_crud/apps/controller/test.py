from sanic import Blueprint
from sanic_ext import openapi
from sanic import request, response


# 蓝图
test_bp = Blueprint('test', url_prefix='/test')


# 测试路由
@test_bp.get("/index")
@openapi.tag('测试')
@openapi.description('测试路由')
@openapi.response(200, {'code': int, 'message': str}, description='测试路由结果')
@openapi.parameter('a', str, location='query', required=False, description='参数a')
@openapi.parameter('b', str, location='query', required=False, description='参数b')
@openapi.parameter('c', str, location='query', required=False, description='参数c')
async def index(request: request.Request):
    lst = []
    lst.append(f"请求的url: {request.url}")
    lst.append(f"请求的path: {request.path}")
    lst.append(f"请求的方法: {request.method}")
    lst.append(f"请求的查询参数: {request.query_args}")
    lst.append(f"请求的查询参数: {request.args}")
    lst.append(f"a: {request.args.get('a')}, "
               f"b: {request.args.get('b')}, "
               f"a_lst: {request.args.getlist('a')}, "
               f"c: {request.args.get('c')}, "
               f"c: {request.args.get('c', 'xxx')}")
    return response.text("\n".join(lst))


@test_bp.get("/cookie")
@openapi.tag('测试')
@openapi.description('测试cookie路由')
@openapi.response(200, {'code': int, 'message': str}, description='测试cookie路由结果')
@openapi.parameter('name', str, location='query', required=False, description='cookie名称')
@openapi.parameter('value', str, location='query', required=False, description='cookie值')
async def cookie(request: request.Request):
    # 获取 cookie
    name = request.args.get("name")
    value = request.args.get("value")
    print(request.cookies.get(name))
    print(request.cookies)
    
    # 创建响应对象
    resp = response.text(f"cookie {name} = {value}")
    
    # 使用response.set_cookie()方法来设置cookie及其属性
    if name and value:
        resp.add_cookie(name, value, max_age=5)
    
    print(resp.cookies.cookies[0])
    print(resp.cookies.cookies[0].value)

    # 删除cookie
    if name:
        resp.delete_cookie(name)
    print(resp.cookies.cookies[0].value)

    return resp

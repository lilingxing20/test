import operator
from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse

from fastapi_crud.apps.models.test import OperateName


# 创建角色路由
test_router = APIRouter(
    prefix="/test",
    tags=["测试模块"],
    responses={404: {"description": "未找到"}}
)


@test_router.get("/")
async def get_test(request: Request):
    return JSONResponse(content={"message": "测试模块"})


@test_router.get("/{flag}")
async def get_flag(flag: bool):
    return JSONResponse(content={"flag": flag})


@test_router.get("/{num1}/{operate}/{num2}")
async def calc(num1: float, operate: OperateName, num2: float):
    try:
        # 转换运算符为Python操作符
        op_func = {
            OperateName.add: operator.add,
            OperateName.sub: operator.sub,
            OperateName.mul: operator.mul,
            OperateName.div: operator.truediv,
        }[operate]
        operate_str = {
            OperateName.add: "+",
            OperateName.sub: "-",
            OperateName.mul: "*",
            OperateName.div: "/",
        }[operate]
        result = op_func(num1, num2)
        return JSONResponse(content={"result": f"{num1} {operate_str} {num2} = {result}"})
    except KeyError:
        return JSONResponse(content={"error": "无效运算符"}, status_code=400)
    except ZeroDivisionError:
        return JSONResponse(content={"error": "除数不能为零"}, status_code=400)

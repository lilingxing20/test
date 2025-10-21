import uvicorn

from fastapi_crud.config.env import FASTAPI_HOST, FASTAPI_PORT, FASTAPI_DEBUG


if __name__ == '__main__':
    # 打印API文档地址
    print("\n" + "="*50)
    print(f"应用启动：")
    print(f"- 访问地址：http://{FASTAPI_HOST}:{FASTAPI_PORT}")
    print(f"- API文档：http://{FASTAPI_HOST}:{FASTAPI_PORT}/docs")
    print(f"- 备选文档：http://{FASTAPI_HOST}:{FASTAPI_PORT}/redoc")
    print("="*50 + "\n")
    # 直接使用FastAPI的run方法启动应用
    uvicorn.run(
        "fastapi_crud.app:app",
        host=FASTAPI_HOST,
        port=FASTAPI_PORT,
        reload=FASTAPI_DEBUG
    )
    print(f"\n应用停止!")

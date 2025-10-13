# -*- coding:utf-8 -*-

import pytest
import traceback
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_crud.apps import create_app
from fastapi_crud.extends.extends_sqlalchemy import Base, get_db
# 移除不存在的DB_URL导入


# 创建测试数据库引擎
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 创建测试会话
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 重写依赖项，使用测试数据库
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# 创建测试客户端
app = create_app()
app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


# 测试前置条件
@pytest.fixture(scope="module")
def test_db():
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    yield
    # 测试完成后删除所有表
    Base.metadata.drop_all(bind=engine)


# 测试角色API
def test_role_api(test_db):
    # 1. 添加角色
    role_data = {
        "name": "测试角色",
        "code": "TEST_ROLE",
        "status": 1,
        "sort": 10,
        "note": "这是一个测试角色"
    }
    response = client.post("/role/add", json=role_data)
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["message"] == "添加成功"
    
    # 2. 查询角色列表
    response = client.get("/role/list?page=1&limit=10")
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["data"]["total"] >= 1
    
    # 获取第一个角色的ID
    role_id = response.json()["data"]["roles"][0]["id"]
    
    # 3. 查询角色详情
    response = client.get(f"/role/detail?id={role_id}")
    assert response.status_code == 200
    assert response.json()["code"] == 200
    assert response.json()["data"]["id"] == role_id
    
    # 4. 更新角色
    update_data = {
        "id": role_id,
        "name": "更新后的角色",
        "code": "UPDATED_ROLE",
        "status": 1,
        "sort": 5,
        "note": "这是更新后的测试角色"
    }
    response = client.put("/role/edit", json=update_data)
    assert response.status_code == 200
    assert response.json()["code"] == 200
    
    # 5. 更新角色状态
    status_data = {
        "id": role_id,
        "status": 2
    }
    response = client.put("/role/status", json=status_data)
    assert response.status_code == 200
    assert response.json()["code"] == 200
    
    # 6. 删除角色
    response = client.delete(f"/role/delete/{role_id}")
    assert response.status_code == 200
    assert response.json()["code"] == 200
    
    # 7. 验证角色已删除
    response = client.get(f"/role/detail?id={role_id}")
    # 修改断言：当角色不存在时，API会直接返回404状态码
    assert response.status_code == 404
    # 对于404响应，不需要检查JSON内容


# 如果直接运行该脚本，则执行测试
if __name__ == "__main__":
    print("运行FastAPI角色管理API测试...")
    # 创建测试数据库
    Base.metadata.create_all(bind=engine)
    
    try:
        # 执行测试
        test_role_api(None)
        print("测试成功！")
    except Exception as e:
        print(f"测试失败：{str(e)}")
        print("完整错误栈：")
        traceback.print_exc()  # 打印完整的错误栈信息
    finally:
        # 清理测试数据库
        Base.metadata.drop_all(bind=engine)
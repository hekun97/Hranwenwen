import pytest
import json

from utils.bulid_json_data import get_json_data

# 定义一些JSON数据
test_data = [
    '{"name": "Alice", "age": 30}',
    '{"name": "Bob", "age": 25}'
]


# 使用pytest.mark.parametrize装饰器
@pytest.mark.parametrize("data", test_data)
def test_json(data):
    # 将JSON字符串转换为字典
    data_dict = json.loads(data)
    # 测试逻辑
    assert "name" in data_dict
    assert "age" in data_dict
    assert type(data_dict["name"]) == str
    assert type(data_dict["age"]) == int

# 使用pytest.mark.parametrize装饰器
@pytest.mark.parametrize("data", get_json_data(1, "login_data"))
def test_json(data):
    # 将JSON字符串转换为字典
    # data_dict = json.loads(data)
    # 测试逻辑
    assert "uname" in data
    assert "upwd" in data
    assert type(data["uname"]) == str
    assert type(data["upwd"]) == str

userinfo = [{"username": "张三", "password": "12345"}]
@pytest.mark.parametrize('info', userinfo)
def test_add(info):
    print(type(info))
    print(info)

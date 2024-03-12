# 成功退出登录断言
def success_login_out(response):
    # 断言状态码
    assert 200 == response.status_code
    # 断言业务状态
    assert response.json().get("status")
    # 断言登录消息，从excel获取数据
    assert "退出登录" == response.json().get("msg")


# 失败退出登录
def failed_login_out(response):
    # 断言状态码
    assert 200 == response.status_code
    # 断言业务状态
    assert not response.json().get("status")
    # 断言登录消息，从excel获取数据
    assert "未登录" == response.json().get("msg")

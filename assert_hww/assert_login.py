# 断言登录成功
def success_login(response):
    # 断言状态码
    assert 200 == response.status_code
    # 断言业务状态
    assert response.json().get("status")
    # 断言登录消息，从excel获取数据
    assert "登录成功" == response.json().get("msg")


# 断言登录参数为空
def failed_login_null(response):
    # 断言状态码
    assert 200 == response.status_code
    # 断言业务状态
    assert not response.json().get("status")
    # 断言登录消息，从excel获取数据
    assert "登录参数为空" == response.json().get("msg")


# 断言用户名或者密码错误
def failed_u_p_error(response):
    # 断言状态码
    assert 200 == response.status_code
    # 断言业务状态
    assert not response.json().get("status")
    # 断言登录消息，从excel获取数据
    assert "用户名或者密码错误" == response.json().get("msg")

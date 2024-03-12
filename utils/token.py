from testcase.test01_login import TestLogin

# 实例化登录测试用例对象
test_login = TestLogin()


# 获取token
def get_token():
    token_l = ""
    if not token_l:
        test_login.setup_method()
        token_l = test_login.test_001_login_success()
    return token_l

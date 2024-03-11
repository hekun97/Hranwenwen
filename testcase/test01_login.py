"""
登录接口的测试用例
"""
import allure

from api.login.login import LoginAPI
from assert_hww import assert_login
from config.logging_config import init_logging
from utils.bulid_json_data import get_json_data


class TestLogin:
    # 方法级别的setup方法
    def setup_method(self):
        # 初始化登录接口类
        self.login_api = LoginAPI()
        self.logger = init_logging()

    # 定义日志级别为CRITICAL
    @allure.severity(allure.severity_level.CRITICAL)
    # 正向功能，仅必填参数
    def test_001_login_success(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(0)
        self.logger.info("case001的输入的登录信息为："+str(json_data).replace("'", "\""))
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 打印获取到的token数据，如果后续其它请求需要保持登录，那么需要带入token信息
        self.logger.info("case001获取到的token信息为："+response.json().get("content").get("token"))
        # 断言
        assert_login.success_login(response)

    # 定义日志级别为CRITICAL
    @allure.severity(allure.severity_level.CRITICAL)
    # 全部参数
    def test_002_login_success(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(1)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.success_login(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 无参
    def test_003_login_failed(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(2)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_login_null(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 少参-用户名
    def test_004_login_failed(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(3)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_login_null(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 多参-ttt
    def test_005_login_success(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(4)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.success_login(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 错误参数（uname>>ttt）
    def test_006_login_failed(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(5)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_login_null(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 数据异常-密码为空
    def test_007_login_failed(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(6)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_u_p_error(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 数据异常-用户名过长
    def test_008_login_failed(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(7)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_u_p_error(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 数据错误-密码含中文，，含小数和特殊符号这里没有账号不测，理论上小数和特殊符号可以通过
    def test_009_login_failed(self):
        # 获取json文件中的第i+1条测试用例data数据
        json_data = get_json_data(8)
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_u_p_error(response)

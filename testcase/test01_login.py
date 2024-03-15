"""
登录接口的测试用例
"""
import allure
import pytest

from api.login.login_api import LoginAPI
from assert_hww import assert_login
from config.logging_config import init_logging
from utils.bulid_json_data import get_json_data


class TestLogin:
    # 方法级别的setup方法
    def setup_method(self):
        # 初始化登录接口类
        self.login_api = LoginAPI()
        self.logger = init_logging()

    # 定义优先级别为CRITICAL
    @allure.severity(allure.severity_level.CRITICAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(1, "login_data"))
    # 正向功能，仅必填参数
    def test_001_login_success(self, json_data):
        self.logger.info("case001的输入的登录信息为："+str(json_data))
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # token数据，如果后续其它请求需要保持登录，那么需要带入token信息
        self.logger.info("case001获取到的token信息为："+response.json().get("content").get("token"))
        # 断言
        assert_login.success_login(response)

    # 定义优先级别为CRITICAL
    @allure.severity(allure.severity_level.CRITICAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(2, "login_data"))
    # 全部参数
    def test_002_login_success(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.success_login(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(3, "login_data"))
    # 无参
    def test_003_login_failed(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_login_null(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(4, "login_data"))
    # 少参-用户名
    def test_004_login_failed(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_login_null(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(5, "login_data"))
    # 多参-ttt
    def test_005_login_success(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.success_login(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(6, "login_data"))
    # 错误参数（uname>>ttt）
    def test_006_login_failed(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_login_null(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(7, "login_data"))
    # 数据异常-密码为空
    def test_007_login_failed(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_u_p_error(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(8, "login_data"))
    # 数据异常-用户名、密码过长两条数据
    def test_008_login_failed(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_u_p_error(response)

    # 定义优先级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 获取json文件中的第i条测试用例data数据
    @pytest.mark.parametrize("json_data", get_json_data(9, "login_data"))
    # 数据错误-密码含中文，，含小数和特殊符号这里没有账号不测，理论上小数和特殊符号可以通过
    def test_009_login_failed(self, json_data):
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = self.login_api.login(json_data)
        # 断言
        assert_login.failed_u_p_error(response)

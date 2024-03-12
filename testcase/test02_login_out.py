"""
退出登录接口的测试用例
"""
import allure

from api.login.login_out import Login_out_API
from config.logging_config import init_logging
from testcase.test01_login import TestLogin


class TestLogin_out:
    # 方法级别的setup方法
    def setup_method(self):
        # 初始化登录接口类
        self.login_out_api = Login_out_API()
        self.logger = init_logging()

    # 定义日志级别为CRITICAL
    @allure.severity(allure.severity_level.CRITICAL)
    # 正向功能，仅必填参数
    def test_001_login_out_success(self):
        # 获取token数据
        token_data = TestLogin.test_001_login_success.token_l
        login_out_data = {"token": "9a590148b58759140605e0030f83adc5"}
        # self.logger.info("case001的输入的退出token信息为："+login_out_data)
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        # 断言状态码
        assert 200 == response.status_code
        # 断言业务状态
        assert response.json().get("status")
        # 断言登录消息，从excel获取数据
        assert "退出登录" == response.json().get("msg")
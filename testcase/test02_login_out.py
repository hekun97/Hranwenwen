"""
退出登录接口的测试用例
"""
import allure

from api.login.login_out import Login_out_API
from config.logging_config import init_logging
from utils.token import get_token
from assert_hww import assert_login_out


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
        token = get_token()
        login_out_data = {"token": token}
        self.logger.info("case001的输入的退出token信息为："+token)
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.success_login_out(response)

"""
退出登录接口的测试用例
"""
import json
import textwrap

import allure

from api.login.login_out import Login_out_API
from config.logging_config import init_logging
from utils.bulid_json_data import get_json_data
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
        # 获取字符串格式的json数据
        json_data = get_json_data(1, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["token"] = token
        # 打印日志信息
        self.logger.info("case001的输入的退出token信息为："+token)
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.success_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 无参
    def test_002_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(2, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 多参
    def test_003_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(3, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["token"] = token
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.success_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 错误参数,token>>>ttt
    def test_004_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(4, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["ttt"] = token
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 数据异常-token为空
    def test_005_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(4, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 数据异常-token过长
    def test_006_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(6, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["token"] = token + login_out_data["token"]
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 错误数据-token含中文
    def test_007_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(7, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["token"] = token + login_out_data["token"]
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 错误数据-token含空格
    def test_008_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(8, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["token"] = login_out_data["token"] + token
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 错误数据-token含小数点
    def test_009_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(9, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]
        login_out_data["token"] = login_out_data["token"] + token
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

    # 定义日志级别为NORMAL
    @allure.severity(allure.severity_level.NORMAL)
    # 错误数据-token长度不足
    def test_010_login_out_success(self):
        # 获取字符串格式的json数据
        json_data = get_json_data(10, "login_out_data")
        # 将json转换为python字典
        login_out_data = json.loads(json_data)
        # 获取token数据
        token = get_token()
        # 将token数据赋值给login_out_data["token"]，使用textwrap.wrap切割字符串
        login_out_data["token"] = textwrap.wrap(token, width=28)
        print(login_out_data["token"])
        # 调用退出登录接口完成退出，token_data为传入的请求体内容
        response = self.login_out_api.login_out(login_out_data)
        # 断言
        assert_login_out.failed_login_out(response)

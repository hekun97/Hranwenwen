import allure
import pytest
import requests
import logging
import utils

from api.login.login import LoginAPI


class TestLogin:
    # 方法级别的setup方法
    def setup_method(self):
        self.login_api = LoginAPI()
        self.session = requests.Session()

    # 方法级别的teardown方法
    def teardown_method(self):
        if self.session:
            self.session.close()

    # 用例001:登录成功，uname为用户名，upwd为密码，expect为预期结果，utils.get_login_data_by_excel为从excel表中获取的数据
    @pytest.mark.parametrize("uname, upwd, expect", utils.get_login_data_by_excel(2, 3))
    # 定义日志级别为CRITICAL
    @allure.severity(allure.severity_level.CRITICAL)
    def test_001_login_success(self, uname, upwd, expect):
        logging.info("用例输入数据如下：用户名：{}，密码：{}，预期结果：{}".format(uname, upwd, expect))
        # 发送请求附带数据
        json_data = {"uname": uname, "upwd": upwd}
        response = self.login_api.login(json_data)
        print(response.json())
        # 打印获取到的token数据
        # print(response.json().get("content").get("token"))
        # 断言状态码
        assert 200 == response.status_code
        # 断言业务状态
        assert response.json().get("status")
        # 断言登录消息，从excel获取数据
        assert expect == response.json().get("msg")

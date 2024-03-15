"""
登录和登出接口
"""

from utils.get_configs import get_env_config
from utils.base_request import BaseRequest


class LoginAndOutAPI:
    def __init__(self):
        # 实例化发请求的BaseRequest对象
        self.base_request = BaseRequest()
        # 实例化环境配置
        config = get_env_config()
        # 获取生产环境'base'中的url
        self.base_url = config.get('base', 'base_url')

    # 发送登录请求
    def login(self, login_data):
        # 登录接口
        url_login = self.base_url + "/api_user/loginapi"
        # 返回响应数据
        response = self.base_request.send_post(url=url_login, data=login_data)
        return response

    # 发送退出登录请求
    def login_out(self, login_out_data):
        # 登出接口
        url_login_out = self.base_url + "/api_user/huanwenwenssologinout"
        # 返回响应数据
        response = self.base_request.send_post(url=url_login_out, data=login_out_data)
        return response

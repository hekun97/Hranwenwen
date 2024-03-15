"""
登录接口
"""

from utils.Prd_config import get_prd_config
from utils.base_request import BaseRequest


class LoginAPI:
    def __init__(self):
        # 实例化发请求的BaseRequest对象
        self.base_request = BaseRequest()
        # 实例化生产环境配置
        config = get_prd_config()
        # 获取生产环境'base'中的url
        base_url = config.get('base', 'base_url')
        # 登录接口
        self.url_login = base_url+"/api_user/loginapi"

    # 发送登录请求
    def login(self, login_data):
        # 返回响应数据
        response = self.base_request.send_post(url=self.url_login, data=login_data)
        return response

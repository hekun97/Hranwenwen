"""
登录接口
"""
import requests

from utils.Prd_config import get_prd_config

import json


class LoginAPI:
    def __init__(self):
        config = get_prd_config()
        # 获取生产环境'base'中的url
        base_url = config.get('base', 'base_url')
        # 登录接口
        self.url_login = base_url+"/api_user/loginapi"

    # 发送登录请求
    def login(self, login_data):
        # 返回响应数据
        response = requests.post(url=self.url_login, data=login_data, verify=False)
        return response

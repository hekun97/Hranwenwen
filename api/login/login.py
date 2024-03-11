"""
登录接口
"""
import requests

from utils.Prd_config import get_prd_config

import json


class LoginAPI:
    # 在初始化方法中，定义需要使用到的接口url
    def __init__(self):
        config = get_prd_config()
        # 获取'base'部分的数据
        base_url = config.get('base', 'base_url')
        # 登录接口
        self.url_login = base_url+"/api_user/loginapi"

    # 发送登录请求
    def login(self, json_data):
        # 将json单引号数据转为双引号
        json_data = (str(json_data).replace("'", "\""))
        # 将json数据转为python字典
        login_data = json.loads(json_data)
        # 返回响应数据
        response = requests.post(url=self.url_login, data=login_data, verify=False)
        return response

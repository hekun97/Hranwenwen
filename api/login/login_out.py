"""
退出登录接口
"""
import requests

from utils.Prd_config import get_prd_config


class Login_out_API:
    def __init__(self):
        config = get_prd_config()
        # 获取生产环境'base'中的url
        base_url = config.get('base', 'base_url')
        # 登录接口
        self.url_login = base_url+"/api_user/huanwenwenssologinout"

    # 发送退出登录请求
    def login_out(self, login_out_data):
        # 返回响应数据
        response = requests.post(url=self.url_login, data=login_out_data, verify=False)
        return response

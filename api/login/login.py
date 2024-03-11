import requests

import utils
import json
"""
登录接口
"""
class LoginAPI:
    # 在初始化方法中，定义需要使用到的接口url
    def __init__(self):
        config = utils.get_prd_config()
        # 获取'base'部分的数据
        base_url = config.get('base', 'base_url')
        self.url_login = base_url+"/api_user/loginapi"
        print(self.url_login)

    # login接口
    def login(self, json_data):
        json_data = (str(json_data).replace("'", "\""))
        py = json.loads(json_data)
        return requests.post(url=self.url_login, data=py, verify=False)

# 发送基本请求的工具类
import requests


class BaseRequest:
    # 发送post请求
    def send_post(self, url=None, data=None, header=None, auth=None):
        # 如果header和auth都不为空
        if header is not None and auth is not None:
            response = requests.post(url=url, data=data, headers=header, auth=auth)
            return response
        # 如果header不为空
        elif header is not None:
            response = requests.post(url=url, data=data, headers=header)
            return response
        # 如果auth不为空
        elif auth is not None:
            response = requests.post(url=url, data=data, auth=auth)
            return response
        # 都为空
        else:
            response = requests.post(url=url, data=data)
            return response

    # 发送get请求
    def send_get(self, url=None, data=None, header=None, auth=None):
        # 如果header和auth都不为空
        if header is not None and auth is not None:
            response = requests.get(url=url, params=data, headers=header, auth= auth)
            return response
        # 如果header不为空
        elif header is not None:
            response = requests.get(url=url, params=data, headers=header)
            return response
        # 如果auth不为空
        elif auth is not None:
            response = requests.get(url=url, params=data, auth=auth)
            return response
        # 都为空
        else:
            response = requests.get(url=url, params=data)
            return response

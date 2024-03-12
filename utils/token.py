from api.login.login import LoginAPI
from utils.bulid_json_data import get_json_data

login_api = LoginAPI()

def get_token():
    # 获取json文件中的第i+1条测试用例data数据
    json_data = get_json_data(0)
    # 调用登录接口完成登录，json_data为传入的请求体内容
    response = login_api.login(json_data)
    # token数据，如果后续其它请求需要保持登录，那么需要带入token信息
    token_l = response.json().get("content").get("token")
    return token_l

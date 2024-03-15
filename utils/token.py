from api.login_and_out_api import LoginAndOutAPI
from config.logging_config import init_logging
from utils.bulid_json_data import get_json_data

login_api = LoginAndOutAPI()
logger = init_logging()

# 获取token
def get_token():
    token_l = ""
    if not token_l:
        # 获取json文件中的第i条测试用例data数据
        json_data = get_json_data(1, "login_data")[0]
        # 调用登录接口完成登录，json_data为传入的请求体内容
        response = login_api.login(json_data)
        # token数据，如果后续其它请求需要保持登录，那么需要带入token信息
        token_l = response.json().get("content").get("token")
        # 打印日志信息
        logger.info("获取的token信息为：" + token_l)
    return token_l

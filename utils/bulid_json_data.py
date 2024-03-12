# 获取json数据的工具类
import json

from utils.base_dir import get_base_dir


def get_json_data(i):
    BASE_DIR = get_base_dir()
    # 指定json文件的路径
    json_file =BASE_DIR+ "/data/login_data.json"
    # 使用utf-8编码的方式打开json文件
    with open(json_file, encoding="utf-8") as f:
        # 读取json数据
        json_datas = json.load(f)
        # 根据索引获取对应的json格式data数据
        json_data = json_datas[i]["data"]
        # 使用dumps返回一个标准的json格式数据，格式为字符串
    return json.dumps(json_data)

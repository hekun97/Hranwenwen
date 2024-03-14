# 获取json数据的工具类
import json

from base_dir_util import get_base_dir


def get_json_data(i, json_data):
    BASE_DIR = get_base_dir()
    # 指定json文件的路径
    json_file =BASE_DIR + "/data/{}.json".format(json_data)
    # 使用utf-8编码的方式打开json文件
    with open(json_file, encoding="utf-8") as f:
        # 读取json数据
        json_datas = json.load(f)
        # 根据caseid获取对应的json格式data数据
        for json_data in json_datas:
            if json_data.get("caseid") == i:
                return json.dumps(json_data["data"])
        # 使用dumps返回一个标准的json格式数据，格式为包含JSON数据的字符串
    return "没有匹配数据"

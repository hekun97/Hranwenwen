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
                # 找到列表类型的data数据，列表内为json格式的信息
                json_data = json_data["data"]
                return json_data
    return "没有匹配数据"

# json_data =get_json_data(1 ,"login_out_data")
#
# token = json_data[0]["token"]
# token_l = token + "测试"
# print(type(token_l))
# print(token_l)

import json

from utils.base_dir import get_base_dir


def get_json_data(i):
    BASE_DIR = get_base_dir()
    # 指定json文件的路径
    json_file =BASE_DIR+ "/data/login_data.json"
    # 使用utf-8编码的方式打开json文件
    with open(json_file, encoding="utf-8") as f:
        # 将读取的文件内容返回为python的字典对象
        json_datas = json.load(f)
        # 遍历字典对象并将数据以元组的方式存放到test_data列表中
    return json_datas[i]["data"]

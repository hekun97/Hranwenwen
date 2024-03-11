from configparser import ConfigParser

import openpyxl
import os


# 获取登录数据的工具类
def get_login_data_by_excel(min_row, max_row):
    # os.path.dirname此方法的作用是用来获取用文件的路径，__file__表示的是当前文件(config.py)
    BaseDir = get_dir()
    # 加载Excel文件
    workbook = openpyxl.load_workbook(BaseDir+'/data/login_data.xlsx')
    # 获取第二列的所有内容
    # 选择第一个工作表
    sheet = workbook.active
    login_data = []
    for row in sheet.iter_rows(values_only=True, min_row=min_row, max_row=max_row, max_col=3):
        # 将每一行的内容加入到login_data
        login_data.append(tuple(row))
    return login_data

# 获取项目目录绝对路径方法
def get_dir():
    return os.path.dirname(__file__)


# 读取生产环境配置文件信息
def get_prd_config():
    # 获取项目目录绝对路径
    BaseDir = get_dir()
    # 创建解析器对象
    config = ConfigParser()
    # 读取配置文件
    config.read(BaseDir + '/config/prd_config.ini')
    return config

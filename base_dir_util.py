import os


# 获取项目目录的绝对路径
def get_base_dir():
    # return os.path.abspath('.')
    return os.path.dirname(os.path.abspath(__file__))

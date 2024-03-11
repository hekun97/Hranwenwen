from configparser import ConfigParser

from utils.base_dir import get_base_dir


# 读取生产环境配置文件信息
def get_prd_config():
    # 获取项目目录绝对路径
    BaseDir = get_base_dir()
    # 创建解析器对象
    config = ConfigParser()
    # 读取配置文件
    config.read(BaseDir + '/config/prd_config.ini')
    return config

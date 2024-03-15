from configparser import ConfigParser

from base_dir_util import get_base_dir


# 读取环境配置文件信息的工具类，按需读取不同环境的配置信息
def get_env_config():
    # 获取项目目录绝对路径
    BaseDir = get_base_dir()
    # 创建解析器对象
    config = ConfigParser()
    # 读取环境配置文件，这里获取生产环境的配置
    config.read(BaseDir + '/config/prd_config.ini')
    return config

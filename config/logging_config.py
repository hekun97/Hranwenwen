import logging, logging.handlers
from datetime import datetime

from base_dir_util import get_base_dir


def init_logging():
    # 创建日志器
    logger = logging.getLogger(__name__)
    # 设置日志的级别
    logger.setLevel(logging.DEBUG)
    # 创建处理器
    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接返回logger去写日志
    if not logger.handlers:
        fh = logging.handlers.TimedRotatingFileHandler(get_base_dir()+"/log/log-{}.log".format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')), when="midnight", interval=1, backupCount=7)
        sh = logging.StreamHandler()
        fh.setLevel(logging.INFO)
        sh.setLevel(logging.INFO)
        # 创建格式器
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
        formatter = logging.Formatter(fmt=fmt)
        # 在处理器添加格式器
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        # 在日志器添加处理器
        logger.addHandler(sh)
        logger.addHandler(fh)
    return logger

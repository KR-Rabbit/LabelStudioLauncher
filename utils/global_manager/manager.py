import utils

# 全局跨模块共享变量管理模块
# pyton global关键字在模块内有效，通过在其他脚本或者模块中导入该模块，实现不同页面间的配置共享
config = {}


def init():
    global config
    config = utils.load_config()


def get_():
    global config
    return config


def set_(value):
    global config
    config = value


def update_(value):
    global config
    config = value


def save_(value):
    global config
    config = value
    utils.save_config(config)

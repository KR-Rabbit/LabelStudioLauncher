import utils

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

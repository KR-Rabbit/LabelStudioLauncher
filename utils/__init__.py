import copy
import json
import os
import pathlib
import re
import socket

USER_PATH = os.path.expanduser("~")
DEFAULT_CONFIG = {
    "version": "2.0.0",
    "image_format": [".jpg", ".jpeg", ".png", ".bmp", ".gif"],
    "main": {
        "close_type": "minimize",
        "second_confirm": False
    },
    "server": {
        "installed": False,
        "latest_check": 0,
        "data_root": "D:\\Data",
        "data_path": "D:\\Data",
        "http_address": {"ip": "localhost", "port": 8000},
        "recursive": False,
    },
    "conda": {
        "conda_root": str(pathlib.Path(USER_PATH, "miniconda3")),
        "conda_exec_path": str(pathlib.Path(USER_PATH, "miniconda3", "_conda.exe")),
        "env_name": "base"
    }
}
# ip地址正则，所有局域网
IP_REG = (r"^(localhost|::1|::0|0\.0\.0\.0|127\.0\.0\.1|10(\.\d{1,3}){0,3}|172\.(1[6-9]|2\d|3[01])(\.\d{1,3}){0,"
          r"2}|192\.168(\.\d{1,3}){0,2})$")


def format_conda_path(conda_path):
    conda_path = pathlib.Path(conda_path) if conda_path is not None else conda_path
    if conda_path.exists():
        for p in conda_path.iterdir():
            if p.name in ["_conda.exe", "conda.bat"]:
                return conda_path
    paths = get_conda_paths_by_env()
    if paths:
        root = min(paths, key=lambda folder: len(folder.parts))
        return root
    else:
        return None


def get_conda_paths_by_env():
    paths = os.environ.get("Path").split(";")
    pl = []
    for path in paths:
        path_ = pathlib.Path(path)
        if path_.exists():
            for p in path_.iterdir():
                if p.name in ["_conda.exe", "conda.bat"]:
                    pl.append(path_)
    return pl


def is_conda_path(conda_path):  # 判断conda的可执行文件或者bat脚本路径是否存在
    if not conda_path:
        return False
    path = pathlib.Path(conda_path)
    if path.exists() and path.name in ["_conda.exe", "conda.bat", "conda.exe"]:
        return True
    return False


def is_conda_root(conda_root):
    if not conda_root:
        return False
    path = pathlib.Path(conda_root)
    if path.exists() and path.joinpath("_conda.exe").exists() or path.joinpath("condabin", "conda.bat").exists():
        return True
    return False


def load_config():
    config_path = pathlib.Path(USER_PATH).joinpath(".studio_launcher")
    if not config_path.exists():
        with config_path.open("w") as f:
            json.dump(DEFAULT_CONFIG, f)
        return DEFAULT_CONFIG
    try:
        with config_path.open("r") as f:
            config = json.load(f)
            t_config = copy.deepcopy(DEFAULT_CONFIG)
            for key in t_config.keys():
                if key in config.keys():
                    if isinstance(t_config[key], dict):
                        for k in t_config[key].keys():
                            if k in config[key].keys():
                                t_config[key][k] = config[key][k]
                    else:
                        t_config[key] = config[key]
            config = t_config
    except (json.JSONDecodeError, PermissionError):
        return DEFAULT_CONFIG
    else:
        return config


def save_config(config):
    config_path = pathlib.Path(USER_PATH).joinpath(".studio_launcher")
    try:
        with config_path.open("w") as f:
            json.dump(config, f)
    except (json.JSONDecodeError, PermissionError):
        pass


def get_python_exe_path(conda_config: dict):
    conda_root = conda_config.get("conda_root")
    env_name = conda_config.get("env_name")
    if is_conda_root(conda_root):
        python_exe_path = pathlib.Path(conda_root, "envs", env_name,
                                       "python.exe") if env_name != "base" else pathlib.Path(conda_root, "python.exe")
    else:
        python_exe_path = ""
    return python_exe_path


def get_data_root(server_config: dict):
    data_root = server_config.get("data_root")
    if data_root and pathlib.Path(data_root).exists():
        return pathlib.Path(data_root).__str__()
    else:
        return ""


def ip_check(ip, to_json=True) -> str:
    """
    检查ip是否合法，该ip用于生成json文件
    :param ip:
    :param to_json: 是否用于生成json文件，影响返回值
    :return:  合法的ip
    """
    pattern = re.compile(IP_REG)
    if pattern.match(ip):
        if to_json:
            if ip in ["0.0.0.0", "::0"]:
                ip = socket.gethostbyname(socket.gethostname())
            elif ip == "::1":
                ip = "localhost"
    else:
        ip = "localhost"
    return ip


def port_check(port, rtype=int) -> int or str:
    try:
        port = int(port)
        if port < 0 or port > 65535:
            r_port = 8000 if rtype == int else "8000"
        else:
            r_port = str(port) if rtype == str else port
    except ValueError:
        r_port = 8000 if rtype == int else "8000"
    return r_port

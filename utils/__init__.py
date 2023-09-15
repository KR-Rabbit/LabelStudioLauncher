import io
import json
import os
import pathlib

USER_PATH = os.path.expanduser("~")
IMAGES_FORMAT = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
default_config = {
    "main": {
        "close_type": "minimize",
        "second_confirm": False
    },
    "server": {
        "installed": False,
        "latest_check": 0,
        "data_root": "D:\\Data",
        "data_path": "D:\\Data",
    },
    "conda": {
        "conda_root": str(pathlib.Path(USER_PATH, "miniconda3")),
        "conda_exec_path": str(pathlib.Path(USER_PATH, "miniconda3", "_conda.exe")),
        "env_name": "base"
    }
}


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
    if path.exists() and path.name in ["_conda.exe", "conda.bat"]:
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
            json.dump(default_config, f)
        return default_config
    try:
        with config_path.open("r") as f:
            config = json.load(f)
    except (json.JSONDecodeError, io.UnsupportedOperation):
        return default_config
    else:
        return config


def save_config(config):
    config_path = pathlib.Path(USER_PATH).joinpath(".studio_launcher")
    try:
        with config_path.open("w") as f:
            json.dump(config, f)
    except (json.JSONDecodeError, io.UnsupportedOperation) as e:
        pass


def generate_json_file(data_root, data_path):
    data_root = pathlib.Path(data_root)
    data_path = pathlib.Path(data_path)
    relative_path = data_path.relative_to(data_root).__str__().replace("\\", "/")
    json_list = []
    for file in data_path.iterdir():
        if file.is_file() and file.suffix in IMAGES_FORMAT:
            dic = {
                "data": {
                    "url": f"http://localhost:8000/{relative_path}/{file.name}"
                }
            }
            json_list.append(dic)
    dst = pathlib.Path(data_path).parent.joinpath(f"{data_path.name}.json")

    with dst.open("w") as f:
        json.dump(json_list, f)


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

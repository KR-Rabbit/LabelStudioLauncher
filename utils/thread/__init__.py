import json
import pathlib
import urllib
from urllib import parse

from PySide6.QtCore import QThread

from utils import DEFAULT_CONFIG, ip_check, port_check


class Executor(QThread):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        self.result = ""
        self.stop = False
        self.stopped = False

    def run(self) -> None:
        self.result = self.generate_json_file(*self.args, **self.kwargs)
        self.stopped = True

    def generate_json_file(self, data_root, data_path, img_format=None, ip="localhost", port="8000", recursive=False):
        data_root = pathlib.Path(data_root)
        data_path = pathlib.Path(data_path)

        json_list = []
        img_format = img_format or DEFAULT_CONFIG.get("image_format")
        if self.stop:
            return ""
        ip = ip_check(ip, to_json=TabError)
        port = port_check(port, rtype=str)
        r_path = pathlib.Path(data_path).relative_to(data_root)
        for file in data_path.rglob("*"):
            if self.stop:
                return
            if file.is_file() and file.suffix in img_format:
                relative_path = file.parent.relative_to(data_root).as_posix() if recursive else r_path.as_posix()
                path = f"{file.name}" if relative_path == "." else f"{relative_path}/{file.name}"
                # url编码
                dic = {"data": {"url": f"http://{ip}:{port}/{urllib.parse.quote(path.encode('utf-8'))}"}}
                json_list.append(dic)
        dst = pathlib.Path(data_path).parent.joinpath(f"{data_path.name}.json")

        with dst.open("w", encoding="utf-8") as f:
            json.dump(json_list, f, ensure_ascii=False, )
        return dst.as_posix()

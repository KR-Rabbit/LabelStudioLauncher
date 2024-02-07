import csv
import json
import pathlib
import zipfile
from urllib.parse import unquote

DEFAULT_KEY = "url"


def _url2path(url: str, data_root: str or pathlib.Path):
    """
    将url转换为本地路径
    :param url: 经过url编码的url
    :param data_root: HTTP服务的数据根目录
    :return: 本地路径
    """
    path = unquote(url).replace("http://", "")
    abs_path = pathlib.Path(data_root).joinpath(path[path.find("/") + 1:]).as_posix()
    return abs_path


def _url_decode(url_encoded: str):
    return unquote(url_encoded)


def parser_json(json_path: str, data_root: str or pathlib.Path, key=DEFAULT_KEY, is_min=False):
    """
    解析label-studio导出的json文件，将url转换为本地路径
    :param json_path: json文件路径
    :param data_root: HTTP服务的数据根目录
    :param key: url所在的键
    :param is_min: 是否是min格式的json文件
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            items = json.load(f)
            if is_min:
                for item in items:
                    url = item.get(key)
                    if url is None:
                        continue
                    item.update({key: _url2path(url, data_root)})
            else:
                for item in items:
                    url = item.get("data").get(key)
                    if url is None:
                        continue
                    item.update(data={key: _url2path(url, data_root)})
    except PermissionError:
        raise PermissionError(f"读取权限异常，解析'{json_path}'失败")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"JSON解码异常，解析'{json_path}'失败", e.doc, e.pos)
    except (AttributeError, ValueError):
        raise AttributeError(f"格式异常，解析'{json_path}'失败")
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=4)
    except json.JSONDecodeError:
        raise json.JSONDecodeError(f"写入'{json_path}'失败", json_path, 0)
    except PermissionError:
        raise PermissionError(f"写入权限异常，写入'{json_path}'失败")


def parser_json_min(json_path: str, data_root: str or pathlib.Path, key=DEFAULT_KEY):
    parser_json(json_path, data_root, key, True)


def _parser_dsv(dsv_path: str, data_root: str or pathlib.Path, delimiter: str, key=DEFAULT_KEY):
    try:
        with open(dsv_path, "r", encoding="utf-8", newline="\r\n") as f:
            reader = csv.reader(f, delimiter=delimiter)
            items = list(reader)
    except PermissionError:
        raise PermissionError(f"读取权限异常，解析'{dsv_path}'失败")
    except UnicodeError:
        raise Exception(f"编码异常, 解析'{dsv_path}'失败")
    except csv.Error:
        raise csv.Error(f"CSV解析异常，解析'{dsv_path}'失败")
    if len(items) == 0:
        raise Exception(f"文件'{dsv_path}'为空")
    header = items[0]
    if key not in header:
        raise AttributeError(f"异常格式，'{dsv_path}'中没有'{key}'字段")
    idx = header.index(key)
    try:
        for item in items[1:]:
            print(item[idx])
            item[idx] = _url2path(item[idx], data_root)
    except ValueError:
        raise ValueError(f"异常数据类型，解析'{dsv_path}'失败")
    try:
        with open(dsv_path, "w", encoding="utf-8", newline="\r\n") as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(items)
    except PermissionError:
        raise PermissionError(f"写入权限异常，写入'{dsv_path}'失败")
    except ValueError:
        raise ValueError(f"写入'{dsv_path}'失败")
    except csv.Error:
        raise csv.Error(f"写入'{dsv_path}'失败")


def parser_csv(csv_path: str, data_root: str or pathlib.Path, key=DEFAULT_KEY):
    _parser_dsv(csv_path, data_root, ",", key)


def parser_tsv(tsv_path: str, data_root: str or pathlib.Path, key=DEFAULT_KEY):
    _parser_dsv(tsv_path, data_root, "\t", key)


def _dir_file_rename(dir_path: str or pathlib.Path):
    dir_path = pathlib.Path(dir_path)
    for file in dir_path.iterdir():
        new_file_name = _url_decode(file.name)
        if new_file_name == file.name:
            continue
        new_file_path = dir_path.joinpath(new_file_name)
        if new_file_path.exists():
            new_file_path.unlink()
        file.rename(new_file_path)


def parser_coco_zip(coco_zip_path: str, data_root: str or pathlib.Path):
    coco_zip_path = pathlib.Path(coco_zip_path)
    data_root = pathlib.Path(data_root)
    extract_dir = data_root.joinpath(coco_zip_path.stem)
    try:
        with zipfile.ZipFile(coco_zip_path, "r") as z:
            z.extractall(extract_dir)
            image_dir_path = extract_dir.joinpath("images")
            json_path = extract_dir.joinpath("result.json")

            _dir_file_rename(image_dir_path)

            with open(json_path, "r", encoding="utf-8") as f:
                images = json.load(f).get("images")
                for image in images:
                    image["file_name"] = _url_decode(image["file_name"])
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(images, f, ensure_ascii=False, indent=4)
    except zipfile.BadZipFile:
        raise zipfile.BadZipFile(f"解压'{coco_zip_path}'失败")
    except PermissionError as e:
        if e.filename == str(extract_dir):
            raise PermissionError(f"解压权限异常，解压'{coco_zip_path}'失败")
        elif e.filename == str(json_path):
            raise PermissionError(f"写入权限异常，{e.filename}")
        else:
            raise PermissionError(f"重命名权限异常，{e.filename}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"文件{e.filename}在处理时被意外删除")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"JSON解码异常，解析'{json_path}'失败", e.doc, e.pos)
    except (AttributeError, ValueError):
        raise AttributeError(f"格式异常，解析'{json_path}'失败")


def parser_yolo_zip(yolo_zip_path: str, data_root: str or pathlib.Path):
    yolo_zip_path = pathlib.Path(yolo_zip_path)
    data_root = pathlib.Path(data_root)
    extract_dir = data_root.joinpath(yolo_zip_path.stem)
    try:
        with zipfile.ZipFile(yolo_zip_path, "r") as z:
            z.extractall(extract_dir)
            image_dir_path = extract_dir.joinpath("images")
            label_dir_path = extract_dir.joinpath("labels")
            _dir_file_rename(image_dir_path)
            _dir_file_rename(label_dir_path)
    except zipfile.BadZipFile:
        raise zipfile.BadZipFile(f"解压'{yolo_zip_path}'失败")
    except PermissionError as e:
        if e.filename == str(extract_dir):
            raise PermissionError(f"解压权限异常，解压'{yolo_zip_path}'失败")
        else:
            raise PermissionError(f"重命名权限异常，{e.filename}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"文件{e.filename}在处理时被意外删除")


if __name__ == '__main__':
    json_src_path = r"D:\Users\Rmi\Downloads\no_bg\project-9-at-2024-02-02-18-16-2cc3dbe9.json"
    data_r = r"E:\Program Files"
    # parser_json(json_src_path, data_r)
    # parser_json_min(json_src_path, data_r)
    csv_src_path = r"D:\Users\Rmi\Downloads\no_bg\csv.csv"

    # parser_csv(csv_src_path, data_r)

    tsv_src_path = r"D:\Users\Rmi\Downloads\no_bg\tsv.csv"
    # parser_tsv(tsv_src_path, data_r)

    coco_zip = r"D:\Users\Rmi\Downloads\no_bg\coco.zip"
    # parser_coco_zip(coco_zip, data_r)

    yolo_zip = r"D:\Users\Rmi\Downloads\no_bg\yolo.zip"
    parser_yolo_zip(yolo_zip, data_r)

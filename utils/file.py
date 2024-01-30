import os
import uuid
import zipfile
from datetime import datetime
from typing import Tuple

import aiofiles
from fastapi import UploadFile


def create_folder_for_today(base_dir: str, ext: str) -> Tuple[str, str]:
    """
    创建存储路径
    :param base_dir: 基础文件夹地址
    :param ext: 文件拓展名
    :return: 文件绝对路径，文件相对路径
    """
    # 获取当前日期
    today = datetime.today()
    unique_id = uuid.uuid4().hex
    # 格式化日期字符串，例如：2022-01-18
    date_str = today.strftime("%Y/%m/%d")

    # 构建文件夹路径
    folder_path = os.path.join(base_dir, date_str)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, f"{unique_id}.{ext}")
    relative_path = os.path.join(date_str, f"{unique_id}.{ext}")
    return file_path, relative_path


async def save_file(file_path: str, file: UploadFile) -> None:
    """
    保存文件，基于aiofile的异步保存文件
    :param file_path: 文件路径
    :param file: 文件对象，fastapi的
    :return:
    """
    async with aiofiles.open(file_path, "wb") as f:
        while True:
            chunk = await file.read(1024 * 40)
            if not chunk:
                break
            await f.write(chunk)


def zip_file(dir_path: str, target_path):
    """
    压缩文件
    :param dir_path: 需要压缩的文件夹
    :param target_path: 保存地址
    :return:
    """
    zip_obj = zipfile.ZipFile(target_path, "w", zipfile.ZIP_DEFLATED)
    for path, dirs, filenames in os.walk(dir_path):
        fpath = path.replace(dir_path, "")
        for filename in filenames:
            zip_obj.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip_obj.close()

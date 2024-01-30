"""
用于检查数据库
"""
import os.path

from config import settings


def check():
    sqlite3_path = os.path.join(settings.BASE_DIR, settings.DB_FILE)

import configparser
import os.path
import re
from curses.ascii import isdigit
from typing import List

from exceptions.config import PalWorldException
from utils.type import is_float, is_bool


class PalGameSettings:
    pal_game_settings_section = "/Script/Pal.PalGameWorldSettings"
    pal_game_settings_name = "OptionSettings"
    blacklist_file: str
    settings: dict
    settings_path: str
    blacklist: List[str]
    special_str_options: List[str] = ["AdminPassword", "ServerPassword"]

    def __init__(self, ini_path: str, blacklist_file: str):
        self.settings_path = ini_path
        self.settings = {}
        self.blacklist = []
        self.config = configparser.ConfigParser()
        self.config.read(ini_path)
        self.parse_settings()

    def parse_settings(self):
        """
        解析配置文件
        :return:
        """
        if not self.config.has_section(self.pal_game_settings_section):
            return
        options_str = self.config.get(
            self.pal_game_settings_section, self.pal_game_settings_name
        )
        match = re.search(r"\((.*?)\)", options_str)
        if not match:
            raise PalWorldException("找不到配置")

        options = match.group(1)
        options = options.split(",")
        for option in options:
            name, value = option.strip().split("=")

            if name in self.special_str_options:
                self.settings[name] = str(value.replace('"', ""))
                continue

            if value.isdigit():
                self.settings[name] = int(value)
            elif is_float(value):
                self.settings[name] = float(value)
            else:
                b, v = is_bool(value)
                if b:
                    self.settings[name] = v
                else:
                    self.settings[name] = value.replace('"', "")

    def save_settings(self, settings: dict):
        """
        保存配置
        :param settings:
        :return:
        """
        self.settings.update(settings)
        options_list = []
        for key, value in self.settings.items():
            if type(value) == str:
                value = f'"{value}"'
            options_list.append(f"{key}={value}")
        options_str = ",".join(options_list)

        if not self.config.has_section(self.pal_game_settings_section):
            self.config.add_section(self.pal_game_settings_section)

        self.config[self.pal_game_settings_section] = {
            self.pal_game_settings_name: f"({options_str})"
        }

        with open(self.settings_path, "w") as f:
            self.config.write(f)

    def get(self, name):
        return self.settings.get(name)

    def load_blacklist(self):
        if not os.path.exists(self.blacklist_file):
            return

        with open(self.blacklist_file, "r") as f:
            content = f.read()
            blacklist = content.strip().split(" ")
            self.blacklist = [steamid.split("_")[-1] for steamid in blacklist]

    def in_blacklist(self, steamid) -> bool:
        self.load_blacklist()
        return steamid in self.blacklist

    def ban_player(self, steamid):
        self.blacklist.append(steamid)
        blacklist = [f"steam_{player}" for player in self.blacklist]
        with open(self.blacklist_file, "w") as f:
            f.write(" ".join(blacklist))

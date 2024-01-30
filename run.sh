#!/usr/bin/env sh

# 初始化数据库
upgrade_output=$(pipenv run aerich upgrade)
check_init_str="You must exec init-db first"

# shellcheck disable=SC2039
if [[ $upgrade_output == *"check_init_str"* ]]; then
    echo "初始化数据库"
    pipenv run aerich init-db
    pipenv run aerich upgrade
fi

# 初始化数据
pipenv run python init.py

# 启动程序
pipenv run python main.py

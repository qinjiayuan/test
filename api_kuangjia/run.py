# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : run.py.py
# @author   : Gowent 
# @Time     : 2025/2/22 9:03
# @Copyright: Personal
import hashlib
import os
import sys

import pytest

from api.base_api import BaseSellerApi
from api.seller.login_apis import SellerLoginApi
from common.file_load import load_yaml_file, write_yaml
from paths_manager import mtxshop_data_yaml, mysql_data_yaml, common_yaml_path,http_yaml_path
import pymysql
if __name__ == '__main__':
    args = sys.argv #获取命令行参数，从来判断要执行哪个环境 == 如果是右键运行的话那么要 args的长度只有1
    env_file = f'config/env_tst.yml'
    if len(args)>1:
        print(args)
        env_name = args[1]
        env_file = f"config/env_{env_name}.yml"
        del args[1]         #要删掉的原因是：这个命令行参数接收到都会传给pytest.main()，这里需要删除防止收集不到用例
    data_info = load_yaml_file(env_file)
    write_yaml(common_yaml_path,data_info["common"])
    write_yaml(http_yaml_path, data_info["http"])
    write_yaml(mysql_data_yaml, data_info["db"])

    pytest.main()

    os.system("allure serve report/data ")
#这是我刚刚提交的
#我刚刚在提交一次
#1
#@
#3
#4

#6#5
#56565
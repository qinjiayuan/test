# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : paths_manager.py
# @author   : Gowent 
# @Time     : 2025/2/22 22:03
# @Copyright: Personal
import json
import os.path
from jsonpath_ng import parse, Index, Fields

#获取当前文件所在的目录，这个目录其实就是项目的根目录
project_path = os.path.dirname((__file__))
#根据project_path来拼接文件的绝对路径

mtxshop_Data_xlsx = f"{project_path}/data/data.xlsx"
print(mtxshop_Data_xlsx)
#测试数据yaml路径
mtxshop_data_yaml = f"{project_path}/data/data.yml"
# 数据库yaml路径
mysql_data_yaml = rf"{project_path}/config/mysql.yml"
#登录用户的yaml路径
common_yaml_path = f"{project_path}/config/common.yml"
#每个用户的ip环境
http_yaml_path = f"{project_path}/config/http.yml"




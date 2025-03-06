# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : base_api.py
# @author   : Gowent 
# @Time     : 2025/2/21 10:19
# @Copyright: Personal

from common.client import RequestsClient
from common.file_load import load_yaml_file
from paths_manager import http_yaml_path
#买家服务类

class BaseBuyerApi(RequestsClient):
    #这里定义的全局性的雷属性，来代表买家token，默认是空字符串
    #token的复制必须在其它接口调用之前完成，最终会在自定义的fixture里完成
    buyer_token = ''
    uid = ""
    def __init__(self):
     super().__init__()
     self.host = load_yaml_file(http_yaml_path)["buyer"]
     self.headers = {"Authorization":BaseBuyerApi.buyer_token}


#卖家服务基类
class BaseSellerApi(RequestsClient):
    #这里定义的全局性的雷属性，来代表卖家token，默认是空字符串
    #token的复制必须在其它接口调用之前完成，最终会在自定义的fixture里完成
    seller_token = ''
    def __init__(self):
        super().__init__()
        self.host = load_yaml_file(http_yaml_path)["seller"]
        self.headers = {"Authorization":BaseSellerApi.seller_token}

#管理员服务基类
class BaseManagerApi(RequestsClient):
    #这里定义的全局性的雷属性，来代表卖家token，默认是空字符串
    #token的复制必须在其它接口调用之前完成，最终会在自定义的fixture里完成
    manager_token = ''
    def __init__(self):
        super().__init__()
        self.host = load_yaml_file(http_yaml_path)["manager"]
        self.header = {"authorization":BaseManagerApi.manager_token}




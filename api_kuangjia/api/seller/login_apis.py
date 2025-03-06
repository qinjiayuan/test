# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : login_apis.py
# @author   : Gowent 
# @Time     : 2025/2/27 10:42
# @Copyright: Personal
from api.base_api import BaseSellerApi


class SellerLoginApi(BaseSellerApi):

    def __init__(self,user,password):
        super().__init__()
        self.url = f"{self.host}/seller/login"
        self.params = {
            "username":user,
            "password":password,
            "captcha":"1512",
            "uuid":"fghjklkjhgfghjk"
        }
        self.method = "get"
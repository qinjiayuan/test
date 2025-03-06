# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : login_apis.py
# @author   : Gowent 
# @Time     : 2025/3/1 14:50
# @Copyright: Personal
from api.base_api import BaseManagerApi


class ManagerLoginApi(BaseManagerApi):

    def __init__(self,username,password):
        super().__init__()
        self.url = f"{self.host}/admin/systems/admin-users/login"
        self.method='get'
        self.params = {
            "username":username,
            "password":password,
            "captcha":"1512",
            "uuid":"fghfgfhfghfgh"
        }


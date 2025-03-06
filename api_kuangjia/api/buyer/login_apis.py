# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : login_apis.py
# @author   : Gowent 
# @Time     : 2025/2/21 9:51
# @Copyright: Personal
import requests

from api.base_api import BaseBuyerApi
from common.client import RequestsClient

class BuyerLoginApi(BaseBuyerApi):
    def __init__(self,username,password):
        super().__init__()
        self.url = f'{self.host}/passport/login'
        self.method = 'post'
        self.data = {
            "username":username,
            "password":password,
            "captcha":"1512",
            "uuid":"fsfafdsf"
        }

    # def send(self):
    #     resp = requests.session().request(method=self.method,url=self.url,json=self.data)
    #     return resp

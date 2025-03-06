from api.base_api import BaseBuyerApi  # !/usr/bin python3
# encoding: utf-8 -*-
# @file     : member_address_apis.py
# @author   : Gowent 
# @Time     : 2025/3/1 15:54
# @Copyright: Personal



class AddAddressApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.url = f"{self.host}/members/address"
        self.method = "post"
        self.data = {
            "def_addr": 0,
            "ship_address_name": "这是地址别名",
            "name": "沙陌20241219班",
            "mobile": "18729399607",
            "region": 2799,
            "addr": "这是详细地址"
        }

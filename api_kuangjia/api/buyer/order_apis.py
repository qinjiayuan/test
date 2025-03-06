# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : order_apis.py
# @author   : Gowent 
# @Time     : 2025/2/27 11:00
# @Copyright: Personal
from api.base_api import BaseBuyerApi


class OrderRogApi(BaseBuyerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.url = f"{self.host}/trade/orders/{order_sn}/rog"
        self.method = "post"
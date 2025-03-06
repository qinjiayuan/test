# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : create_trade_apis.py
# @author   : Gowent 
# @Time     : 2025/2/23 19:01
# @Copyright: Personal
from api.base_api import BaseBuyerApi


class CreateTradeApi(BaseBuyerApi):

    def __init__(self,client='PC',way='BUY_NOW'):
        super().__init__()
        self.url = f"{self.host}/trade/create"
        self.method = 'post'
        self.data = {
            "client":client,
            "way":way
        }
# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : goods_apis.py
# @author   : Gowent 
# @Time     : 2025/3/1 15:18
# @Copyright: Personal
from api.base_api import BaseManagerApi


class GoodsBatchAuditApi(BaseManagerApi):

    def __init__(self,goods_ids:list):
        super().__init__()
        self.url = f"{self.host}/admin/goods/batch/audit"
        self.method = 'post'
        self.json = {
            "goods_ids": goods_ids,
            "message": "aaaaaa",
            "pass": 1
        }
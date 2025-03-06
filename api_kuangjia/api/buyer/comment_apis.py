# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : comment_apis.py
# @author   : Gowent 
# @Time     : 2025/2/27 11:03
# @Copyright: Personal
from api.base_api import BaseBuyerApi


class AddCommentApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id):
        super().__init__()
        self.url = f"{self.host}/members/comments"
        self.method = "post"
        self.json = {
            "order_sn":order_sn,
            "delivery_score": 5 ,
            "description_score":5,
            "service_score":5,
            "comments":[
                {
                    "sku_id": sku_id,
                    "content" :"我就是随便发一发",
                    "grade":"good",
                    "images":[]
                }
            ]
        }
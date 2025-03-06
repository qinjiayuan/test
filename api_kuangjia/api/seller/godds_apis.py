# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : godds_apis.py
# @author   : Gowent 
# @Time     : 2025/3/1 12:59
# @Copyright: Personal
from api.base_api import BaseSellerApi



#添加商品
class AddGoodsApi(BaseSellerApi):

    def  __init__(self):
        super().__init__()
        self.url = f"{self.host}/seller/goods"
        self.method = "post"
        self.json = {
            "brand_id": "",
            "category_id": 83,
            "category_name": "",
            "goods_name": "沙陌炒锅20241219班",
            "sn": "sn011111",
            "price": "800",
            "mktprice": "890",
            "cost": "10",
            "weight": "1",
            "goods_gallery_list": [
                {
                    "img_id": -1,
                    "original": "http://59.36.173.55:7000/statics/attachment/goods/2025/2/15/14/50101155.png",
                    "sort": 0
                }
            ],
            "quantity": 99999999,
            "goods_transfee_charge": 1,
            "has_changed": 0,
            "market_enable": 1,
            "template_id": 0,
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "shop_cat_id": 0,
            "meta_description": "",
            "meta_keywords": "",
            "page_title": "",
            "goods_params_list": [],
            "sku_list": [],
            "intro": "<p>商品描述</p>"
        }

# 修改订单
class ChangeGoodsApi(BaseSellerApi):
    def  __init__(self,id):
        super().__init__()
        self.url = f"{self.host}/seller/goods/{id}"
        self.method = "put"
        self.json = {
            "brand_id": "",
            "category_id": 83,
            "category_name": "",
            "goods_name": "沙陌炒锅20241219班",
            "sn": "sn011111",
            "price": "800",
            "mktprice": "890",
            "cost": "10",
            "weight": "1",
            "goods_gallery_list": [
                {
                    "img_id": -1,
                    "original": "http://59.36.173.55:7000/statics/attachment/goods/2025/2/15/14/50101155.png",
                    "sort": 0
                }
            ],
            "quantity": 99999999,
            "goods_transfee_charge": 1,
            "has_changed": 0,
            "market_enable": 1,
            "template_id": 0,
            "exchange": {
                "category_id": "",
                "enable_exchange": 0,
                "exchange_money": 0,
                "exchange_point": 0
            },
            "shop_cat_id": 0,
            "meta_description": "",
            "meta_keywords": "",
            "page_title": "",
            "goods_params_list": [],
            "sku_list": [],
            "intro": "<p>商品描述</p>"
        }

#商品下架
class GoodsUnderApi(BaseSellerApi):

    def __init__(self,goods_ids : list):
        super().__init__()
        #这里攒送的是列表参数，需要变成/seller/goods/111,222,333/under
        goods = ','.join(map(str,goods_ids))
        self.url = f"{self.host}/seller/goods/{goods}/under"
        self.method = 'put'
        self.data = {
            "reason":"没啥理由"
        }


#商家将商品放入回收站
class GoodsRecycleApi(BaseSellerApi):

    def __init__(self,goods_ids : list):
        super().__init__()
        #这里攒送的是列表参数，需要变成/seller/goods/111,222,333/under
        goods = ','.join(map(str,goods_ids))
        self.url = f"{self.host}/seller/goods/{goods}/recycle"
        self.method = 'put'
        self.data = {
            "reason":"没啥理由"
        }

#商品删除接口
class GoodsDeleteApi(BaseSellerApi):

    def __init__(self,goods_ids : list):
        super().__init__()
        #这里攒送的是列表参数，需要变成/seller/goods/111,222,333/under
        goods = ','.join(map(str,goods_ids))
        self.url = f"{self.host}/seller/goods/{goods}"
        self.method = 'delete'
        self.data = {
            "reason":"没啥理由"
        }

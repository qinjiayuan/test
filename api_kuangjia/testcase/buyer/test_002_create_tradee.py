# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_002_create_tradee.py.py
# @author   : Gowent 
# @Time     : 2025/2/23 18:19
# @Copyright: Personal
from api.buyer.cart_apis import BuyNowApi, DeleteCartApi
from api.buyer.create_trade_apis import CreateTradeApi
from common.file_load import load_yaml_file
from paths_manager import mtxshop_data_yaml
import pytest

# class TestCreateTrade:
#
#     datas = load_yaml_file("../../data/data.yml")["创建交易接口"]
#     client_data = datas["client"]
#     way = datas["way"]
#
#     @pytest.mark.parametrize("client",client_data)
#     @pytest.mark.parametrize("way",way)
#     def test_001(self,client,way):
#         if way == "BUY_NOW":
#             BuyNowApi(sku_id=541).send()
#         elif way == 'CART':
#             DeleteCartApi.send()
#             CreateTradeApi.send()





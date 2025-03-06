# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_301_goods.py
# @author   : Gowent 
# @Time     : 2025/3/2 11:08
# @Copyright: Personal
import allure
import jsonpath
import pytest

from api.seller.godds_apis import AddGoodsApi
from common.file_load import load_yaml_file
from common.json_util import updata_json
from paths_manager import mtxshop_data_yaml

@allure.epic("卖家接口测试")
@allure.feature("商品-商品相关API")
@allure.story('添加商品接口测试')


class TestAddGoodsApi:

    # #测试商品为空的情况
    # def test_add_goods_exception(self):
    #     api = AddGoodsApi()
    #     api.json["goods_name"] = ''
    #     resp = api.send()
    #     assert resp.status_code == 400
    #     assert resp.json() == {"code":"004","message":"商品名称不能为空"}
    #
    # #将商品价格为空的情况
    # def test_add_price_exception(self):
    #     api = AddGoodsApi()
    #     api.json["price"] = ""
    #     resp = api.send()
    #     assert resp.status_code == 400
    #     assert resp.json() == {"code": "004", "message": "商品价格不能为空"}

    test_data = load_yaml_file(mtxshop_data_yaml)["添加商品接口"]

    @pytest.mark.parametrize("casename,new_params,expect_code,expect_body",test_data)

    def test_add_goods(self,casename,new_params,expect_code,expect_body):
        allure.dynamic.title(casename)
        api  = AddGoodsApi()
        for expr , value  in new_params.items():
            api.json = updata_json(api.json,expr,value)
        resp = api.send()


        assert resp.status_code == expect_code
        assert resp.json() == expect_body


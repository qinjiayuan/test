# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_001_buy_now.py
# @author   : Gowent 
# @Time     : 2025/2/22 8:59
# @Copyright: Personal
import allure

from api.buyer.cart_apis import BuyNowApi
import pytest

from common.file_load import read_excel
from paths_manager import mtxshop_Data_xlsx
from paths_manager import mtxshop_data_yaml

@allure.epic("买家接口测试")
@allure.feature("交易-购物车接口模块")
@allure.story('立即购买接口测试')

class TestBuyNowApi():
    test_data = read_excel(mtxshop_Data_xlsx, "立即购买接口")
                # read_excel(r"../data/data.xlsx", "立即购买接口")

    # def test_buy_now(self):
    #     #实例化一个理解购买接口对象
    #     api = BuyNowApi(sku_id=541)
    #     resp = api.send()
    #     print(resp.json())
    #     pytest.assume(resp.status_code==200,f"期望值：200，实际值：{resp.status_code}")

    @pytest.mark.parametrize("casename,sku_id,num,expect_status,expect_body",test_data)
    def test_buy_now_exception(self,casename,sku_id,num,expect_status,expect_body):
        allure.dynamic.title(casename)      #因为这里有参数化，所以可以通过allure.dynamic.title来进行层级分层
        api = BuyNowApi(sku_id,num)
        resp = api.send()
        print(resp.json())
        pytest.assume(resp.status_code==expect_status,f"期望值：{expect_status},实际值：{resp.status_code}")
        pytest.assume(resp.text == expect_body,f"期望值：{expect_body},实际值：{resp.json()}")

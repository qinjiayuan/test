# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_003-member_address.py
# @author   : Gowent 
# @Time     : 2025/3/4 13:52
# @Copyright: Personal
import allure
import jsonpath
import pytest

from api.buyer.member_address_apis import AddAddressApi
from common.file_load import load_yaml_file
from common.json_util import updata_json, extract_json
from paths_manager import mtxshop_data_yaml
@allure.epic("买家接口测试")
@allure.feature("会员-会员地址相关API")
@allure.story('添加收货地址')

class TestAddAddress:

    test_data = load_yaml_file(mtxshop_data_yaml)["添加收货地址接口"]

    @pytest.mark.parametrize("casename,new_params,expect_status,expect_body", test_data)
    def test_add_address_expection(self,casename,new_params,expect_status,expect_body):
        allure.dynamic.title(casename)
        api = AddAddressApi()
        for expr , value in new_params.items():
            api.data = updata_json(api.data,expr,value)
        resp = api.send()
        code =extract_json(resp.json(),"$.code")
        print(f"响应状态码：{code}")
        print(f"类型是{type(code)}")
        pytest.assume(resp.status_code == expect_status, f"期望值：{expect_status},实际值：{resp.status_code}")
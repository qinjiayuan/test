# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : after_sales_apis.py
# @author   : Gowent 
# @Time     : 2025/2/27 11:09
# @Copyright: Personal


from api.base_api import BaseBuyerApi

class ReturnGoodsApi(BaseBuyerApi):

    def __init__(self,order_sn,sku_id):
        super().__init__()
        self.url = f"{self.host}/agter-sales/apply/return/goods"
        self.method = "post"
        self.data = {
            "service_type":"RETURN_GOODS",
            "return_num":1,
            "ship_addr":"这是详细地址",
            "ship_name":"沙陌",
            "ship_mobile":"18729399607",
            "account_type":"BANKTRANSFER",
            "bank_name":"北京银行",
            "bank_deposit_name":"北京开户行",
            "bank_account_name":"沙陌户名",
            "bank_account_number":"3456344324234",
            "reason":"商品降价",
            "problem_desc":"没啥描述，就是不想要了",
            "order_sn":order_sn,
            "sku_id": sku_id,
            "apply_vouchers":"",
            "region":2799
        }

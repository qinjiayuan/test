# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : order_apis.py
# @author   : Gowent 
# @Time     : 2025/2/27 10:55
# @Copyright: Personal
from api.base_api import BaseSellerApi


class OrderDeliveryApi(BaseSellerApi):

    def __init__(self,order_sn):
        super().__init__()
        self.method = "post"
        self.url = f"{self.host}/seller/trade/orders/{order_sn}/delivery"
        self.data = {
            "ship_no":"asdfdgdffdf",
            "logi_id":13,
            "logi_name":"中通01"
        }



class OrderPayApi(BaseSellerApi):

    def __init__(self,order_sn,pay_price):
        super().__init__()
        self.url = f"{self.host}/seller/trade/orders/{order_sn}/pay"
        self.data = {"pay_price":pay_price}
        self.method = "post"


# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : cart_apis.py.py
# @author   : Gowent 
# @Time     : 2025/2/21 10:09
# @Copyright: Personal
import requests

from api.base_api import BaseBuyerApi
from api.buyer.login_apis import BuyerLoginApi
from common.client import RequestsClient
#因为封装了公共的api请求类，所以直接继承可以使用方法
class BuyNowApi(BaseBuyerApi):

    def __init__(self,sku_id,num=1 ):
        super().__init__()  #继承父类的初始化方法
        self.url = f'{self.host}/trade/carts/buy'
        self.method = "post"

        self.data = {
            "sku_id":sku_id,
            "num":num,
            "activity_id":''
        }

    # def send(self):
    #     resp = requests.session().request(url=self.url,method=self.method,headers=self.headers,json=self.data)
    #     return resp


#清空购物车接口
class DeleteCartApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()
        self.url = f"{self.host}/trade/carts"
        self.method = "delete"

if __name__ == '__main__':
    response = BuyerLoginApi('shamo','d8c26d069c9950eec5cc79ab7b839821').send()
    BaseBuyerApi.buyer_token = response.json()["access_token"]
    print(BaseBuyerApi.buyer_token)
    resp = BuyNowApi(sku_id=541,num=0).send()
    print(resp.status_code)
    print(resp.json())

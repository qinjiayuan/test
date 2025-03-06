# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_900_order_flow.py
# @author   : Gowent 
# @Time     : 2025/2/27 11:17
# @Copyright: Personal
import allure
import jsonpath
from api.buyer.after_sales_apis import ReturnGoodsApi
from api.buyer.cart_apis import BuyNowApi
import pytest
from api.buyer.comment_apis import AddCommentApi
from api.buyer.create_trade_apis import CreateTradeApi
from api.buyer.order_apis import OrderRogApi
from api.seller.order_apis import OrderDeliveryApi, OrderPayApi

@allure.epic("主流程测试")       #使用这个来进行allure页面的报告层级
@allure.feature("订单主流程测试")
class TestOrderFlow:
    #可以将关联数据定义成类属性。给其他接口用
    order_sn = ""
    pay_price = ""

    def setup_class(self):
        print("前置开始")

    def teardown_class(self):
        print("后置开始")

    @allure.title("立即购买")
    @pytest.mark.dependency()
    def test_buy_now(self):     #购买
        api = BuyNowApi(sku_id=541)
        resp = api.send()

        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"

    @allure.title("下单")
    @pytest.mark.dependency(depends =["TestOrderFlow::test_buy_now"])
    def  test_create_trade(self):
        api = CreateTradeApi()#下单
        resp = api.send()

        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"
        TestOrderFlow.order_sn = jsonpath.jsonpath(resp.json(),"$..sn")[0]
        TestOrderFlow.pay_price = jsonpath.jsonpath(resp.json(),"$..total_price")[0]

    @allure.title("提交订单")
    @pytest.mark.dependency(depends=["TestOrderFlow::test_create_trade"])
    def test_order_delivery(self):  #提交订单
        resp = OrderDeliveryApi(order_sn=TestOrderFlow.order_sn).send()
        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"

    @allure.title("卖家发货")
    @pytest.mark.dependency(depends=["TestOrderFlow::test_order_delivery"])
    def test_order_rog(self):   #卖家发货
        resp = OrderRogApi(TestOrderFlow.order_sn).send()
        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"

    @allure.title("买家收货")
    @pytest.mark.dependency(depends=["TestOrderFlow::test_order_rog"])
    def test_order_pay(self):   #买家收货
        resp = OrderPayApi(TestOrderFlow.order_sn,TestOrderFlow.pay_price).send()
        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"

    @allure.title("发表评论")
    @pytest.mark.dependency(depends=["TestOrderFlow::test_order_pay"])
    def test_comment(self): #发表评论
        resp = AddCommentApi(TestOrderFlow.order_sn,TestOrderFlow.pay_price).send()
        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"

    @allure.title("退货")
    @pytest.mark.dependency(depends=["TestOrderFlow::test_comment"])
    def test_return_goods(self) :
        resp = ReturnGoodsApi(TestOrderFlow.order_sn,TestOrderFlow.pay_price).send()
        assert resp.status_code==200,f"期望值:200，实际值:{resp.status_code}"




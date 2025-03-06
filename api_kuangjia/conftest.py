# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : conftest.py
# @author   : Gowent 
# @Time     : 2025/2/20 10:29
# @Copyright: Personal
from typing import List

import pymysql
import pytest

from api.base_api import BaseBuyerApi, BaseSellerApi, BaseManagerApi
from api.buyer.checkout_params_apis import SetOrderPayTypeApi
from api.buyer.login_apis import BuyerLoginApi
from api.manager.login_apis import ManagerLoginApi
from common.file_load import load_yaml_file
from common.logger import GetLogger
from api.seller.login_apis import SellerLoginApi
from paths_manager import mysql_data_yaml
config = {"host": "192.168.78.128",
          "user": "root",
          "password": "123456",
          "port": 3306,
          "db": "otc",
          "charset":'utf8mb4',

          "cursorclass":pymysql.cursors.DictCursor} #能够吧每个字段的名字当成一个字典形式

#重写pytest内置的狗子函数，来解决pycharm控制台上看到的用例名称中文乱码
# @pytest.fixture(scope='session')
# def pytest_collection_modifyitems(items:List['Item']):
#     for item in items:
#         item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")

@pytest.fixture(scope='session',autouse=False)
def connect_db():
    mysql_config = load_yaml_file("mysql_data_yaml")
    mysql_config = {**mysql_data_yaml ,**{"cursorclass":pymysql.cursors.DictCurso}}
    db = pymysql.connect(**mysql_config)
    cursor = db.cursor()
    yield db , cursor
    db.close()


@pytest.fixture(scope='session',autouse=True)
def buyer_login(worker_id):     #workder_id是pytest内置的参数，代表线程号

    #判断当前进程到底给谁，给他不同的用户完成登录/也可以通过写在yaml文件里面读取来判断
    if worker_id == 'gw0'   or worker_id == 'master':   #master表示不使用分布式执行
        api = login = BuyerLoginApi('shamo','d8c26d069c9950eec5cc79ab7b839821')
    elif worker_id == 'gw1':
        api = login = BuyerLoginApi('shamo123','e622fdb8f36d56d96d8cf815d72112cb')
    login = BuyerLoginApi('shamo','d8c26d069c9950eec5cc79ab7b839821').send()
    BaseBuyerApi.buyer_token = login.json()["access_token"]     #需要给父类来赋值，那么所有继承父类的都可以用到
    BaseBuyerApi.uid = login.json()["uid"]



@pytest.fixture(scope="session",autouse=True)
def aaalogger_init():
    GetLogger.get_logger().info("日志初始化成功")

@pytest.fixture(scope='session',autouse=True)
def seller_login():
    login = SellerLoginApi("shamoseller","fafd8b5f5d11048e8078b66ab075acb3").send()
    BaseSellerApi.seller_token = login.json()["access_token"]

@pytest.fixture(scope='session',autouse=True)
def manager_login():
    login = ManagerLoginApi("admin","78b157cf49d312ecf69d1335e8b589ef").send()
    BaseManagerApi.manager_token = login.json()["access_token"]

@pytest.fixture(scope='class',autouse=False)
def init_order_params():
    #设置订单的支付类型为货到付款
    SetOrderPayTypeApi().send()
    


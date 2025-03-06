# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : client.py
# @author   : Gowent 
# @Time     : 2025/2/21 10:20
# @Copyright: Personal
import requests

from common.logger import GetLogger


#定义一个发起接口的类


class RequestsClient:
    session = requests.session()
    def __init__(self):
        self.url = None
        self.method =None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files=None
        self.resp = None

    def send(self):
        GetLogger.get_logger().debug("<=====================================================>")
        GetLogger.get_logger().debug(f"发起接口调用，url：{self.url}")
        GetLogger.get_logger().debug(f"发起接口调用，method：{self.method}")
        GetLogger.get_logger().debug(f"发起接口调用，header：{self.headers}")
        GetLogger.get_logger().debug(f"发起接口调用，data：{self.data}")
        GetLogger.get_logger().debug(f"发起接口调用，json：{self.json}")
        GetLogger.get_logger().debug(f"发起接口调用，params：{self.params}")
        GetLogger.get_logger().debug(f"发起接口调用，files：{self.files}")
        try:
            #发起接口调用
            resp = RequestsClient.session.request(
                method = self.method,
                headers=self.headers,
                url=self.url,
                data=self.data,
                json=self.json,
                params=self.params,
                files=self.files,
                verify = False #表述湖绿https的证书的校验
            )
            GetLogger.get_logger().debug(f"接口响应状态码：{resp.status_code}")
            GetLogger.get_logger().debug(f"接口调用返回结果：{resp.text}")
        except BaseException as e :
            GetLogger.get_logger().exception("接口发起失败")
            raise BaseException("接口发起失败")
        return resp
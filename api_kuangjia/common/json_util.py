# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : json_util.py
# @author   : Gowent 
# @Time     : 2025/3/2 17:17
# @Copyright: Personal
from jsonpath_ng import parse, Index, Fields
import jsonpath
from common.logger import GetLogger


#复杂的json格式处理



def updata_json(json_object,json_path,new_values):

    expr = parse(json_path)

    matches = expr.find(json_object)
    for matche in matches:
        path = matche.path
        if isinstance(path,Index):
            #判断是否需要删除
            if new_values == "$del":
                del matche.context.value[matche.path.index]
            else :
                #替换原来的字段
                matche.context.value[matche.path.index] = new_values
        elif isinstance(path,Fields):
            #判断是否需要删除
            if new_values == "$del":
                del matche.context.value[matche.path.fields[0]]
            else :
                #替换原来的字段
                matche.context.value[matche.path.fields[0]] = new_values

    return json_object


#封装通过jsonpath来提取json中的值
def extract_json(json_object,json_expr,index=0):
    """

    :param json_object:
    :param json_expr:
    :param index: 匹配的第几个值
    :return:
    """
    logger = GetLogger.get_logger()
    res = jsonpath.jsonpath(json_object,json_expr)
    #res如果提取到了值，那么是一个有数据的列表，如果没有匹配到他的值是Fasle
    if res  :
        logger.info(f"通过{json_expr}匹配到的结果是:{res}")
        if index <0:
            #如果index小于0，则认为你想要所有的匹配结果
            return res
        else :
            #如果不小于0，那么你传几，就代表你要的是匹配结果的某一个
            return res[index]
    else:
        logger.exception(f"通过{json_expr}匹配到的结果是:{res}")

if __name__ == '__main__':
    data = {
        "store": {  # 字段名: "store"
            "book": [  # 字段名: "book"
                {"title": "Sword Art Online","price":234},
                {"title": "Naruto","price":345}
            ]
        }
    }
    print(updata_json(data, 'store.book[0].title', "$del"))

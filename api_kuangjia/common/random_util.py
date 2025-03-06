# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : random_util.py
# @author   : Gowent 
# @Time     : 2025/3/6 15:52
# @Copyright: Personal
import time

#随机数据的生成
from faker import Faker

fake = Faker(locale = "zh_CN")

#随机生成一个手机号
def rdm_phone_number():
    return fake.phone_number()

#随机生成当前日期
def cur_date_time():
    return fake.date_time_between_dates()

#随机生成日期，指定日期格式
def rdm_date(pattern='%Y-%m-%d'):
    return fake.date(pattern=pattern)

#随机生成日期带时分秒
def rdm_date_time():
    return fake.date_time()

#生成当前时间戳
def cur_timesstamp(level='s'):
    if level == 's':
        return int(time.time()) #10位时间戳，精确到秒
    elif level == 'ms':
        return int(time.time()*1000)    #13位时间戳，精确到毫秒

#生成某一个时间段内的时间戳
def gen_timestamp(start_date="+0d",end_date="+1d"):
        date_time = fake.date_time_between(start_date,end_date)
        return int(time.mktime(date_time.timetuple()))

#随机生成一个地址
def get_fake_address():
    address = fake.address()
    return address

if __name__ == '__main__':
    print(get_fake_address())
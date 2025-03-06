# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : logger.py
# @author   : Gowent 
# @Time     : 2025/2/23 19:12
# @Copyright: Personal

import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
from paths_manager import project_path
import sys

class GetLogger:

    #整个框架其实只需要一个日志对象即可,可以用单利模式实现
    #把logger定义类属性，默认是None
    logger = None

    @classmethod
    # def get_logger(cls):
    #     if cls.logger is None :
    #         # 如果是空才会去创建这个logger对象
    #         #这个logger对象的名字是apiautotest--由自己定义
    #         cls.logger = logging.getLogger("apiautotest")
    #         cls.logger.setLevel(logging.DEBUG) #设置DEBUG，意味着比他高级别的日志都会被记录
    #         #定义日志的一种格式
    #         fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s] [%(funcName)s:%(lineno)d] - %(message)"
    #         fm = logging.Formatter(fmt)
    #         #创建日志处理器，把日志存储到文件，按照一定的规则
    #         tf = logging.handlers.TimedRotatingFileHandler(
    #             filename = f'{project_path}/logs/requests.log',
    #             when = 'H',  #"间隔多长时间去生成日志文件的时间单位",
    #             interval = 1 ,#间隔的数量
    #             backupCount = 3 ,
    #             encoding = 'utf-8'
    #         )
    #
    #         #讲日志输出到控制台
    #         logging.basicConfig(level=logging.DEBUG,format=fmt)
    #
    #         #在处理器中添加格式
    #         tf.setFormatter(fm)
    #         cls.logger.addHandler(tf)
    #
    #     return cls.logger
    def get_logger(cls):
        if not hasattr(cls, 'logger') or cls.logger is None:
            cls.logger = logging.getLogger("apiautotest")
            cls.logger.setLevel(logging.DEBUG)

            # 定义文件处理器
            file_formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] [%(name)s] "
                "[%(filename)s:%(lineno)d] - %(message)s"
            )
            tf = TimedRotatingFileHandler(
                filename=f'{project_path}/logs/requests.log',
                when='H', interval=1, backupCount=3, encoding='utf-8'
            )
            tf.setFormatter(file_formatter)
            cls.logger.addHandler(tf)

            # 定义控制台处理器（带颜色）
            console_formatter = logging.Formatter(
                "\033[1;32m%(asctime)s\033[0m "      # 绿色时间
                "[\033[1;35m%(levelname)s\033[0m] "                # 白色级别
                "[\033[1;33m%(name)s\033[0m] "                     # 黄色模块名
                "[\033[1;36m%(filename)s:%(lineno)d\033[0m] "     # 白色文件行号
                "- \033[1;34m%(message)s\033[0m"   # 蓝色消息
            )
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(console_formatter)
            cls.logger.addHandler(console_handler)

        return cls.logger

if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.debug("312321")
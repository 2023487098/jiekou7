"""
框架搭建:
    核心： api + case +data
        api = 封装请求业务(requests)
        case : 集成unit test实现，调用api以及参数化解析data
        data: 封装测试数据
    报告：report + tools +run_suite
        report：保存测试报告
        tools: 封装工具文件
        run_suite:组织测试套件
    配置：app.py
        app.py:封装程序常量以及配置信息
    日志：log
        log:保存日志文件
"""

import os
import  logging
import logging.handlers


# 封装接口的url前缀
BASE_URL = "http://182.92.81.159"

# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
RPO_PATH = os.path.dirname(FILE_PATH)

# 代码简化
# RPO_PATH =os.path.dirname(os.path.abspath(__file__))
# print(RPO_PATH)
# 定义个变量
TOKEN = None
USER_ID = None




# 日志模块实现
def my_log_config():
    # 配置日志，默认日志级别不能满足需求
    # 1.获取日志对象
    logger = logging.getLogger()
    # 2.配置输出级别-info以上
    logger.setLevel(logging.INFO)

    # 配置输出目标 - 控制台和磁盘文件
    to_1 = logging.StreamHandler()
    to_2 = logging.handlers.TimedRotatingFileHandler(RPO_PATH + "/log/mylog.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=14,
                                                     encoding="utf-8")
    # 配置输出格式-年月日时分秒 用户 级别  python文件 函数  行号
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 组织配置并添加进日志对象
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)


# 调用，在需要的位置调用
my_log_config()
logging.info("njusgdsdgfsdjk")

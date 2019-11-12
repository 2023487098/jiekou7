"""
    封装unittest相关实现
"""

# 导包
import json
import unittest
import requests

import app
from api.Login_api import Login
from parameterized import parameterized


# 参数化  1.导包  2.解析json文件(1.创建空列表  2.解析文件流，将数据追加进列表  3.返回列表)   3.调用
def read_json_file():
    data = []
    with open(app.RPO_PATH + "/data/login_data.json", "r", encoding="utf-8")as f:
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            ele = (mobile, password, success, code, message)
            data.append(ele)
    return data


# 创建测试类(继承unittest.TestCase)
class Test_Login(unittest.TestCase):
    def setUp(self) -> None:  # 初始化函数
        self.session = requests.Session()  # 初始化session
        self.login_obj = Login()  # 初始化api对象

    # 资源卸载
    def tearDown(self) -> None:
        self.session.close()  # 销毁session

    # 核心：测试函数-登录  1.参数化 2.请求业务  3.断言业务
    @parameterized.expand(read_json_file())  # 调用参数化数据
    def test_login(self, mobile, password, success, code, message):
        print("参数化读取的数据", mobile, password, success, code, message)
        response = self.login_obj.login(self.session, mobile, password)
        print("-" * 100)
        print("登录响应结果：", response.json())
        # 断言
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

        # 编写登录成功的测试函数

    def test_login_success(self):
        # 直接提交正向数据发送请求业务
        response = self.login_obj.login(self.session, "13800000002", "123456")
        print("登录成功的数据：", response.json())
        # 断言响应结果   data = 1a00173f-2020-40df-be36-9921f5b7a592
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        # 提取token
        token = response.json().get("data")
        print("登录后响应的token：", token)
        app.TOKEN = token  # 将token写入app.py 文件

    if __name__ == '__main__':
        unittest.main()

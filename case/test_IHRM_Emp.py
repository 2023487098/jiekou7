"""
    测试员工模块的增删改查
"""
# 导包
import logging
import unittest
import requests


# 创建测试类
import app
from api.Empapi import EmpCRUD
from case.Test_IHRM_login import Test_Login


class Test_Emp(unittest.TestCase):
    # 初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()
        self.test_login = Test_Login()

    # 资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 测试函数1：增
    # 直接提交失败的原因？1.先执行登录操作(run_suite测试套件) 2.还需要提交token
    # 解决：从登录接口提取响应的token值2.在新增业务提交token
    # 2.1 (1.ihrm_login.py上提取token 2.app.py定义变量 3.empapi.py上调用)

    def test_add(self):
        logging.info("员工新增")
        # 请求业务
        response = self.emp_obj.add(self.session, username="hahahahh122",
                                    mobile="1442341122")
        print("员工新增响应结果：", response.json())
        id = response.json().get("data").get("id")
        app.USER_ID = id
        print("新增员工的id:", id)
        # 2.断言业务
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))

    # 测试函数2：改
    def test_update(self):
        logging.info("员工修改")
        response = self.emp_obj.update(self.session, app.USER_ID, "lghawy2355")
        print("修改员工的id：", response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        # 测试函数3：查
    def test_get(self):
        logging.info("查询员工")
        response = self.emp_obj.get(self.session,app.USER_ID)
        print("查询员工：",response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 测试函数4：删
    def test_delete(self):
        logging.info("删除员工")
        response = self.emp_obj.delete(self.session,app.USER_ID)
        print("删除员工：",response.json())
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

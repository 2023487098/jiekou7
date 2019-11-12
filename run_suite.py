"""
    测试套件：
        按照需求组合被执行的测试函数
    补充说明：
        关于测试套件的组件
"""
# 导包

import unittest

import app
from case.Test_IHRM_login import Test_Login
# 实例化套件对象，组织被执行的测试函数
from case.test_IHRM_Emp import Test_Emp
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))  # 组织登录成功的测试函数
suite.addTest(Test_Emp("test_add"))  # 组织员工新增的测试函数
suite.addTest(Test_Emp("test_update"))  # 修改员工测试函数
suite.addTest(Test_Emp("test_get"))  # 组织员工查询测试函数
suite.addTest(Test_Emp("test_delete"))  # 组织员工的删除测试函数
# 执行套件，生成测试报告
# runner = unittest.TextTestRunner()
# runner.run(suite)
with open(app.RPO_PATH + "/report/report.html", "wb")as f:
    runner = HTMLTestRunner(f, title="人力资源管理系统测试报告", description="测试了人员的增删改查")
    runner.run(suite)





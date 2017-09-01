"""
assertIn(first,second,msg = None)
assertNotIn(first,second,msg = None)
断言第一个参数是否在第二个参数中，反过来讲，第二个参数是否包含第一个参数
"""

from django.test import TestCase

class TestIn(TestCase):
    def setUp(self):
        print("开始测试")

    def test_case(self):
        a = "hello"
        b = "hello world"
        self.assertIn(a,b,msg="厉害了，果然是包含的")
    def tearDown(self):
        print("游戏结束")
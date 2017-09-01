"""
assertEqual(first,second,msg=None)
assertNotEqual(first,second,msg=None)
断言第一个参数和第二个参数是否相等，如果不相等则测试失败。
msg为可选参数，用于定义测试失败时打印的信息
"""
from django.test import TestCase

class Test3(TestCase):
    def setUp(self):
        number = input("输入一个数：")
        self.number = int(number)

    def test_case(self):
        self.assertEqual(self.number,10,msg="fuck you 数字都输错")
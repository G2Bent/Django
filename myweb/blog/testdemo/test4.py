from django.test import TestCase

#用于判断质数
def is_prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

class Test(TestCase):
    def setUp(self):
        print("开始测试")
    def test_case(self):
        self.assertTrue(is_prime(7),msg="不是质数")
    def tearDown(self):
        print("游戏结束")
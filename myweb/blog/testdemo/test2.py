from django.test import TestCase
from blog.models import Publisher

class PublisherTestCase(TestCase):
    def setUp(self):
        Publisher.objects.create(name = "zhongxin",address = "tianhelu",
                                 city = "guangzhou",state_province = "China",
                                 country = "guangzhou",website = "http://www.fuckyou.com")
    def test_add_publisher_city(self):
        zhongxin = Publisher.objects.get(name = "zhongxin")
        self.assertEqual(zhongxin.city,"guangzhou")
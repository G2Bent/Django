from django.test import TestCase
from blog.models import Author
# Create your tests here.
class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(first_name = "zhang",last_name = "lei", email = "zhanglei@qq.com")
        Author.objects.create(first_name = "li",last_name = "chun", email = "lichun@qq.com")

    def test_add(self):
        """测试添加作者功能"""
        zhang = Author.objects.get(first_name="zhang")
        # zhang = Author.objects.get_queryset()
        # li = Author.objects.get_queryset()
        self.assertEqual(zhang.email,"zhanglei@qq.com")

    def test_lichun_email(self):
        li = Author.objects.get(first_name="li")
        self.assertEqual(li.email,"lichun@qq.com")

if __name__ == '__main__':
    TestCase.main()
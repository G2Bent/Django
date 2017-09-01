import unittest
import requests

class PollsTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/polls'

    def tearDown(self):
        pass
    def test_get_poll_index(self):
        """测试投票系统首页"""
        r = requests.get(self.base_url)
        code = r.status_code
        text = r.text
        self.assertEqual(code,200)
    def test_get_poll_question(self):
        """获取问题1的所有选项"""
        r = requests.get(self.base_url+'/1/')
        code = r.status_code
        text = r.text
        self.assertEqual(code,500)
        self.assertIn("3",text)

if __name__ == '__main__':
    unittest.main()

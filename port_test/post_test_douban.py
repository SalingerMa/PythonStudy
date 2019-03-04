#coding:utf-8

import requests
import unittest


class APIAutoTest28(unittest.TestCase):
    def setUp(self):
        self._url = "https://api.douban.com/v2/book/search"


    def tearDown(self):
        pass

    def testSearch01(self):
        pyload = {

            "q":"women",
            "start":"0",
            "count":"10"
        }
        rvResponseBody = requests.get(self._url, params=pyload)
        # 将返回内容转换Json格式
        jsonResponseBody = rvResponseBody.json()
        # 验证服务器返回http状态码 200
        self.assertEqual(str(rvResponseBody.status_code), "200", msg= "服务器返回http状态码error")
        # 验证服务器返回start 为0
        self.assertEqual(str(jsonResponseBody["start"]), "0", msg="服务器返回start值error")
        # 验证服务器返回count 为10
        self.assertEqual(str(jsonResponseBody["count"]), "10", msg="服务器返回count值error")
        # 验证服务器返回内容包含 我们 字符串
        self.assertIn("我们", rvResponseBody.text, msg="not found")

    def testSearch02(self):
        pyload = {

            "q":"我们",
            "start":"0",
            "count":"10"
        }
        sedHeaders = {

            "Accept":"Applicatuion/json,text/html"
        }
        rvResponseBody = requests.post(self._url, data=pyload, header=sedHeaders)
   


if __name__ == '__main__':
    unittest.main()

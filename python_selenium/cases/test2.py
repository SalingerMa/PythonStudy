# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.baidu.com")

    def test_01(self):
        time.sleep(2)
        t = self.driver.title
        print(t)

    def test_02(self):
        time.sleep(2)
        h = self.driver.window_handles
        print(h)
        # 随便写的用例，没写断言



if __name__ == "__main__":
    unittest.main()

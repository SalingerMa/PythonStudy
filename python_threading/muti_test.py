# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from runner import ThreadingTestRunner
from common.logger import logger
from time import sleep


class UNTest(unittest.TestCase):

    def setUp(self):
        logger.infout('setup')

    def tearDown(self):
        logger.infout('teardown')

    @parameterized.expand([str(i) for i in range(10)])
    def test(self, url):

        logger.infout(f'test-{url}')

if __name__ == '__main__':
    runner = ThreadingTestRunner(
        resultclass=unittest.TextTestResult,
        thread_count=2,
        failfast=False,
        verbosity=False)

    unittest.main(testRunner=runner)
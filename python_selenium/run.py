# -*- coding: utf-8 -*-
import unittest
from mod.common import Common
from time import strftime

class A(unittest.TestCase):
    pass

class B(unittest.TestCase):
    pass

def DoubleTestSuite():
    DoubleSuite = unittest.TestSuite()
    DoubleSuite.addTest(unittest.makeSuite(A))
    DoubleSuite.addTest(unittest.makeSuite(B))
    # DoubleSuite.addTest(unittest.makeSuite(VideoShareTest))
    fileName = f'Test-{strftime("%YF%m%d-%H%M%S")}'
    fileTitle = '直播登录测试'
    fileDes = ''
    # Common.create_report(fileName, fileTitle, fileDes, DoubleSuite)
    print(DoubleSuite.__dict__['_tests'][0])

if __name__ == '__main__':
    DoubleTestSuite()
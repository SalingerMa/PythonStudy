# -*- coding: utf-8 -*-
from selenium import webdriver
from.htmltestrunner import HTMLTestRunner

class Common(object):

    @classmethod
    def get_chrome_driver(cls):
        return webdriver.Chrome()

    @classmethod
    def create_report(cls, fileName, revT, revD, revTest):
        with open('../TestReport/' + fileName + '.html', 'wb') as HtmlFile:
            HTMLTestRunner(
                stream=HtmlFile,  # 文本流
                verbosity=2,  # 报告详情级别,一般都用2
                title=revT,  # 标题
                description=revD  # 描述
            ).run(revTest)


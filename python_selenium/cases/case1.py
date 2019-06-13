# -*- coding: utf-8 -*-
from res.baiduRes import BaiduRes
from mod.common import Common



url = 'https://www.baidu.com'

driver = Common.get_chrome_driver()
driver.get(url)


baidu = BaiduRes(driver)

baidu.news_link.click()

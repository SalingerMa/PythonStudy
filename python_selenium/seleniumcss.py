# -*- coding: utf-8 -*-

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
link = driver.find_element_by_id("su")
print(link.value_of_css_property("background"))
print(driver.find_element_by_link_text("新闻").value_of_css_property("font-size"))
time.sleep(2)
driver.quit()

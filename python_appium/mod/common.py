# -*- coding: utf-8 -*-
from appium import webdriver

def get_driver(noReset=False,**kwargs):
    capabilities = {
        "platformName": "Android",
        "deviceName": "fdd48786",
        "appPackage": "com.wali.live",
        "platformVersion": "8.0.0",
        "appActivity": '.main.LiveMainActivity',
    }

    if noReset:
        capabilities['noReset'] = 'true'

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    return driver
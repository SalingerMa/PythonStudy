# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
from mod.gesture import GestureAction

capabilities = {
    "platformName": "Android",
    "deviceName": "fdd48786",
    "appPackage": "com.wali.live",
    "platformVersion": "8.0.0",
    "appActivity": '.main.LiveMainActivity',
    "noReset": 'true',
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
gesture = GestureAction(driver)

sleep(5)
gesture.swipe_on('left')
sleep(1)


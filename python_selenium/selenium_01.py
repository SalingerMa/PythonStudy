# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep

data = {
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "lithium",
  "appPackage": "com.wali.live",
  "appActivity": ".main.LiveMainActivity",
  "app": r"C:\\Users\\mhm\\Downloads\\walilive-RELEASE-DEFAULT-release-4.36.43.apk",
  "newCommandTimeout": 6000,
  "unicodeKeyboard": True,
  "resetKeyboard": True,
  "autoGrantPermissions": True,
  "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', data)
sleep(2)

def target_click(x1, y1):  # x1,y1为你编写脚本时适用设备的实际坐标

    x_1 = x1 / 1080  # 计算坐标在横坐标上的比例，其中375为iphone6s的宽
    y_1 = y1 / 2040  # 计算坐标在纵坐标667为iphone6s的高
    x = driver.get_window_size()['width']  # 获取设备的屏幕宽度
    y = driver.get_window_size()['height']  # 获取设备屏幕的高度
    print(x_1 * x, y_1 * y)  # 打印出点击的坐标点
    driver.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作

driver.tap([(540,1835)],500)
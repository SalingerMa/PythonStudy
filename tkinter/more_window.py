import time
from selenium import webdriver


browser = webdriver.Chrome()

# 在当前浏览器中访问百度
browser.get('https://www.baidu.com')

# 新开一个窗口，通过执行js来新开一个窗口
js = 'window.open("https://www.sogou.com");'
browser.execute_script(js)

# 输出当前窗口句柄（百度）
baidu_handle = browser.current_window_handle

# 获取当前窗口句柄集合（列表类型）
handles = browser.window_handles
print(handles)  # 输出句柄集合
# ['CDwindow-E9B85270B51D42AF7369D81B9AA70FFE',
# 'CDwindow-90004FD79A0F59EE057846B34D0E7327']

# 获取搜狗窗口
sogou_handle = None
for handle in handles:
    if handle != baidu_handle:
        sogou_handle = handle

# 输出当前窗口句柄（搜狗）
print('switch to ', handle)
browser.switch_to.window(sogou_handle)
time.sleep(10)
browser.close() #关闭当前窗口（搜狗）

# 切换回百度窗口
browser.switch_to.window(baidu_handle)

time.sleep(10)
browser.quit()

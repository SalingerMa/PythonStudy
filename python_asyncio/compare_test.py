# -*- coding: utf-8 -*-
# 同步代码

# import time
#
# def hello():
#     time.sleep(1)
# def run():
#     for i in range(5):
#         hello()
#         print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！
# if __name__ == '__main__':
#     run()

"""
Hello World:1560236924.284579
Hello World:1560236925.2850227
Hello World:1560236926.285826
Hello World:1560236927.286281
Hello World:1560236928.2865975
"""
import time
import asyncio

# 定义异步函数
a = []
async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())
    a.append(time.time())

def run():
    for i in range(5):
        loop.run_until_complete(hello())

loop = asyncio.get_event_loop()
if __name__ =='__main__':
    run()
    print(a)

"""
Hello World:1560237008.2971125
Hello World:1560237008.2971125
Hello World:1560237008.2971125
Hello World:1560237008.2971125
Hello World:1560237008.2971125
"""
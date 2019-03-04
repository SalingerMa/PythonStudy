# -*- coding: utf-8 -*-
import time
import threadpool
def sayhello(str):
    print("Hello ",str)
    time.sleep(2)


name_list = range(20)

start_time = time.time()

pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(sayhello, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()
print('%d second'% (time.time()-start_time))
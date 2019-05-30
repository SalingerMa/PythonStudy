import threading,time


def read():
    if event.is_set():
        print("事件已设置，我要读了!!!!")
        time.sleep(1)
    else:#事件未设置
        print("还没写好，我要等咯")
        event.wait()#那么就等着咯
        #如果等到了
        print("终于等到了！那么我又可以读了")
        time.sleep(1)

def write():
    event.clear()#初始设空
    time.sleep(3)#写
    event.set()#设置事件，一旦set,那么读者wait就有返回了，读者可以继续运行了
    print("write:写好了")
    time.sleep(2)#等人读
    event.clear()#清除事件


event=threading.Event() #创建事件对象

t1=threading.Thread(target=write)
t2=threading.Thread(target=read)

t1.start()
t2.start()
t1.join()
t2.join()
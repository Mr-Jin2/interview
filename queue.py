#coding=utf-8
from time import sleep
from Queue import Queue
import threading
from random import randint

def write(queue):
    name = ['Mike','Louise','Rose']
    while True:
        queue.put(name[randint(0,2)],1)
        print '现在队列大小为:%d'%queue.qsize()
        sleep(randint(1,3))

def read(queue):
    while True:
        r = queue.get(1)
        print '现在消费了一个 %s,还剩下%d个'%(r,queue.qsize())
        sleep(randint(2,5))

if __name__ == '__main__':
    q=Queue(32)
    t1= threading.Thread(target=write,args=(q,))
    t2=threading.Thread(target=read,args=(q,))

    t1.start()
    t2.start()
    thread = threading.current_thread()#问题：加不加括号有什么区别
    print thread.getName()
    #t1.join()
    #t2.join()
    #问题：主线程结束，子线程会不会强制结束?

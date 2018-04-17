# coding=utf-8
# !/usr/bin/env python
'''''
author:Mr.Jing
created on Fri Sep 22 14:29:03 2017
platfrom:win10,python2.7
'''

from socket import *
from time import ctime
import threading
from Queue import Queue # 放每个客户端的socket
import time
import threadpool
HOST = ''
PORT = 2158
BUFSIZ = 1024
ADDR = (HOST, PORT)




def handle(queue):
            try:
                print 'in'
                q=queue.get()
                data = q.recv(BUFSIZ)  #
                print '小明'
                if data is not None:
                    q.send('[%s],%s' % (ctime(), data))
                    q.close()
            except Exception as e:
                pass


def consume(queue):
        pool = threadpool.ThreadPool(10)  # 开线程池
        print '我来啦'
        while True:
            requests = threadpool.makeRequests(handle,(queue,))#注意参数形式，一定要为可迭代对象
            print type(requests)
            for req in requests:
                pool.putRequest(req)
            pool.wait()


if __name__ == '__main__':
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(10)
    q=Queue(10)

    print  '我在%s线程中 ' % threading.current_thread().name  # 本身是主线程
    print 'waiting for connecting...'
    t1=threading.Thread(target=consume,args=(q,))#消费队列子线程
    print t1.getName()
    t1.start()
    while True:
        clientSock, addr = tcpSerSock.accept()
        print  'connected from:', addr
        clientSock.setblocking(0)
        q.put(clientSock)#将客户端连接放到队列中去
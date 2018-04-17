#coding=utf-8
from socket import *


HOST='192.168.0.165'
PORT=2158
BUFSIZ=1024
ADDR = (HOST,PORT)



if __name__ == '__main__':
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = raw_input('==>')
        if data == 'quit':
            break
        tcpCliSock.send('%s' %data) #发送数据
        rec_data = tcpCliSock.recv(BUFSIZ)
        print rec_data
        #tcpCliSock.close()


from _thread import *
from socket import *


def connectNewUser(c , ad):
    while True:
        msg = c.recv(2084)
        msg = ad[0] + ' : ' + msg.decode('utf-8')
        sendToAll(msg ,c)

def sendToAll(m , c):
    for client in clients:
        if client != c:
            client.send(m.encode('utf-8'))



s = socket(AF_INET , SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.bind((host, port))
s.listen(5)
clients = []



while True:
    c , addr = s.accept()
    clients.append(c)
    start_new_thread( connectNewUser , (c,addr) )

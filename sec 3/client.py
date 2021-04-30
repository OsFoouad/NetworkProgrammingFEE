from _thread import *
from socket import *
   
def client_thread(s):
    while True:
        msg = s.recv(2048)
        print(msg.decode('utf-8') )

s = socket(AF_INET , SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.connect((host,port))
start_new_thread(client_thread , (s,))

while True:
    s.send(input().encode('utf-8'))

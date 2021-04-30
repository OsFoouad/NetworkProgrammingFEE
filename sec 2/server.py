from _thread import *
from socket import *

def receive_thread(c):
    while True:
        x = c.recv(500)
        print("Client : ",x.decode('utf-8'))
        
        
def client_thread(c):
    start_new_thread(receive_thread , (c,))
    while True:
        c.send(input("Server : ").encode('utf-8'))
        
   
s = socket(AF_INET , SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.bind((host, port))
s.listen(5)
while True:
    c , addr = s.accept()
    print("Connection from "  , addr[0])
    start_new_thread( client_thread , (c,) )


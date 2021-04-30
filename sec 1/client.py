#client File 

from socket import *

#the next line return the socket Number
s = socket(AF_INET , SOCK_STREAM)

#Connection parameters
host = "127.0.0.1"
port = 6000

#use the fun connect to make a connection with the server
s.connect((host , port))

#send a massage 
msg = "hey , whats up"
s.send(msg.encode())
s.close()
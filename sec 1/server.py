#server File 

from socket import *

#the next line return the socket Number
s = socket(AF_INET , SOCK_STREAM)

#Connection parameters
host = "127.0.0.1"
port = 6000

# bind and listen is  a combination to give the clients chance to connect
#use the fun bind 
s.bind((host , port))

#give the current socket a listener 
s.listen(5)

while True:
	c, a = s.accept()
	print("COnnected \n")
	msg = c.recv(1024).decode()
	print(msg)
	
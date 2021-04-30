from tkinter import *
from socket import *
from _thread import *

s = socket(AF_INET , SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.bind((host , port))
s.listen(3)
c , a =  s.accept()

def recv_fun(c):
    while True:
        m = c.recv(2048)
        m = m.decode('utf-8')
        print(m)
        lb.config(text = m)

start_new_thread( recv_fun , (c,) )

def clicked():
    msg = ent.get()
    c.send(msg.encode('utf-8'))


#the main form
window = Tk()
window.title("Server Screen")
window.geometry('400x400')

#textBox creation
ent = Entry(window , width =50)
ent.place(x = 50 , y = 50)

#button creation
bt = Button(window  , text = "Send" , command = clicked)
bt.place(x = 200 , y = 100)

#label creation
lb = Label(window , text = " " )
lb.place(x = 200 , y = 150)

window.mainloop()

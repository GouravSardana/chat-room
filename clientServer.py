import socket
import tkinter
host=input("Enter host: ")
port=input("Enter port: ")
if not port:
    port=33000
else:
    port=int(port)
buff=1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
def receive():
    while True:
        try:
            msg=s.recv(buff).decode("utf-8")
            msg_list.insert(tkinter.END, msg)
        except OSError:
            break

import socket
import threading
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buff=1024
host=''
port=33000
s.bind((host,port))
clients={}
address={}
def accept_client():
    while True:
        client, client_address=s.accept()
        print("%s:%s has connected" %client_address)
        address[client]=client_address
        client.send(bytes("Type your name and hit ENTER Type {quit} to EXIT" , 'utf-8'))
        threading.Thread(target=handle_client, args=(client,)).start()
def handle_client(client):
    name=client.recv(buff).decode('utf-8')
    welcome="welcome %s to Gourav Sardana's chat room" %name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg=client.recv(buff)
        if msg!= bytes('{quit}', "utf-8"):
            broadcast(msg, name+': ')
        else:
            client.send(bytes('{quit}', 'utf=8'))
            client.close()
            del client[client]
            broadcast("%s has left the chat" %name, 'utf-8')
            break
def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, 'utf-8')+msg)
s.listen(5)
print("Waiting for connection...")
ACCEPT_THREAD = threading.Thread(target=accept_client)
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
s.close()
'''
This is main server script 
I am working on the client server GUI and after completing the client i will push it to remote.
'''

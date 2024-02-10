import time 
import socket
from sklearn.datasets import load_iris

data = load_iris()
print("Hi there")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()

while True:
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You're connected!\n".encode())
    client.send("Hello Boys!\n".encode())
    # client.send(f"{data['data'][:,0]}\n".encode())
    time.sleep(2)
    client.send("You're being disconnected!\n".encode())
    client.close()

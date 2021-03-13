import socket
import threading
import time

class Heartbeat(threading.Thread):
    def run(self):
        global client
        while True:
            print(client.recv(128).decode("utf-8"))



client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect(("localhost",8005)) 
client.send(b"Hello") 
Heartbeat().start()
day = 0
while True:
    client.send("heart".encode("utf-8")) 
    time.sleep(5)
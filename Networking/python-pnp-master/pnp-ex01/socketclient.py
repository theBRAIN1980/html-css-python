import socket

sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("10.20.40.178",8005))
sClient.close()
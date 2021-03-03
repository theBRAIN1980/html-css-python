import socket 

sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
sSocket.bind(("0.0.0.0",8005))
sSocket.listen()
print("Server is listening...")
sSocket.accept()
print("It was a pleasure")
sSocket.close()
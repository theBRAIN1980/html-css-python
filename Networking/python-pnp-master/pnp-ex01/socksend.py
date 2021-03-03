import socket 

cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect(("10.20.40.178",8005))

cSocket.send(bytearray(0x41)) 
#cSocket.sendall(b"Merge treaba?") 
 
cSocket.close()
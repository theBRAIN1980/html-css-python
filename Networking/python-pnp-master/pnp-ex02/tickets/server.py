import socket
import threading 
import memoryHandler
import base64
import authenticationService

def accept(sock):
    conn, addr = sock.accept()
    hh = HttpHandler(conn)
    hh.daemon = True
    hh.start()

class HttpHandler(threading.Thread):
    sock = None
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        request = self.sock.recv(1024).decode("utf-8") 
        parts = request.split("\r\n")

        bodyData = parts[len(parts)-1]  

        description = parts[0].split(" ")
        resource = description[1].replace("/","")
        method = description[0]
        code = "200 OK"
        locationHeader = wwwAuthHeader = body = ""

        for header in parts:
            if header.split(":")[0] == "Authorization":
                if " " in header and len(header.split(" ")) == 3:
                    encodedCreds = header.split(" ")[-1]
                    decodedCreds = base64.b64decode(encodedCreds).decode("ascii")
                    user = decodedCreds.split(":")[0]
                    password = decodedCreds.split(":")[1]
        
        if(not resource):
            body = "This is not a valid page"
            code = "404 Not Found"
        else:  
            if resource == "insert":
                authenticated = False
                if user is not None and password is not None:
                    authenticated = authenticationService.authenticate(user, password)
                if authenticated :
                    body = memoryHandler.insertticket()
                else:
                    code = "401 Unauthorized"
                    wwwAuthHeader = "WWW-Authenticate: Basic realm='myapp'\r\n"
            elif resource == "checkout":
                if method.lower() != "post":
                    body = "You must use post method on this page"
                    code = "405 Method Not Allowed" 
                elif not bodyData: 
                    body = "Not a valid body"
                    code = "400 Bad Request"
                else:
                    print(f"Validating ticket {bodyData}")
                    if not bodyData.isnumeric():
                        body = "Not a valid ticket code"
                        code = "400 Bad Request"
                    else:
                        body = memoryHandler.checkout(bodyData)
            else:
                body = "Not a valid command"
                code = "400 Bad Request"
        
            print(F"Returning {body}")
            protocol = "HTTP/1.1"
            self.sock.send(f"{protocol} {code}\r\n{locationHeader}{wwwAuthHeader}Content-Type: text/html\r\nConnection: Close\r\n\r\n{body}".encode("utf-8")) 
            self.sock.close()


sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()

while True:
    input("Press enter to get a ticket code: ")
    try:
        httpResp = urllib.request.urlopen("http://localhost:8005/insert")
        hdrs = httpResp.getheaders()
        print(hrds)
        ticketToken = httpResp.read()
        print("Your ticket code : ", ticketToken)
        authHeader =
    accept(sSocket)
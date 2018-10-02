from socket import *

def createServer():
    serverHashmap = {}
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()

    while True:
        clientInput = connectionSocket.recv(1024).decode()
        #HASHMAP LOGIC
        clientInput = clientInput.replace('\r\n', '')
        words = clientInput.split(" ")
        #GET
        if words[0] == "GET":
            if len(words) == 2:
                if words[1] in serverHashmap:
                    value = serverHashmap.get(words[1])
                    connectionSocket.send("HTTP/1.1 200 OK\n".encode())
                    connectionSocket.send(value.encode())
                    connectionSocket.send("\n".encode())
                else:
                    connectionSocket.send("HTTP/1.1 404 NOT FOUND\n".encode())
            else:
                connectionSocket.send("HTTP/1.1 400 BAD_REQUEST\n".encode())
        #PUT
        elif words[0] == "PUT":
           if len(words) == 3:
               serverHashmap[words[1]] = words[2]
               connectionSocket.send("HTTP/1.1 200 OK\n".encode())
           else:
               connectionSocket.send("HTTP/1.1 400 BAD_REQUEST\n".encode())

        #DELETE
        elif words[0] == "DELETE":
            if len(words) == 2:
                del serverHashmap[words[1]]
                connectionSocket.send("HTTP/1.1 200 OK\n".encode())
            else:
                connectionSocket.send("HTTP/1.1 400 BAD_REQUEST\n".encode())
        #CLEAR
        elif words[0] == "CLEAR":
            if len(words) == 1:
                serverHashmap.clear()
                connectionSocket.send("HTTP/1.1 200 OK\n".encode())
            else:
                connectionSocket.send("HTTP/1.1 400 BAD_REQUEST\n".encode())
        #QUIT
        elif words[0] == "QUIT":
            if len(words) == 1:
                connectionSocket.close()
            else:
                connectionSocket.send("HTTP/1.1 400 BAD_REQUEST\n".encode())
        else:
            connectionSocket.send("HTTP/1.1 220 UNSUPPORTED\n".encode())

    connectionSocket.close()

if __name__ == "__main__":
    createServer()

from socket import *

def createServer():
    serverHashmap = {}
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
            clientInput = connectionSocket.recv(1024).decode()
            # connectionSocket.send(sentence.upper().encode())
            #HASHMAP LOGIC
            clientInput = clientInput.replace('\r\n', '')
            words = clientInput.split(" ")

            # #GET
            # if words[0] == "GET":
            #     if words[1] != None:
            #         if words[1] in serverHashmap:
            #             value = serverHashmap.get(words[1])
            #             connectionSocket.send("200 OK\n".encode())
            #             connectionSocket.send(value.encode())
            #             connectionSocket.send("\n".encode())
            #         else:
            #             connectionSocket.send("404 NOT FOUND\n".encode())
            #     else:
            #         connectionSocket.send("400 BAD_REQUEST\n".encode())
            #

            #PUT
            if words[0] == "PUT":
               if words[1] != None and words[2] != None:
                   serverHashmap[words[1]] = words[2]
                   connectionSocket.send("200 OK\n".encode())
               else:
                   connectionSocket.send("400 BAD_REQUEST\n".encode())

            # #DELETE
            # elif(words[0] == "DELETE"):
            #     if(words[1] != None):
            #         serverHashmap.delete(words[1])
            #
            # #CLEAR
            # elif(words[0] == "CLEAR"):
            #     connectionSocket.send("Hello, this is CLEAR".encode())
            #QUIT
            if(words[0] == "QUIT"):
                connectionSocket.close()

            else:
                connectionSocket.send("200 UNSUPPORTED\n".encode())
        except:
            connectionSocket.close()
if __name__ == "__main__":
    createServer()

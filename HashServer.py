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
        clientInput = connectionSocket.recv(1024).decode()
        # connectionSocket.send(sentence.upper().encode())
        #HASHMAP LOGIC
        clientInput = clientInput.replace('\r\n', ' $ ')
        words = clientInput.split(" ")

        #GET
        if(words[0] == "GET"):
            connectionSocket.send("Hello, this is GET".encode())

        #PUT
        if(words[0] == "PUT"):
            connectionSocket.send("Hello, this is PUT".encode())

        #DELETE
        if(words[0] == "DELETE"):
            connectionSocket.send("Hello, this is DELETE".encode())

        #CLEAR
        if(words[0] == "CLEAR"):
            connectionSocket.send("Hello, this is CLEAR".encode())
        #QUIT
        if(words[0] == "QUIT"):
            connectionSocket.close()

if __name__ == "__main__":
    createServer()

from socket import *

def createServer():
    serverPort = 12000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')

    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        connectionSocket.send(sentence.upper().encode())
        #HASHMAP LOGIC

        #PUT

        #GET

        #DELETE

        #CLEAR

        #QUIT
        connectionSocket.close()

if __name__ == "__main__":
    createServer()

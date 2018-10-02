from socket import *

def createServer():
    serverHashmap = { }
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
        words = clientInput.split(" ")

        #GET
        if(words[0] == "GET"):
            print("Hello, this is GET")
        
        #PUT
        if(words[0] == "PUT"):
            print("Hello, this is PUT")

        #DELETE
        if(words[0] == "DELETE"):
            print("Hello, this is DELETE")

        #CLEAR
        if(words[0] == "CLEAR"):
            print("Hello, this is CLEAR")
        #QUIT
        if(words[0] == "QUIT"):
            connectionSocket.close()

if __name__ == "__main__":
    createServer()

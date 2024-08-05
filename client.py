import socket

class NumberGuessClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((self.host, self.port))
   
    def get_client_socket(self):
           return self.__client_socket
import socket

class NumberGuessClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((self.host, self.port))
   
    def get_client_socket(self):
           return self.__client_socket
    
client = NumberGuessClient('localhost', 12345)


while True:
    guess = input("Enter your guess (between 1 and 100): ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess_number = int(guess)

    client.get_client_socket().send(str(guess_number).encode())

    response = client.get_client_socket().recv(1024).decode()
    print(response)

    if response == "Correct guess! You got it!":
        client.get_client_socket().close()
        break
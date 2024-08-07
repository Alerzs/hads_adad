import socket
import random

class NumberGuessServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.random_number = random.randint(1, 100)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.client_socket = None
        print(f"Random number is: {self.random_number}")

    def start(self):
        self.server_socket.listen(1)  # Listen for incoming connections
        self.client_socket, client_addr = self.server_socket.accept()
        print(f"Connection established from {client_addr}")
        self.handle_client()

    def handle_client(self):
        while True:
            guess = self.client_socket.recv(1024).decode().strip()
            if not guess:
                continue
           
            guess_number = int(guess)

            if guess_number == self.random_number:
                self.client_socket.send("Correct guess! You got it!".encode())
                break
            elif guess_number < self.random_number:
                self.client_socket.send("Your guess is low.".encode())
            else:
                self.client_socket.send("Your guess is high.".encode())

    def close(self):
        if self.client_socket:
            self.client_socket.close()
        self.server_socket.close()


server = NumberGuessServer('localhost', 12345)
try:
    server.start()
finally:
    server.close()
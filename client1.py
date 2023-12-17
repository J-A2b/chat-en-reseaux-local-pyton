import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.username = input("Entrez votre nom d'utilisateur : ")

    def send_message(self):
        while True:
            message = input()
            self.client_socket.send(f"{self.username}: {message}".encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                print(message)
            except:
                break

    def start(self):
        send_thread = threading.Thread(target=self.send_message)
        receive_thread = threading.Thread(target=self.receive_messages)

        send_thread.start()
        receive_thread.start()

if __name__ == "__main__":
    client = ChatClient('127.0.0.1', 5555)
    client.start()

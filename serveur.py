import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.send(message)
                except:
                    self.remove(client)

    def remove(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if not message:
                    break
                self.broadcast(message, client_socket)
            except:
                self.remove(client_socket)
                break

    def start(self):
        print("Le serveur de chat est à l'écoute...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connexion établie avec {client_address}")
            self.clients.append(client_socket)
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = ChatServer('127.0.0.1', 5555)
    server.start()


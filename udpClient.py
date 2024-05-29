# UDP Client
# Author: Fernando Magallon-Romero
# RED ID: 825276901
# CS 576 Spring 2024

import socket

def main():
    server_host = '127.0.0.1'   # localhost
    server_port = 12345         # The port the server is listening on

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "Hello"
    client_socket.sendto(message.encode("utf-8"), (server_host, server_port))

    response, server_address = client_socket.recvfrom(1024)
    print("Received message from server:", response.decode("utf-8"))

    client_socket.close()

if __name__ == "__main__":
    main()

# UDP Server
# Author: Fernando Magallon-Romero
# CS 576 Spring 2024

import socket
import signal
import sys

def main():
    server_host = '127.0.0.1'   # localhost
    server_port = 12345         # port #

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_host, server_port))

    print("UDP server is listening on {}:{}".format(server_host, server_port))

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode("utf-8")
            response = "{} - {}".format(message, "There's no place like 127.0.0.1")
            server_socket.sendto(response.encode("utf-8"), client_address)
    except KeyboardInterrupt:
        print("\nServer terminated by user.")
        server_socket.close()
        sys.exit(0)

if __name__ == "__main__":
    main()

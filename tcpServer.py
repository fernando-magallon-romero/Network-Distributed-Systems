# TCP Server
# Author: Fernando Magallon-Romero
# RED ID: 825276901
# CS 576 Spring 2024

import socket

def encode_message(message):
   encoded_message = ""        # creates a empty message
   # loops through every char and increments by 1 in ASCII
   for char in message:
       encoded_message += chr(ord(char) + 1)
   return encoded_message

def main():
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_host = '127.0.0.1'   # desired host
   server_port = 12345         # desired port
   server_socket.bind((server_host, server_port))
   # listens over the host's server
   server_socket.listen(1)
   print(f"Server listening on {server_host}:{server_port}...")

   while True:
       client_socket, client_address = server_socket.accept()
       print(f"Connection to {client_address} established.")
       
       # receives message from client and reads up to 256 bytes
       message = client_socket.recv(256).decode("utf-8")
       encoded_message = encode_message(message)
       print(f"Encoded message: {encoded_message}")
       print(f"Received message from client: {message}")

       # sends encoded message to client
       client_socket.send(encoded_message.encode("utf-8"))
       client_socket.close()

if __name__ == "__main__":
   main()
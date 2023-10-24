
from Client.connection import clientConnection
from Client.handleConnection import handleConnection


SERVER_IP = input("ENTER SERVER IP")
SERVER_PORT = int(input("ENTER SERVER PORT"))




if __name__ == "__main__":
   my_socket = clientConnection()

   my_socket.createConnection(SERVER_IP , SERVER_PORT)

   handleConnection(my_socket)
   print("Closing Connection")
   my_socket.close()

    



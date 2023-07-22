# these changes are on the eoma branch
# branches are isolated environment
# Import socket module
import socket

# specify port number and header size
PORT = 6050
HEADER = 64
FORMAT = 'utf-8'

# Identify IP address of hosting server
SERVER = socket.gethostbyname(socket.gethostname())

# Assign the address
ADDR = (SERVER, PORT)

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server.bind(ADDR)

# Listen for incoming connections
server.listen()
print(f"[LISTENING] Server is listening on {SERVER}")
while True:
    # Establish connection with client
    clientsocket, address = server.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server. You have successfully connected!", "utf-8"))

    data = clientsocket.recv(1024)
    print("Server received", repr(data))

    # close the connection
    clientsocket.close()





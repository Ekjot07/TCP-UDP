import socket

# Create a TCP socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port number
server_socket.bind(('localhost', 8000))

# Listen for incoming connections
server_socket.listen()

# Wait for a client to connect
print('Waiting for a client to connect...')
client_socket, address = server_socket.accept()
print(f'Connected to {address}')

# Receive data from the client
data = client_socket.recv(1024)
print(f'Received data from client: {data.decode()}')

# Send data back to the client
message = 'Hello from the server!'
client_socket.send(message.encode())

# Close the connection
client_socket.close()
server_socket.close()

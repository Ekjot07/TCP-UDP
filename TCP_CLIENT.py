import socket

# Create a TCP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 8000))

# Send data to the server
message = 'Hello from the client!'
client_socket.send(message.encode())

# Receive data from the server
data = client_socket.recv(1024)
print(f'Received data from server: {data.decode()}')

# Close the connection
client_socket.close()

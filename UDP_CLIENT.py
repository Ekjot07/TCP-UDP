import socket

# create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send a message to the server
message = 'Hello, server!'
udp_socket.sendto(message.encode(), ('127.0.0.1', 5000))

# receive a response from the server
data, address = udp_socket.recvfrom(1024)
print('Received response from {}: {}'.format(address, data.decode()))

# close the socket
udp_socket.close()

import socket

# create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific address and port
udp_socket.bind(('127.0.0.1', 5000))

while True:
    # receive data from the socket
    data, address = udp_socket.recvfrom(1024)
    print('Received data from {}: {}'.format(address, data.decode()))

    # send a response back to the sender
    response = 'ACK: {}'.format(data.decode())
    udp_socket.sendto(response.encode(), address)

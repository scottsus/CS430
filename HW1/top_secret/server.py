import socket
import sys
import os.path
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('intro.hw1-usc430cb.usc430.isi.deterlab.net', 80)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        filename = ''
        data = connection.recv(1024)
        if data:
            filename += str(data.decode())
            f = open("/tmp/" + filename, "r")
            message = f.read()
            connection.sendall(message.encode())

    except IOError:
        f = open("tmp/404.html", "r")
        message = "404" + f.read()
        connection.sendall(message.encode())

    finally:
        connection.close()



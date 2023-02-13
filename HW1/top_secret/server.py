import socket
import os.path

SERVER_IP = 'localhost'
PORT = 80

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (SERVER_IP, PORT)
print('Starting up on %s port %s' % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)

        # Receive the data in small chunks and retransmit it
        filename = ''
        data = connection.recv(1024)
        if data:
            filename += str(data.decode())
            f = open("./tmp/" + filename, "r")
            message = f.read()
            connection.sendall(message.encode())

    except IOError:
        f = open("./tmp/404.html", "r")
        message = "404" + f.read()
        connection.sendall(message.encode())

    finally:
        connection.close()



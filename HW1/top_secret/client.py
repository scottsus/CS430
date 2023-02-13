import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (sys.argv[1], 80)
print('Connecting to %s port %s' % server_address)

sock.connect(server_address)
sock.settimeout(1)
try:
    # Send data
    filename = sys.argv[2]
    print('request:\nGET /' + filename + ' HTTP/1.1\n')

    sock.sendall(filename.encode())

    # Look for the response
    alldata = ""
    while True:
        data = sock.recv(16)
        if not data:
            if alldata[0:3] == "404":
                print(str(alldata[3 : len(alldata)]))
                break
            else:
                print("response:\nHTTP/1.1 200 OK\n\n" + str(alldata))
                break
        else:
            alldata += data.decode()

except IOError as e:
    print("error occurred")
    print(e)

finally:
    sock.close()

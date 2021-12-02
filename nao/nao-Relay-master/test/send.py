import socket


def sendData():

    host= '127.0.0.1'  # The remote host
    port = 50007  # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    s.close()
    print('Received', repr(data))


sendData()

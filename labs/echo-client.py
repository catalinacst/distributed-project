# client 
import socket

RHOST = '0.0.0.0'
RPORT = 3030
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((RHOST,RPORT))
    message = 'Hello the packet'
    while True:
        s.sendall(bytes(message,'utf8'))
        data = s.recv(1024)
        print(data,'\n')
        print('Received', repr(data))


    s.close()
        

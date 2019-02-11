# client side.
import socket
from time import sleep


RHOST = '0.0.0.0'   
# Remote host and remote port.
RPORT = 3030
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # with the  context manager with don't need to close the 
    # connection, s.close() is automatically by the cm.
    s.connect((RHOST,RPORT))
    message = 'Hello the packet'
    for i in range(101):
        s.sendall(bytes(message+str(i),'utf8'))
        data = s.recv(1024)
        sleep(0.8)  
        # delay 800ms.
        print('Received {}'.format(repr(data)))

print('Done')

        

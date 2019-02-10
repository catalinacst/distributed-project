# getting right with python3.6 and reserved keyword with. 
import socket

HOST = '0.0.0.0'
PORT = 3030     
# non-privileged ports are > 1023
BUFFER_SIZE = 1024
# message size, 1024 Bytes.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    
    # context manager here’s no need to call s.close()
    # we use ipv4 and tcp as transport.
    s.bind((HOST, PORT))        
    # asociate the ipv4 address and port to the current interface.
    
    s.listen()
    # the backlog parameter here is 128 in my linux machine. Maximum connections allowed
    # check this in /proc/sys/net/core/somaxconn.
    print('Server is listening in >> {}:{}'.format(HOST,PORT))
    conn, addr = s.accept()
    # if a client connect I'll accept, getting the new socket object and the 
    # tuple addr which is the ip and port.
    print('conn {}, add {}'.format(conn, addr))
    with conn:
        # this context manager will handle the connection until client send 
        # socket.close()
        print('Connected by {}'.format(addr))
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            conn.sendall(data)
            # sendall will ensure that all the message is sent, 
            # without matters the data lenght.

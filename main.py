#!/usr/bin/env python3.6
# h3ct0rjs, catalicacst, juanjose
# distributed systems 2018
# standard libraries
import socket
import sys
import threading
# libraries for common functions
from src.util import *

HOST = ''
PORT = 8080
BUFFER_SIZE = 1024

if __name__ == "__main__":
    banners()
    print('{} Setting and Launching Server'.format(info))
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:        
        try : 
            server.bind((HOST,PORT))
            # the backlog parameter here is 128 in my linux machine. Maximum connections allowed
            # check this in /proc/sys/net/core/somaxconn.
            server.listen()
            print('{} Server is listening in >> {}:{} '.format(ok,*(server.getsockname())))
            client_conn, client_addr = server.accept()
            print('{} New client connection from {}:{}'.format(info,*client_addr))
            print('{} Handling Connection'.format(warning))
            with client_conn: 
                print('{} Connected'.format(ok))
                while True : 
                    data = client_conn.recv(BUFFER_SIZE)
                    if not data : 
                        print('{} Client got disconnected'.format(err))
                        break
                    client_conn.sendall(data)

        except OSError as e: 
            print('{} Error during initialization'.format(err))
            sys.exit()

        
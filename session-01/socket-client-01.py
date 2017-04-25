# A basic socket client
# - open a socket
# - send data
# - receive data
# - close socket.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 21337))

s.send('Hello, server\n')
data = s.recv(1024)
s.close()

print '[received] ', data


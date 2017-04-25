# A basic socket client
# - open a socket
# - send data
# - receive data
# - close socket.
#
# A server can be emulated in another terminal using netcat
# $ nc -lk -p 21337

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 21337))

s.send('Hello, server\n')
data = s.recv(1024)
s.close()

print '[received] ', data


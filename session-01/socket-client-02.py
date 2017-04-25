# A basic socket client
# - open a socket
# - send data
# - receive data
# - close socket
# A server can be emulated in another terminal using netcat
# $ nc -lk -p 21337
#
# 02
# Adding sys to allow for port argument (poor man's option parser)

import socket
import sys

port = sys.argv[1]

print '[*] Connecting to port %s on 127.0.0.1' % str(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make sure an int is used.
s.connect(('127.0.0.1', int(port)))

s.send('Hello, server\n')
data = s.recv(1024)
s.close()

print '[received] ', data


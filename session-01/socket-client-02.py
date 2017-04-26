# A basic socket client
# - open a socket
# - send data
# - receive data
# - close socket
# A server can be emulated in another terminal using netcat
# $ nc -lk -p 21337
#
# 02
# - adding sys to allow for port argument (poor man's option parser)
# - adding a list example.. just to demonstrate

import socket
import sys

"""
These constants represent the address (and protocol) families, used for the
first argument to socket().

    socket.AF_UNIX
    socket.AF_INET
    socket.AF_INET6

These constants represent the socket types, used for the second argument to
socket().

    socket.SOCK_STREAM
    socket.SOCK_DGRAM
    socket.SOCK_RAW
    socket.SOCK_RDM
    socket.SOCK_SEQPACKET

"""

port = sys.argv[1]

ip_list = ['192.168.2.2', '192.168.2.3', '192.168.2.4']

print '[*] Connecting to port %s on 127.0.0.1' % str(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make sure an int is used.
s.connect(('127.0.0.1', int(port)))

s.send('Hello, server..\n')

for ip in ip_list:
    s.send(ip + '\n')

s.close()


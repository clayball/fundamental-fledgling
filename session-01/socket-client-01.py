#!/usr/bin/env python

"""
A basic socket client
- open a socket
- send data
- receive data
- close socket.

A server can be emulated in another terminal using netcat
$ nc -lk -p 21337
"""

import socket

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

Reference, https://docs.python.org/2/library/socket.html
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 21337))

s.send('Hello, server\n')
data = s.recv(1024)
s.close()

print '[received] ', data


#!/usr/bin/env python

"""
A basic socket client
- open a socket
- send data
- receive data
- close socket
A server can be emulated in another terminal using netcat
$ nc -lk -p 21337

socket-client-02
- adding sys to allow for port argument (poor man's option parser)

socket-client-03
- adding option parser
- adding try/except socket error
- adding while loop
- adding input file for reading
- sending data from input file
- removing recv data.. just send data
"""

import socket
import sys
import os.path
from optparse import OptionParser

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

"""
PRELIMINARIES

Get options from option parser, etc.
"""

# Use OptionParser just to make the interface and feedback nice
parser = OptionParser()
# We setting a sane default so this is not required.
parser.add_option("-p", "--port", dest="port", default="21337",
                    help="Server port to connect to.")
(options, args) = parser.parse_args()
port = options.port

infile = 'subnets.csv'

try:
    os.path.isfile(infile)
except IOError:
    print '[-] File does not exist!'
    sys.exit()


"""
CONNECT TO REMOTE SERVER

This is the main part of our script.
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Make sure an int is used.
    print '[*] Connecting to port %s on 127.0.0.1' % str(port)
    s.connect(('127.0.0.1', int(port)))
except socket.error, msg:
    print "[ERROR] Caught exception socket.error : %s" % msg
    sys.exit()

ifile = open(infile, 'r')

s.send('Subnet list..\n')
for f in ifile:
    print '[*] sending: %s' % f
    s.send(f)

s.close()

print '[*] Goodbye'

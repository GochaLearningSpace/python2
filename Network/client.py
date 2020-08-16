#! /usr/bin/env python2 

import socket 

s = socket.socket()

host = socket.gethostname()
port = 1025

s.connect ((host , port ))
print s.recv(1025)

s.close()

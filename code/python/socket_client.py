# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:53:24 2020

@author: ell
"""


import socket

PORT = 50000
BUFFER_SIZE = 1024 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", PORT))
    data = input("please input >")
    s.send(data.encode())
    print(s.recv(BUFFER_SIZE).decode())
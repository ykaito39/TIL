# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:13:23 2020

@author: ell
"""

import time
from socket import socket, AF_INET, SOCK_STREAM

HOST        = 'localhost'
PORT        = 52000

def com_send(msg):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((HOST, PORT))
        
        sock.send(msg.encode("utf-8"))
        
        sock.close()
    except Exception as e:
        print(str(e))
        
def interval_signal(sec):
    try:
        #sock = socket(AF_INET, SOCK_STREAM)
        #sock.connect((HOST, PORT))
        
        while True:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((HOST, PORT))
            time.sleep(sec)
            sock.send("interval".encode("utf-8"))
            print("sent")
            sock.close()
        
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    #interval_signal(1)
    while True:
        s = input("> ")
        if s == "q":
            exit()
        com_send(s)

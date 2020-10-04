#!/usr/bin/python3
# N11rm44L 7w44711
# GitHub : https://www.github.com/niirmaaltwaatii/PyPortScanner

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(4)

# for specific scan
def sscan():
    host = input("IP Address : ")
    port = int(input("Specific Port : "))
    portScan(host, port)

# for fixed scan
def fscan(port) :
    host = input("IP Address : ")
    portScan(host, port)


# scan port
def portScan(host, port):
    if s.connect_ex((host, port)):
        print(f"{host}:{port} is closed")
    else:
        print(f"{host}:{port} is Open")

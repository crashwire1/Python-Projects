#!/usr/bin/python3
from datetime import datetime
import socket
import sys
import threading
import queue

# Thread-safe queue for managing open ports
open_ports = queue.Queue()

# Function to scan ports
def port_scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))  # Error indicator 
        if result == 0:
            print(f'>> Port {port} is open')
            open_ports.put(f'Port {port} open on target {target}\n')  # Store results in the queue
        s.close()
    except socket.error as e:
        pass  # Ignore socket errors to avoid clutter
    except Exception as e:
        print(f'Unexpected error on port {port}: {e}')

# Function to write results to file
def write_results(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        while not open_ports.empty():
            f.write(open_ports.get())

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 port_scan.py <target IP Address>")
        sys.exit(1)

    target = sys.argv[1]
    try: 
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    # Banner
    print("*" * 30)
    print("             .-.")
    print("            (0.0)")
    print("          '=.|m|.='")
    print("          .='`\"``=.")
    print("         PORT SCANNER")
    print("*" * 30)
    print("Author: Crashwire -> (Credit: Heath Adams/TCM Sec)")
    print("-" * 50)
    print(f'Scanning target {target_ip}')
    print(f'Time started: {datetime.now()}')
    print("-" * 50)

    # Multi-threading with a thread pool
    thread_limit = 10000  # Limit active threads
    threads = []
    for port in range(1, 65536):
        thread = threading.Thread(target=port_scan, args=(target_ip, port))
        threads.append(thread)
        thread.start()
        
        if len(threads) >= thread_limit:  # Wait for some threads to complete
            for t in threads:
                t.join()
            threads = []

    # Ensure all threads complete
    for t in threads:
        t.join()

    # Write results to file
    write_results('port_scan.txt')
    print("\nScan Completed!")

if __name__ == "__main__":
    main()

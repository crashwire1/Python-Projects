#!/usr/bin/python3
from scapy.all import sniff, Dot11

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        # Probe Requests
        if pkt.type == 0 and pkt.subtype == 4:
            print(f"[Probe] Device: {pkt.addr2} is probing for SSID: {pkt.info.decode('utf-8', 'ignore')}")
        # Beacon Frames
        elif pkt.type == 0 and pkt.subtype == 8:
            ssid = pkt.info.decode('utf-8', 'ignore') or "Hidden SSID"
            print(f"[Beacon] SSID: {ssid}, BSSID: {pkt.addr2}, Channel: {ord(pkt[Dot11Elt:3].info)}")

print("Listening for Probe Requests and Beacon Frames...")
sniff(iface="wlan0mon", prn=packet_handler, store=False)

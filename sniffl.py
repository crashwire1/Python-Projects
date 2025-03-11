#!/usr/bin/python3
from scapy.all import sniff, Dot11, Dot11Elt

#Banner
print("*" * 30)
print("           .-.")
print("          (0.0)")
print("        '=.|m|.='")
print("        .='`\"``=.")
print("WIRELESS PROBE & BEACON SNIFFER")
print("    Author: Crashwire")
print("*" * 30)

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        # Probe Requests
        if pkt.type == 0 and pkt.subtype == 4:
            print(f"[Probe] Device: {pkt.addr2} is probing for SSID: {pkt.info.decode('utf-8', 'ignore')}")
        # Beacon Frames
        elif pkt.type == 0 and pkt.subtype == 8:
            ssid = pkt.info.decode('utf-8', 'ignore') or "Hidden SSID"
            channel_info = pkt.getlayer(Dot11Elt, ID=3)  # Get channel element
            channel = ord(channel_info.info) if channel_info else "Unknown"
            print(f"[Beacon] SSID: {ssid}, BSSID: {pkt.addr2}, Channel: {channel}")
            f = open("sniffl-output.txt", "a", encoding="utf-8")
            f.write(f"[Beacon] SSID: {ssid}, BSSID: {pkt.addr2}, Channel: {channel}\n")

print("Listening for Probe Requests and Beacon Frames...")
sniff(iface="wlan0mon", prn=packet_handler, store=False)

if __name__ == "___main___":
    main()

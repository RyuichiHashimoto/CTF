import sys
import scapy
import os
from scapy.all import rdpcap
import re
from typing import TextIO

def extract_strings(data):
    """
    Extract printable ASCII strings from binary data.
    Similar to the `strings` command in Unix.
    """
    pattern = re.compile(b"[ -~]{4,}")  # Match sequences of 4 or more printable ASCII characters
    return pattern.findall(data)

def strings_pcap(file_path):
    """
    Process a pcap file and extract strings for each packet.
    Include packet number in the output.
    """
    packets = rdpcap(file_path)
    
    for i, packet in enumerate(packets, start=1):
        if hasattr(packet, 'payload') and packet.payload:
            raw_data = bytes(packet.payload)
            strings = extract_strings(raw_data)
            for string in strings:
                print(f"[{i}]", string.decode('utf-8', errors='replace'))

def display_helpmessage():
    print("Usage: python strings_pcap.py <pcap_file>")
    print("Process a pcap file and extract printable ASCII strings from each packet.")
    exit(0)

# 使用例
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        display_helpmessage()
        exit(1)

    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        display_helpmessage()
        exit(2)
        
    
    pcap_file = sys.argv[1]  # 対象のPCAPファイルを指定

    if not os.path.exists(pcap_file):
        print(f"error: '{pcap_file}' No such file",file=sys.stderr)
        exit(2)

    output = strings_pcap(pcap_file)






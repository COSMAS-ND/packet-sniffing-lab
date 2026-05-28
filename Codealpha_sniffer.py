from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP]
        print("\n[+] Packet Captured")
        print(f"Source IP: {ip.src}")
        print(f"Destination IP: {ip.dst}")

        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print("Protocol: TCP")
            print(f"Source Port: {tcp.sport}")
            print(f"Destination Port: {tcp.dport}")

        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print("Protocol: UDP")
            print(f"Source Port: {udp.sport}")
            print(f"Destination Port: {udp.dport}")

        else:
            print("Protocol: Other")

sniff(prn=process_packet, store=False)



from scapy.all import sniff, Raw


def process_tcp_packet(packet):
    if Raw in packet:
        if 'POST' in packet[Raw].load:
            print(packet[Raw].load.split('\r\n')[-1])

sniff(filter='tcp', prn=process_tcp_packet)
